"""
Hall management System
Shakib Hasan Readoy
"""
class Star_Cinema:
    hall_list=[]
    def entry_hall(self,value):
        pass


class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no
        self.seats= dict()
        self.show_list=[]
        super().__init__()

    def entry_show(self,id,movie_name,time):
        self.id=id
        self.move_name=movie_name
        self.time=time

        self.store=(self.id,self.move_name,self.time)
        self.show_list.append(self.store)
        

        #making 2 d list wiht false value
        self.list=[]
        for i in range(self.__rows):
            c=[]
            for j in range(self.__cols):
                c.append(0)
            self.list.append(c)


  
        
        #storing id and list to the seat dictionary
        self.seats[self.id]=self.list
       


    def book_seats(self, name,phone,c_id,seat):
        self.name=name
        self.phone=phone
        self.c_id=c_id
        self.seat=seat

        c=0
        for i in self.show_list: #accessing the key
            if (i[0]==c_id): # matching key
                c+=1
                print("\n**** TICKET BOOKED SUCCESSFULLY! \n")
                print("_________________________________________________________________________________________ \n")
                print(f"Name: {name}\nPhone Number: {phone}\n\n")
                print(f"Movie Name: {i[1]}\t\t Movie Time: {i[2]} \nHall: {self.__hall_no}  \n\n")
                # self.seats[i[0]][2][3]=1
                for (a,b) in seat: #accessing seat
                    if(a>self.__rows or b>self.__cols):
                        print("you have inserted a wrong seat")
                        break
                    elif( self.seats[i[0]][a][b]==1):
                        print("this seat is already booked")
                        break
                    else:
                     self.seats[i[0]][a][b]=1 # updating seat status. here seats[i[0]] indicating the value of the mathch id. then we are accessing row col postition depending on ab from seats dictionary
        print("_________________________________________________________________________________________ \n")
        if(c==0):
            print("You have entered a wrong id")


    def view_show_list(self):
        for i in self.show_list:
            print(f"Show ID: {i[0]}\t\t Movie Name: {i[1]}\t\t Time: {i[2]} \n")


    def view_available_seats(self,show_id):
        c=0
        for i in self.show_list: #accessing the key
            if (i[0]==show_id): # matching key
                c+=1
                print(f"Movie Name: {i[1]}\t\t Time: {i[2]} \n\nX for already booked seats \n")
                print("_________________________________________________________________________________________ \n")
                for index,j in enumerate(self.seats[i[0]]): # accessing index and value of row 
                    for k in range(0,len(j)): # accessing column
                        if(j[k]==1):  # checking that seat is booked or not
                            print("X",end='\t\t')
                        else:
                            print(f"{chr(index+65)}{k}",end='\t\t')
                    
                    print("\n")
                print("_________________________________________________________________________________________ \n")
        if(c==0):
            print("You have entered a wrong id\n")




CinePlex = Hall(5,5,20221)
CinePlex.hall_list.append(CinePlex._Hall__cols)
CinePlex.hall_list.append(CinePlex._Hall__rows)
CinePlex.hall_list.append(CinePlex._Hall__hall_no)
CinePlex.entry_show("abc1","spiderman1","7 pm, 17 October, 2022")
CinePlex.entry_show("abc2","Iron Man","9 pm, 27 October, 2022")

def convert_seat(ticket_no):
    ticket_list=[]
    for i in range(0,ticket_no):
        seat = input("Enter seat Number :")
        if(seat[0]>="A" and seat[0]<="Z"):
            for j in seat:
            
                if(j>="A" and j<="Z"):
                    r = ord(j)-65
                else:
                    c = ord(j)-48
            ticket_list.append((r,c))
        else:
            print("unvalid seat number")
    
    return ticket_list


print("1. view all shows today \n")
print("2. View available seats \n")
print("3. Book ticket \n")
print("4. exist \n")
option = int(input("enter option: "))
while(option!=4):
    if(option==1):
        print("_________________________________________________________________________________________ \n")
        CinePlex.view_show_list()
        print("_________________________________________________________________________________________ \n")

    elif(option==2):
        show_id = input("enter show Id: ")
        print("\n")
        CinePlex.view_available_seats(show_id)

    elif(option==3):
        name= input("Enter customer name: ")
        phone = input("Enter customer phone: ")
        Id = input("Enter show ID: ")
        no_of_ticket = int(input("Enter number of ticket: "))
        ticket_list = []
        ticket_list=convert_seat(no_of_ticket)   
        CinePlex.book_seats(name,phone,Id,ticket_list)

    

    print("1. view all shows today \n")
    print("2. View available seats \n")
    print("3. Book ticket \n")
    print("4. exist \n")
    option = int(input("enter option: "))


# name= input("Enter customer name: ")
# phone = input("Enter customer phone: ")
# Id = input("Enter show ID: ")
# no_of_ticket = int(input("Enter number of ticket: "))
# ticket_list = []
# ticket_list=convert_seat(no_of_ticket)   
# CinePlex.book_seats(name,phone,Id,ticket_list)
# CinePlex.view_available_seats(Id)


# CinePlex.book_seats("Shakib","01711","abc1",[(1,2),(2,3)])
# CinePlex.book_seats("Hasan",'0233',"abc1",[(1,2)])

# CinePlex.view_available_seats("abc1")

# CinePlex.view_show_list()

# print(CinePlex.seats)
# for i in CinePlex.seats:
#     # print(CinePlex.seats[i])
#     for j in CinePlex.seats[i]:
#         print(j)

# print(CinePlex.seats)

# print(CinePlex.show_list)

# for (a,b) in CinePlex.seats:
#     print(a,b)


# print(CinePlex.seats)


