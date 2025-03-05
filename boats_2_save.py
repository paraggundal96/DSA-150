from typing import List

'''
The maximum number of people a boat can carry is 2
The maximum weight a boat can carry is an input called LIMIT
Every Individual has a weight lower than or equal to limit
'''

class Boat:

    def min_boat(self, people: List[int], limit: int) -> int:
        heavP = len(people)-1
        lightP = 0
        boat = 0
        people.sort()
        while(lightP <= heavP):
            if(people[lightP] + people[heavP] <= limit):
                boat += 1
                lightP += 1
                heavP -= 1
            else:
                boat +=1 
                heavP -= 1
        return boat

    

boats = Boat()
print(boats.min_boat([3,2,1,2],4))

            
            

