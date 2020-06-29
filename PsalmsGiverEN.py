from PsalmsGiverDefinitions import *

print("Welcome do PSALM GIVER - it will assign you a psalm for a day")

#First - the names:
the_names = namesTaker()

#Second  - how many days of challenge for everybody
the_days = daysNumberReceiver()

# And here we go!

for name in the_names:
    PsalmsGiver(name, the_days)

input("Thank You for Usind PSALM GIVER \n press enter")



