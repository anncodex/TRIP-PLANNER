destinations=[{"name":"Goa","state":"Goa","type":"beach","season":("summer","winter"),"budget":15000,"days":4,"activities":["beaches","water sports","nightlife","food"]},
{"name":"Manali","state":"Himachal Pradesh","type":"mountains","season":("summer","winter"),"budget":18000,"days":5,"activities":["snow","trekking","mountains","camping"]},
{"name":"Jaipur","state":"Rajasthan","type":"historical","season":("winter","monsoon"),"budget":12000,"days":3,"activities":["forts","palaces","shopping","food"]},
{"name":"Rishikesh","state":"Uttarakhand","type":"adventure","season":("summer","winter"),"budget":10000,"days":3,"activities":["rafting","camping","trekking","yoga"]},
{"name":"Udaipur","state":"Rajasthan","type":"romantic","season":("winter","monsoon"),"budget":14000,"days":3,"activities":["lakes","palaces","boating","food"]},
{"name":"Kerala","state":"Kerala","type":"nature","season":("winter","monsoon"),"budget":20000,"days":5,"activities":["backwaters","nature","beaches","food"]},
{"name":"Agra","state":"Uttar Pradesh","type":"historical","season":("winter","monsoon"),"budget":8000,"days":2,"activities":["Taj Mahal","forts","history","food"]},
{"name":"Ladakh","state":"Ladakh","type":"adventure","season":("summer",),"budget":30000,"days":7,"activities":["biking","mountains","lakes","trekking"]},
{"name":"Andaman","state":"Andaman and Nicobar","type":"beach","season":("winter","summer"),"budget":28000,"days":6,"activities":["scuba diving","beaches","snorkeling","islands"]},
{"name":"Shimla","state":"Himachal Pradesh","type":"mountains","season":("summer","winter"),"budget":13000,"days":4,"activities":["snow","mountains","shopping","trekking"]},
{"name":"Mysore","state":"Karnataka","type":"historical","season":("winter","monsoon"),"budget":11000,"days":3,"activities":["palaces","temples","food","shopping"]},
{"name":"Munnar","state":"Kerala","type":"nature","season":("winter","monsoon"),"budget":16000,"days":4,"activities":["tea gardens","hills","nature","trekking"]}]

types={"beach","mountains","historical","adventure","romantic","nature"}
seasons={"summer","winter","monsoon"}

print("="*55)
print("                 TRIP PLANNER")
print("="*55)
print("Find a destination according to your budget,")
print("season and type of place you want to visit.")

while True:
    try:
        budget=float(input("\nEnter your total budget: ₹"))
        if budget>0:
            break
        else:
            print("Budget should be greater than 0.")
    except:
        print("Please enter a valid amount.")

while True:
    print("\nAvailable seasons:")
    for season in seasons:
        print("-",season.title())

    season=input("Enter your preferred season: ").lower().strip()

    if season in seasons:
        break
    else:
        print("Invalid season. Try again.")

while True:
    print("\nAvailable types of places:")
    for place in types:
        print("-",place.title())

    place=input("What type of place do you want to visit? ").lower().strip()

    if place in types:
        break
    else:
        print("Invalid type. Try again.")

while True:
    try:
        people=int(input("\nHow many people are travelling? "))

        if people>0:
            break
        else:
            print("Number of people must be greater than 0.")

    except:
        print("Enter a valid number.")

per_person=budget/people

print("\n"+"="*55)
print("                  TRIP DETAILS")
print("="*55)
print("Total budget: ₹",format(budget,",.0f"))
print("Budget per person: ₹",format(per_person,",.0f"))
print("Season:",season.title())
print("Place type:",place.title())
print("Number of people:",people)

if people==1:
    print("Trip style: Solo trip")
elif people==2:
    print("Trip style: Couple/Friends")
elif people<=5:
    print("Trip style: Small group")
else:
    print("Trip style: Large group")

if per_person<10000:
    print("Budget category: Economy")
elif per_person<20000:
    print("Budget category: Moderate")
elif per_person<30000:
    print("Budget category: Premium")
else:
    print("Budget category: Luxury")

matches=[]

for destination in destinations:
    if season in destination["season"]:
        if place==destination["type"]:
            if per_person>=destination["budget"]:
                matches.append(destination)

print("\n"+"="*55)

if len(matches)>0:
    print("       DESTINATIONS MATCHING YOUR REQUIREMENTS")
    print("="*55)

    for i in range(len(matches)):
        destination=matches[i]

        print("\nRecommendation",i+1)
        print("-"*45)
        print("Destination:",destination["name"])
        print("State:",destination["state"])
        print("Type:",destination["type"].title())
        print("Best season:",", ".join(destination["season"]))
        print("Suggested days:",destination["days"])

        total_cost=destination["budget"]*people

        if people>=6:
            total_cost=total_cost*0.85
        elif people>=4:
            total_cost=total_cost*0.90
        elif people>=2:
            total_cost=total_cost*0.95

        print("Estimated cost: ₹",format(total_cost,",.0f"))

        print("Activities:")

        for activity in destination["activities"]:
            print("-",activity.title())

else:
    print("       NO EXACT MATCH FOUND")
    print("="*55)
    print("There are no destinations matching all")
    print("your requirements.")

    relaxed=[]

    for destination in destinations:
        if season in destination["season"]:
            if place==destination["type"]:
                if per_person>=destination["budget"]*0.8:
                    relaxed.append(destination)

    if len(relaxed)>0:
        print("\nSome destinations are slightly above")
        print("your budget:")

        for i in range(len(relaxed)):
            destination=relaxed[i]

            print("\nRecommendation",i+1)
            print("-"*45)
            print("Destination:",destination["name"])
            print("State:",destination["state"])
            print("Type:",destination["type"].title())
            print("Budget per person: ₹",destination["budget"])
            print("Suggested days:",destination["days"])

            print("Activities:")

            for activity in destination["activities"]:
                print("-",activity.title())

    else:
        print("\nNo suitable destinations were found.")

if len(matches)>0:
    print("\n"+"="*55)
    print("             DESTINATION SELECTION")
    print("="*55)

    for i in range(len(matches)):
        print(i+1,"-",matches[i]["name"])

    while True:
        try:
            choice=int(input("\nChoose a destination number: "))

            if 1<=choice<=len(matches):
                selected=matches[choice-1]
                break
            else:
                print("Invalid choice.")

        except:
            print("Enter a valid number.")

    print("\nYou selected:",selected["name"])
    print("Here are some details about your trip:")

    print("\nLocation:",selected["state"])
    print("Trip duration:",selected["days"],"days")
    print("Type:",selected["type"].title())
    print("Activities:")

    for activity in selected["activities"]:
        print("-",activity.title())

    final_cost=selected["budget"]*people

    if people>=6:
        discount=15
        final_cost=final_cost*0.85
    elif people>=4:
        discount=10
        final_cost=final_cost*0.90
    elif people>=2:
        discount=5
        final_cost=final_cost*0.95
    else:
        discount=0

    print("\nOriginal estimated cost: ₹",format(selected["budget"]*people,",.0f"))
    print("Group discount:",discount,"%")
    print("Final estimated cost: ₹",format(final_cost,",.0f"))

    activities=set(selected["activities"])

    print("\nAvailable activities:")
    for activity in activities:
        print("-",activity.title())

    print("\nTrip planning tips:")

    if selected["type"]=="beach":
        print("Carry sunscreen, sunglasses and comfortable clothes.")
    elif selected["type"]=="mountains":
        print("Carry warm clothes and comfortable shoes.")
    elif selected["type"]=="historical":
        print("Carry comfortable footwear for sightseeing.")
    elif selected["type"]=="adventure":
        print("Carry comfortable clothes and necessary safety items.")
    elif selected["type"]=="nature":
        print("Carry comfortable shoes and a light jacket.")
    elif selected["type"]=="romantic":
        print("Plan your sightseeing and stay in advance.")

print("\n"+"="*55)
print("                 TRIP PLANNER END")
print("="*55)
print("Have a safe and enjoyable trip!")


