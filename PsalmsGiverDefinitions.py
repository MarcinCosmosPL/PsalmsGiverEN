MaxDays = 150 #there are 150 psalms in the Bible but we can change it here

#Get the names of the users:
def namesTaker():  #Ask for the names of demanded number of users and return list of these names
    namesList = []
    taking = True
    userNumber = 1
    while taking:
        userName = input("User no. {} \n What is Your name? Put it here and press enter: \n".format(userNumber))
        #ASK THE NAME
        if userName != "":
            namesList.append(userName)
            userNumber+=1
        else:
            print("no name added!")
            continue

        #IS THIS ALL? - inside loop
        while True:
            continuationChoice = input("Do you want to enter next user? Put yes or no and press enter: \n")
            if continuationChoice.lower() == "yes":
                break #just break the inside loop
            elif continuationChoice.lower() == "no":
                return namesList #Result of namesTaker
            else:
                print("invalid answer - repeat!")

### TEST

##mojaLista = namesTaker()
##for i in mojaLista:
##    print(i)


### OK IT WORKS            
            
def daysNumberReceiver(MaxDays=MaxDays): #single question - how many days do the parcipants want to do the challenge    
    #Loop to receive the demanded number of days
    while True:
        try:
            days = input("Put the number of days (up to {}) and press enter \n".format(MaxDays))
            if int(days)%1 == 0 and int(days) > 0 and int(days) < MaxDays+1:
                return int(days)
                #break
            else:
               print('Error! Give an integer up to {}'.format(MaxDays))
               continue
        except:
            print('Error! Give an integer up to {}'.format(MaxDays))

### TEST
##myDays = daysNumberReceiver()
##print(myDays)

def PsalmsGiver(person, days, MaxDays=MaxDays): #draw psalms for one person and create a file with them
    #Loop to create the list of drawn psalms (draw from number of psalms without repetitions)
    psalms = []
    p = 1
    import random
    while p <= days:
        nextPs = random.randint(1, MaxDays)
        if nextPs in psalms:
            continue
        else:
            psalms.append(nextPs)
            p = p+1


    ### SO FAR SO GOOD



    #LOOP to display each day with its assigned psalm and create a file

    import os
    PsalmyFileName = "Received_Psalms_for_{}.txt".format(person)
    PsalmsResult = open(PsalmyFileName, 'w')


    i=1
    for psalm in psalms:
        #print("Day:", i, " Psalm:", psalm) #uncommento display every psalms number in the log
        line = "Day: "+ str(i)+ " Psalm: "+ str(psalm)+ '\n'
        PsalmsResult.write(line)
                      
        i=i+1

    PsalmsResult.close()
    #After creating a file - put the adnotation

    print("Script has created a file:", PsalmyFileName, "in the actual folder.")


