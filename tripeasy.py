destinations=[
{"name":"Goa","state":"Goa","type":"beach","season":("summer","winter"),"budget":15000,"days":4,"activities":["beaches","water sports","nightlife","food"]},
{"name":"Manali","state":"Himachal Pradesh","type":"mountains","season":("summer","winter"),"budget":18000,"days":5,"activities":["snow","trekking","sightseeing","camping"]},
{"name":"Jaipur","state":"Rajasthan","type":"heritage","season":("winter","summer"),"budget":10000,"days":3,"activities":["forts","shopping","food","sightseeing"]},
{"name":"Kerala","state":"Kerala","type":"nature","season":("winter","monsoon"),"budget":20000,"days":5,"activities":["backwaters","hills","beaches","boating"]},
{"name":"Rishikesh","state":"Uttarakhand","type":"adventure","season":("summer","winter"),"budget":12000,"days":3,"activities":["rafting","camping","trekking","bungee jumping"]},
{"name":"Udaipur","state":"Rajasthan","type":"heritage","season":("winter","summer"),"budget":11000,"days":3,"activities":["lakes","palaces","shopping","food"]},
{"name":"Darjeeling","state":"West Bengal","type":"mountains","season":("winter","summer"),"budget":16000,"days":4,"activities":["tea gardens","hills","sightseeing","trekking"]},
{"name":"Andaman","state":"Andaman and Nicobar","type":"beach","season":("winter","summer"),"budget":25000,"days":6,"activities":["scuba diving","beaches","boating","snorkeling"]}
]

def show_destinations():
    print("\nAvailable destinations:")
    for place in destinations:
        print(place["name"],"-",place["type"],"- Rs.",place["budget"],"-",place["days"],"days")

def get_budget():
    while True:
        try:
            budget=int(input("Enter your budget: "))
            if budget>0:
                return budget
            print("Budget should be greater than 0.")
        except:
            print("Enter a valid number.")

def get_season():
    seasons={"1":"summer","2":"winter","3":"monsoon"}

    while True:
        print("\nChoose season:")
        print("1. Summer")
        print("2. Winter")
        print("3. Monsoon")

        choice=input("Enter choice: ")

        if choice in seasons:
            return seasons[choice]

        print("Invalid choice.")

def get_type():
    types={"1":"beach","2":"mountains","3":"heritage","4":"nature","5":"adventure"}

    while True:
        print("\nChoose type of place:")
        print("1. Beach")
        print("2. Mountains")
        print("3. Heritage")
        print("4. Nature")
        print("5. Adventure")

        choice=input("Enter choice: ")

        if choice in types:
            return types[choice]

        print("Invalid choice.")

def find_trips():
    budget=get_budget()
    season=get_season()
    place_type=get_type()
    matches=[]

    for place in destinations:
        if place["budget"]<=budget and season in place["season"] and place["type"]==place_type:
            matches.append(place)

    if len(matches)==0:
        print("\nNo destination matched your choices.")
        return

    print("\nDestinations for you:")

    for place in matches:
        print("\nName:",place["name"])
        print("State:",place["state"])
        print("Budget: Rs.",place["budget"])
        print("Days:",place["days"])
        print("Activities:",", ".join(place["activities"]))

def search_destination():
    name=input("\nEnter destination name: ").lower()
    found=False

    for place in destinations:
        if name in place["name"].lower():
            print("\nName:",place["name"])
            print("State:",place["state"])
            print("Type:",place["type"])
            print("Budget: Rs.",place["budget"])
            print("Days:",place["days"])
            print("Activities:",", ".join(place["activities"]))
            found=True

    if not found:
        print("Destination not found.")

def show_activities():
    activities=set()

    for place in destinations:
        for activity in place["activities"]:
            activities.add(activity)

    print("\nActivities available:")

    for activity in sorted(activities):
        print(activity)

def plan_trip():
    show_destinations()
    name=input("\nEnter destination: ").lower()
    selected=None

    for place in destinations:
        if place["name"].lower()==name:
            selected=place
            break

    if selected is None:
        print("Destination not found.")
        return

    while True:
        try:
            days=int(input("How many days do you want to stay?"))

            if days>0:
                break

            print("Enter a positive number.")
        except:
            print("Enter a valid number.")

    daily_cost=selected["budget"]/selected["days"]
    total_cost=round(daily_cost*days)

    print("\nYour trip:")
    print("Destination:",selected["name"])
    print("State:",selected["state"])
    print("Days:",days)
    print("Estimated cost: Rs.",total_cost)
    print("Activities:",", ".join(selected["activities"]))

    if days>selected["days"]:
        print("You are planning a longer trip.")
    elif days<selected["days"]:
        print("You are planning a shorter trip.")
    else:
        print("This is the suggested trip duration.")

def compare_places():
    show_destinations()

    first=input("\nEnter first destination: ").lower()
    second=input("Enter second destination: ").lower()

    place1=None
    place2=None

    for place in destinations:
        if place["name"].lower()==first:
            place1=place
        if place["name"].lower()==second:
            place2=place

    if place1 is None or place2 is None:
        print("Destination not found.")
        return

    print("\n",place1["name"],"and",place2["name"])

    print("Budget:")
    print(place1["name"],": Rs.",place1["budget"])
    print(place2["name"],": Rs.",place2["budget"])

    print("Days:")
    print(place1["name"],":",place1["days"])
    print(place2["name"],":",place2["days"])

    print("Type:")
    print(place1["name"],":",place1["type"])
    print(place2["name"],":",place2["type"])

    activities1=set(place1["activities"])
    activities2=set(place2["activities"])
    common=activities1.intersection(activities2)

    if len(common)>0:
        print("Common activities:",", ".join(common))
    else:
        print("No common activities.")

def main():
    while True:
        print("\nTRIP PLANNER")
        print("1. View destinations")
        print("2. Find a trip")
        print("3. Search destination")
        print("4. See activities")
        print("5. Plan a trip")
        print("6. Compare destinations")
        print("7. Exit")

        choice=input("Enter your choice: ")

        if choice=="1":
            show_destinations()
        elif choice=="2":
            find_trips()
        elif choice=="3":
            search_destination()
        elif choice=="4":
            show_activities()
        elif choice=="5":
            plan_trip()
        elif choice=="6":
            compare_places()
        elif choice=="7":
            print("Thank you for using Trip Planner!")
            break
        else:
            print("Invalid choice.")

main()

