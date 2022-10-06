'''Create two class definitions

1) a Play class that has attributes for id, name, number of seats, date and status. ✅
Set the value of the status attribute to True as default. 
Create an accessor method each for the name, seats and status attributes only. ✅
Create a method called 'seats_left' that will reduce the number of seats by 1 every time it is called.
Create a mutator method called 'set_status' that will change the status attribute to False.

2) a Booking class that has attributes for customer name and seat number. ✅
Create accessor methods for both attributes. ✅''' 
        
class Play:
    def __init__(self, iD, name, seats, date):
        self.__iD = iD
        self.__name = name
        self.__seats = seats
        self.__date = date
        self.__status = True

    def get_name(self):
        return self.__name
        
    def get_seats(self):
        #self.seats = number
        return self.__seats 

    def get_status(self):
        return self.__status

    def seats_left(self):
        self.__remain = self.__seats - 1

    def get_seats_left(self):
        return self.__remain

    def set_status(self):
        self.__status = False

class Booking:
    def __init__(self, name, seat_num):
        self.__name = name
        self.__seat_num = seat_num

    def get_name(self):
        return self.__name
    
    def get_seat_num(self):
        return self.__seat_num

