"""
oyster_menu class handles services for the user
"""

import sys
sys.path.append('D:/alef_education')
sys.path.append('D:/alef_education/app')
from app.balance import balance
import values as val

class oyster_menu(object):
    
    def __init__(self):
        self.bal_obj = balance(30)       # instantiating balance class and loading a minimum balance

    # Checking whether the user input is present for the requested services 
    def valid_option(self, code, menu):
        if code.isdigit() and int(code) in range(1,menu+1):
            return True
        if int(code) == 0:
            return True
        return False


    def station_menu(self,status):

        menu_list = []
        for i in val.stations.keys():
            menu_list.append(i)
        
        print('Enter a station code from  1 to 6, Bus Exit: 0')
        station_code = input(
            '''
            - Enter on which station you want to board or exit
            - For bus exit, enter 0

            Note:
            For train and bus(boarding): Enter options from 1 to 6
            For bus exit: Enter 0 and enter the location
            '''
        )

        if self.valid_option(station_code, len(menu_list)):

            if int(station_code) == 0:
                print('enter the bus destination')
                station = input()
                self.transp_type(status,station)
            else:    
                station = menu_list[int(station_code)-1]
                self.transp_type(status,station)
            
        else:
            print(f'{station_code} is not a correct station code, Enter the correct code!')
            self.station_menu(status)

    def transp_type(self, status, station):

        transport_mode = ['train', 'bus']
        print('Enter the transport Type; 1-Train, 2-Bus!!')
        transp_code = input(
            '''
            Select the transport type: 
                - 1-Train
                - 2-Bus

            '''
        )        

        if self.valid_option(transp_code, len(transport_mode)):
            if transport_mode[int(transp_code)-1] == 'train':
                x = self.bal_obj.cal_new_balance(status, station, 'train')      # Calling balance class to calculate trip fare and update the balance
                if not(x):
                    print('Starting point cannot be at exit')
                    raise SystemExit
                    
            else:
                x = self.bal_obj.cal_new_balance(status, station, 'bus')
                if not(x):
                    print('Starting point cannot be at exit')
                    raise SystemExit
            if status == 'IN':
                print('Now you can board to the station')
            else:
                print('Exited the station')    

            self.main_menu()

        else:
            print(f'{transp_code} is not a valid code for tranport mode')
            self.transp_type(status,station)
    

    def main_menu(self):
        
        ''' Enter a valid service from 1 to 6!!'''
        options = input(
            '''
            - For boarding(IN); Enter-1
            - For exit(OUT); Enter-2
            - For Current Balance; Enter-3
            - For Trip History; Enter-4
            - For addinf balance; Enter-5
            - For Exit out of the System; Enter-6
            
            '''
        )

        if self.valid_option(options,6):
            opt = int(options)
            if opt == 1:
                print('Boarding!!')
                self.station_menu('IN')
                self.main_menu()
            
            elif opt == 2:
                print('Exit!!')
                self.station_menu('OUT')
                self.main_menu()
            
            elif opt == 3:
                print(f'Current Balance: €{self.bal_obj.get_balance()}')
                self.main_menu()

            elif opt==4:
                out = self.bal_obj.trip_history()
                if out:
                    print(out[0])
                else:
                    print('No history found!!')
                self.main_menu()
            
            elif opt == 5:
                print('Enter amount to add')
                amt = input()
                out = self.bal_obj.load_bal(int(amt))
                if not(out):
                    print('Choose 5 renter the amount.')
                    self.main_menu()
                
                print(f'Current Balance after recharge: €{self.bal_obj.get_balance()}')
                self.main_menu()


            elif opt == 6:
                print('Thanks for using Oyster Card!!')
                raise SystemExit

        else:
            print(f'{options} is not a valid option in the menu, renter the value')
            self.main_menu()



            


        

