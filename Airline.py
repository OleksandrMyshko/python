class Pilot:
    def __init__(self, salary):
        self.salary = salary


class Stewardess:
    def __init__(self, salary):
        self.salary = salary


class Ticket:
    def __init__(self, type, price):
        self.type = type
        self.price = price


class Plane:
    def __init__(self, type, number_of_tickets_A, ticket1, number_of_tickets_B, ticket2):
        self.type = type
        self.number_of_tickets_A = number_of_tickets_A
        self.number_of_tickets_B = number_of_tickets_B
        self.ticket1 = ticket1
        self.ticket2 = ticket2


class Flight:
    def __init__(self, number_of_pilots, pilot, number_of_stewardeses, stewardess, plane):
        self.number_of_pilots = number_of_pilots
        self.pilot = pilot
        self.number_of_stewardeses = number_of_stewardeses
        self.stewardess = stewardess
        self.plane = plane


class Airplane:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def total(self):
        sum = 0
        for flight in self.flights:
            sum += (flight.number_of_pilots * flight.pilot.salary + flight.number_of_stewardeses * flight.stewardess.salary
            + flight.plane.number_of_tickets_A * flight.plane.ticket1.price + flight.plane.number_of_tickets_B * flight.plane.ticket2.price)
        return sum

def main():
    pilot = Pilot(200)
    stewardess = Stewardess(100)
    ticket1 = Ticket('A', 10)
    ticket2 = Ticket('B', 20)
    plane1 = Plane('X', 10, ticket1, 20, ticket2)
    plane2 = Plane('Y', 20, ticket1, 40, ticket2)
    flight1 = Flight(2, pilot, 4, stewardess, plane1)
    flight2 = Flight(2, pilot, 6, stewardess, plane2)
    airplane = Airplane()
    airplane.add_flight(flight1)
    airplane.add_flight(flight2)

    print(airplane.total())

main()











