#import practiceClassKEY as p
import practiceClass as pc
import csv


shows = {
    "play1":{
        'id':3245,
        'name':'Phantom of the Opera',
        'capacity':65,
        'event_date':'03/01/2023'
    },
    "play2":{
        'id':1548,
        'name':'The Music Man',
        'capacity':45,
        'event_date':'05/15/2023'
    },
    "play3":{
        'id':9587,
        'name':'Hamilton',
        'capacity':124,
        'event_date':'07/21/2023'
    },
    "play4":{
        'id':6254,
        'name':'The Lion King',
        'capacity':89,
        'event_date':'09/29/2023'
    },

}

'''using the above dictionary iterate through it and create an instance of the 
play class that has id 9587
NOTE: Do not hard code the values to create the instance but use
keys and values from the dictionary '''
#instance = pc.Play(9587)
dictionary = {}

for key in shows:
    if shows[key]["id"] == 9587:
        #iD = shows[key]["id"]
        #name = shows[key]["name"]
        #seats = shows[key]["capacity"]
        #date = shows[key]["event_date"]
        #instance = pc.Play(iD, name, seats, date)
        #print("yes")
        instance = pc.Play(shows[key]["id"],shows[key]["name"],shows[key]["capacity"],shows[key]["event_date"])
        #dictionary[instance.get_iD()] = [instance.get_name()]

#print(dictionary)




'''using the bookings.csv file process only those 
reservations for the same play (9587). Create an 
instance of the Booking class for each customer
that is going to play 9587 - Hamilton. 
if the play reaches capacity print out a 
error message as shown in output.JPG'''


#open the csv file in read mode
infile = open("bookings.csv","r")
csvfile = csv.reader(infile, delimiter = ",")
next(csvfile)
open_seats = 124
num = 1

#for line in csvfile:
#    print(line)

avail_seats = instance.get_seats()

for line in csvfile:
    if float(line[0]) == 9587:
        avail_seats = avail_seats - 1
        #instance.seats_left(124)
        #print(instance.get_move())
        if avail_seats > -1:
            continue
        else:
            print("*********ERROR*********\n")
            print("Guest Name: " + line[1] + "\n")
            print("Sorry, show: Hamilton is sold out \n")



        


'''
print(avail_seats)

for records in csvfile:
    if float(records[0]) == 9587:
        avail_seats-=1
        if avail_seats > 0:
            print("Welcome")
        else:
            print("*********ERROR*********\n" + "GuestName: " + records[1] + "\n" + "Sorry, show: Hamilton is sold out")
'''


#create a csv object from the file object from the step above
#if instance[]



# use a for loop to iterate through each record in the bookings file

