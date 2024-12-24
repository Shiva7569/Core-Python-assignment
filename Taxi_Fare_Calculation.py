def calculate_fare(trip):
    price=list(map(lambda x:50+x*10,trip))
    return price
trip=[]
number_of_trips=int(input("Enter the number of trips : "))
for i in range(number_of_trips):
    trip.append(int(input(f"Enter the distance of trip {i+1} : ")))
costs=calculate_fare(trip)
for i in range(len(costs)):
    print(f"Trip {i+1} : ${costs[i]}")
print(f"Total fare : ${sum(costs)}")