'''
        Submissiom performance

- Runtime: 630ms 
- Memory Usage: 20.10 MB

        Submission Results

- Memory better than 27.14% of the total submissions

- Runtime better than 83.97% of the total submissions 

'''
from typing import List

class Solution:
    def lemonadeChange(self, bills:List[int]) -> bool:
        account = {5:0,10:0,20:0}

        for customer in bills:
            account[customer] += 1
            
            # We need to calculate change
            if customer != 5:
                change_collected = 0
                change_needed = customer - 5
                bills_to_build_change = sorted([_ for _ in account.keys() if _ < customer], reverse=True) # we prefer first to remove the highets values
                for bill in bills_to_build_change:
                    available_qty = account[bill]
                    take_from_account = change_needed//bill

                    # There's no enough money saved to build the change
                    if (available_qty < take_from_account):
                        if min(bills_to_build_change) == bill:
                            return False
                        else:
                            # We can check if we can build the change with lower denomination
                            pass
                    
                    # There's enough money, now we need to remove the change given from our account
                    else:

                        account[bill] -= take_from_account
                        change_collected += bill*take_from_account
                        change_needed -= bill*take_from_account


            else:
                pass

        return True


sol = Solution()
assert(sol.lemonadeChange([5,5,5,20,5,5,5,20,5,5,5,10,5,20,10,20,10,20,5,5]) == False)
assert(sol.lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]) == True)
assert(sol.lemonadeChange([5,5,5,10,20]) == True)
assert(sol.lemonadeChange([5,5,5,10,5,5,10,20,20,20]) == False)
