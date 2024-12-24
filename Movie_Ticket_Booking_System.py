def seat_booking(total_seats,booked_seats, seat):
    if seat not in booked_seats:
        booked_seats.append(seat)
        booked_seats.sort()
    else:
        print(f"Seat {seat} is already booked.")

def seat_cancellation(booked_seats, seat):
    if seat in booked_seats:
        booked_seats.remove(seat)
    else:
        print(f"Seat {seat} was not booked.")

def available_seats(total_seats, booked_seats):
    return [i for i in range(1, total_seats + 1) if i not in booked_seats]
total_seats = int(input("Enter the total number of seats: "))
booked = input("Enter the booked seats numbers separated with comma: ")
booked_seats = list(map(int, booked.split(",")))
while True:
    operation = input("Do you want to book or cancel a seat? (book/cancel/exit): ").lower()
    if operation == 'exit':
        break
    seat = int(input("Enter seat number: "))
    if operation == 'book':
        seat_booking(total_seats,booked_seats, seat)
    elif operation == 'cancel':
        seat_cancellation(booked_seats, seat)
    else:
        print("Invalid action.")
print("Available Seats:", available_seats(total_seats, booked_seats))
