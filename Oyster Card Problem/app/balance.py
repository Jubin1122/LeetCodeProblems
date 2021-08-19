
"""
balance class handles balance related queries
"""
import sys
sys.path.append('D:/alef_education')
import values as val


class balance:
    journey_history = list()
    status_track ={'f_status':None}          # To keep track of the status(IN, OUT) while journey         

    def __init__(self, balance):
        self.balance = balance

    # Check whether there is sufficient balance in the card.
    def is_sufficient_bal(self, status, trans_type):

        train_max_fare = val.train_fare_max
        bus_max_fare = val.bus_fare_max
        
        if status == 'IN' and trans_type == 'train' and self.get_balance() < train_max_fare:
            return False

        elif status == 'IN' and trans_type == 'bus' and self.get_balance() < bus_max_fare:
            return False
        
        return True

    # For loading balance in the card
    def load_bal(self, amount):
        
        if self.balance + amount > val.max_balance_limit:
            print('Maximum limit of the card is €91.')
            return False
         
        self.balance += amount
        return self.balance

    # For estimating fare and updating balance in the card
    def cal_new_balance(self, status, station, trans_type):

        if self.status_track['f_status'] == 'OUT' and self.journey_history:
            self.status_track['f_status'] = None
            self.journey_history = list()

        if status == 'IN' and trans_type == 'train' and self.edge_cases_status(status) and self.is_sufficient_bal(status,trans_type):
            self.status_track['f_status'] = status
            self.new_bal = self.get_balance() - val.train_fare_max
            self.entry_station = station
            self.in_trans_type = trans_type

        elif status == 'IN' and trans_type == 'bus' and self.edge_cases_status(status) and self.is_sufficient_bal(status,trans_type):
            self.status_track['f_status'] = status
            self.new_bal = self.get_balance() - val.bus_fare_max
            self.entry_station = station 
            self.in_trans_type = trans_type

        elif status == 'OUT' and self.edge_cases_status(status):
            self.status_track['f_status'] = status
            last_IN_transp_type = self.in_trans_type
            if last_IN_transp_type == 'bus':
                journey_log = {'entry_station':self.entry_station, 'exit_station':station, 'balance':round(self.new_bal,2), 'fare':val.bus_fare_max}
                self.journey_history.append(journey_log)
                self.balance = self.new_bal

            else:
                start_station = self.entry_station
                start_zones = val.stations[start_station]
                dest_zones = val.stations[station]

                comb_zones  = start_zones+dest_zones
                if not(len(set(dest_zones)) > 1):
                    if_more_than_2 = abs(dest_zones[0] - start_zones[0])
                else:
                    if_more_than_2 = 0

                if comb_zones == [1,1] and (len(start_zones)==1 and len(dest_zones)==1): # Anywhere in Zone 1 
                    self.fare = 2.50
                    self.new_bal = self.get_balance() - self.fare 
                    
                
                elif len(list(set(comb_zones))) == 1 and (list(set(comb_zones))[0] == 2 or list(set(comb_zones))[0] == 3) and (len(start_zones)==1 and len(set(dest_zones))==1): # Any one zone outside zone 1 
                    self.fare = 2.00
                    self.new_bal = self.get_balance() - self.fare 
                    

                elif (1 in comb_zones) and ((2 in comb_zones) or (3 in comb_zones)) and (len(start_zones)==1 and len(set(dest_zones))==1) and if_more_than_2 == 1: # Any two zones including zone 1
                    self.fare = 3.00
                    self.new_bal = self.get_balance() - self.fare 
                    

                elif not(1 in comb_zones) and ((2 in comb_zones) or (3 in comb_zones)) and (len(start_zones)==1 and len(set(dest_zones))==1): # Any two zones excluding zone 1
                    self.fare = 2.25
                    self.new_bal = self.get_balance() - self.fare 
                    

                elif if_more_than_2 > 1 and (len(start_zones)==1 and len(set(dest_zones))==1): # More than two zones (3+)
                    self.fare = 3.20
                    self.new_bal = self.get_balance() - self.fare 

                elif len(start_zones)==1 and len(set(dest_zones)) > 1: # When more than one fare is possible
                    print('multiple fares possible, flat rate: 2.50')
                    self.fare = 2.50
                    self.new_bal = self.get_balance() - self.fare 
                
                elif len(set(start_zones))>1 and len(dest_zones) == 1: # When more than one fare is possible
                    print('multiple fares possible, flat rate: 2.50')
                    self.fare = 2.50
                    self.new_bal = self.get_balance() - self.fare 

                else:
                    return False
    

                #Update the balance after the trip complete
                journey_log = {'entry_station':self.entry_station, 'exit_station':station, 'balance':round(self.new_bal,2), 'fare':self.fare}
                self.journey_history.append(journey_log)

                self.balance = round(self.new_bal,2)
        elif status == 'IN' and not(self.is_sufficient_bal(status,trans_type)):
            print('Enter amount')
            amt = input()
            upd_bal = self.load_bal(int(amt))
            print(f'Current Balance after recharge: €{upd_bal}')
            self.cal_new_balance(status, station, trans_type)

        else:
            return False



        return self.new_bal

    #Check the whether Journey starts from IN or OUT; If out will return False
    def edge_cases_status(self,status):
       
        if status == 'IN' and not(self.status_track['f_status']):
            return True
        elif status == 'OUT' and self.status_track['f_status'] == 'IN':  
            return True
        else:
            return False  # edge cases are clear

    #Print a list of the jouney history.
    def trip_history(self):       

        if self.journey_history:
            return self.journey_history

        return False

    # Get Balance
    def get_balance(self):
        return self.balance
