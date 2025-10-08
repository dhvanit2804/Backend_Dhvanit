class Train:
    def __init__(self, name, seat, fare):
        self.name = name
        self.seat = seat
        self.fare = fare

    def getStatus(self):
        print(f"Train: {self.name} | Avilabale Seats : {self.seat}")

    def getFareInfo(self):
        print(f"Train : {self.name} | Ticket Fare : {self.fare}")

    def bookTicket(self):
        if self.seat > 0:
            print(f"Ticket Booked successfully on {self.name}. Seat Number : {self.seat}")
            self.seat -= 1
        else:
            print("Sorry, no seats avalible")

t1 = Train("Rajdhani Express", 3, 1500)

t1.getStatus()
t1.getFareInfo()
t1.bookTicket()
t1.getStatus()