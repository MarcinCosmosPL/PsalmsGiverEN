import random

print("Welcome do PSALM GIVER - it will assign you a psalm for a day")

MaxDays = 150 #there are 150 psalms in the Bible but we can change it here

#Get the name of the user:
userName = input("What is Your name? Put it here and press enter: \n")



#Loop to receive the demanded number of days
while True:
    try:
        days = input("Put the number of days (up to {}) and press enter \n".format(MaxDays))
        if int(days)%1 == 0 and int(days) > 0 and int(days) < MaxDays+1:
           break
        else:
           print('Error! Give an integer up to {}'.format(MaxDays))
           continue
    except:
        print('Error! Give an integer up to {}'.format(MaxDays))


#Loop to create the list of drawn psalms (draw from number of psalms without repetitions)
psalms = []
p = 1
while p <= int(days):
    nextPs = random.randint(1, MaxDays)
    if nextPs in psalms:
        continue
    else:
        psalms.append(nextPs)
        p = p+1

#Preview:
#print(psalms)


#LOOP to display each day with its assigned psalm and create a file

import os
PsalmyFileName = "Received_Psalms_for_{}.txt".format(userName)
PsalmsResult = open(PsalmyFileName, 'w')


i=1
for psalm in psalms:
    print("Day:", i, " Psalm:", psalm)
    line = "Day: "+ str(i)+ " Psalm: "+ str(psalm)+ '\n'
    PsalmsResult.write(line)
                  
    i=i+1

PsalmsResult.close()
#After creating a file - put the adnotation

print("Script has created a file:", PsalmyFileName, "in the actual folder.")


input('Press enter to end')

## Notes to experiment with rebuilding the script: ###
# Find a way to implement some elegant way of quiting the script
# Right now it is very simple - I created it at the beggining of Python learnig, but it could use some functions or maybe even clas
# Maybe it could be rebuild to serve more than one user at time and enable the repetition of single usage - some mainloop maybe


