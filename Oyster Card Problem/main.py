"""
The Oyster Card Problem:

    - user can add balance
    - book a Tube ride
    - book a bus ride
    - handle all the edge case scenarios
    - If the current balance is less than the minimum balance. So, system will prompt a request for adding amount.

Minimum balance in the card - £30
● Any bus journey costs a flat rate of £1.80 regardless of the journey stations.
● The maximum possible fare is therefore £3.20

Note:
A limited case scenario


"""
import sys
sys.path.append('D:/alef_education')
sys.path.append('D:/alef_education/app')

from app.oyster_card import oyster_menu

menu_obj = oyster_menu()
menu_obj.main_menu()