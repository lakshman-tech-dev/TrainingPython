class MovieTicket:
    def __init__(self, booked_seats):
        self.booked_seats = booked_seats

    def is_booked(self, seat):
        return seat in self.booked_seats

    def total_booked(self):
        return len(self.booked_seats)

    def available_seats(self):
        available = []

        for seat in range(1, 21):
            if seat not in self.booked_seats:
                available.append(seat)

        return available


ticket = MovieTicket([1, 3, 5, 7, 10, 15])

print("Total Booked Seats:", ticket.total_booked())
print("Available Seats:", ticket.available_seats())
