#---------------------TRIP PLANNER PROJECT-----------------------

from datetime import datetime
from array import array
import json

destinations = [

    {
        "name": "Manali",
        "state": "Himachal Pradesh",
        "region": "North",
        "types": ("Adventure", "Relaxation"),
        "seasons": ("Winter", "Spring"),
        "budget": 12000,
        "days": 5,
        "rating": 4.7,
        "places": ["Solang Valley", "Mall Road", "Rohtang Pass"],
        "food": ["Momos", "Siddu", "Thukpa"],
        "packing": ["Jacket", "Warm clothes", "Comfortable shoes"]
    },

    {
        "name": "Shimla",
        "state": "Himachal Pradesh",
        "region": "North",
        "types": ("Relaxation", "Culture"),
        "seasons": ("Winter", "Spring"),
        "budget": 10000,
        "days": 4,
        "rating": 4.5,
        "places": ["Mall Road", "Kufri", "Jakhoo Temple"],
        "food": ["Momos", "Siddu", "Chana"],
        "packing": ["Jacket", "Warm clothes", "Shoes"]
    },

    {
        "name": "Rishikesh",
        "state": "Uttarakhand",
        "region": "North",
        "types": ("Adventure", "Relaxation"),
        "seasons": ("Spring", "Summer"),
        "budget": 8000,
        "days": 3,
        "rating": 4.6,
        "places": ["River Rafting", "Laxman Jhula", "Beatles Ashram"],
        "food": ["Aloo Puri", "Pakora", "Momos"],
        "packing": ["Sports shoes", "Light clothes", "Water bottle"]
    },

    {
        "name": "Nainital",
        "state": "Uttarakhand",
        "region": "North",
        "types": ("Relaxation", "Adventure"),
        "seasons": ("Summer", "Spring"),
        "budget": 9000,
        "days": 4,
        "rating": 4.4,
        "places": ["Naini Lake", "Mall Road", "Snow View"],
        "food": ["Momos", "Aloo Ke Gutke", "Bal Mithai"],
        "packing": ["Light jacket", "Shoes", "Sunglasses"]
    },

    {
        "name": "Jaipur",
        "state": "Rajasthan",
        "region": "West",
        "types": ("Culture", "City"),
        "seasons": ("Winter", "Spring"),
        "budget": 9000,
        "days": 4,
        "rating": 4.6,
        "places": ["Amber Fort", "Hawa Mahal", "City Palace"],
        "food": ["Dal Baati", "Pyaaz Kachori", "Ghewar"],
        "packing": ["Comfortable shoes", "Sunglasses", "Light clothes"]
    },

    {
        "name": "Udaipur",
        "state": "Rajasthan",
        "region": "West",
        "types": ("Relaxation", "Culture"),
        "seasons": ("Winter", "Spring"),
        "budget": 10000,
        "days": 4,
        "rating": 4.7,
        "places": ["Lake Pichola", "City Palace", "Jag Mandir"],
        "food": ["Dal Baati", "Gatte", "Kachori"],
        "packing": ["Comfortable shoes", "Sunglasses", "Light clothes"]
    },

    {
        "name": "Goa",
        "state": "Goa",
        "region": "West",
        "types": ("Beach", "Relaxation"),
        "seasons": ("Winter", "Spring"),
        "budget": 13000,
        "days": 5,
        "rating": 4.8,
        "places": ["Baga Beach", "Fort Aguada", "Anjuna Beach"],
        "food": ["Goan Curry", "Bebinca", "Seafood"],
        "packing": ["Beach clothes", "Sunscreen", "Sunglasses"]
    },

    {
        "name": "Mumbai",
        "state": "Maharashtra",
        "region": "West",
        "types": ("City", "Culture"),
        "seasons": ("Winter", "Spring"),
        "budget": 8000,
        "days": 3,
        "rating": 4.4,
        "places": ["Marine Drive", "Gateway of India", "Elephanta Caves"],
        "food": ["Vada Pav", "Pav Bhaji", "Misal Pav"],
        "packing": ["Comfortable shoes", "Light clothes", "Umbrella"]
    },

    {
        "name": "Lonavala",
        "state": "Maharashtra",
        "region": "West",
        "types": ("Relaxation", "Adventure"),
        "seasons": ("Monsoon", "Winter"),
        "budget": 6000,
        "days": 2,
        "rating": 4.5,
        "places": ["Tiger Point", "Bhushi Dam", "Rajmachi"],
        "food": ["Vada Pav", "Corn", "Chikki"],
        "packing": ["Raincoat", "Comfortable shoes", "Umbrella"]
    },

    {
        "name": "Agra",
        "state": "Uttar Pradesh",
        "region": "North",
        "types": ("Historical", "Culture"),
        "seasons": ("Winter", "Spring"),
        "budget": 6000,
        "days": 2,
        "rating": 4.3,
        "places": ["Taj Mahal", "Agra Fort", "Mehtab Bagh"],
        "food": ["Petha", "Mughlai Food", "Bedai"],
        "packing": ["Comfortable shoes", "Sunglasses", "Water bottle"]
    },

    {
        "name": "Varanasi",
        "state": "Uttar Pradesh",
        "region": "North",
        "types": ("Culture", "Historical"),
        "seasons": ("Winter", "Spring"),
        "budget": 7000,
        "days": 3,
        "rating": 4.5,
        "places": ["Ganga Ghats", "Sarnath", "Kashi Vishwanath"],
        "food": ["Kachori", "Banarasi Chaat", "Lassi"],
        "packing": ["Comfortable shoes", "Light clothes", "Water bottle"]
    },

    {
        "name": "Kolkata",
        "state": "West Bengal",
        "region": "East",
        "types": ("Culture", "City"),
        "seasons": ("Winter", "Spring"),
        "budget": 8000,
        "days": 3,
        "rating": 4.4,
        "places": ["Victoria Memorial", "Howrah Bridge", "Indian Museum"],
        "food": ["Rosogolla", "Kathi Roll", "Macher Jhol"],
        "packing": ["Comfortable shoes", "Light clothes", "Umbrella"]
    },

    {
        "name": "Darjeeling",
        "state": "West Bengal",
        "region": "East",
        "types": ("Relaxation", "Adventure"),
        "seasons": ("Spring", "Summer"),
        "budget": 10000,
        "days": 4,
        "rating": 4.6,
        "places": ["Tiger Hill", "Tea Gardens", "Batasia Loop"],
        "food": ["Momos", "Thukpa", "Darjeeling Tea"],
        "packing": ["Jacket", "Comfortable shoes", "Umbrella"]
    },

    {
        "name": "Gangtok",
        "state": "Sikkim",
        "region": "East",
        "types": ("Adventure", "Relaxation"),
        "seasons": ("Spring", "Summer"),
        "budget": 11000,
        "days": 5,
        "rating": 4.7,
        "places": ["Tsomgo Lake", "Nathula Pass", "MG Marg"],
        "food": ["Momos", "Thukpa", "Phagshapa"],
        "packing": ["Jacket", "Comfortable shoes", "Sunglasses"]
    },

    {
        "name": "Shillong",
        "state": "Meghalaya",
        "region": "East",
        "types": ("Adventure", "Relaxation"),
        "seasons": ("Summer", "Spring"),
        "budget": 11000,
        "days": 5,
        "rating": 4.6,
        "places": ["Umiam Lake", "Elephant Falls", "Shillong Peak"],
        "food": ["Jadoh", "Momos", "Tungrymbai"],
        "packing": ["Raincoat", "Comfortable shoes", "Light jacket"]
    },

    {
        "name": "Bengaluru",
        "state": "Karnataka",
        "region": "South",
        "types": ("City", "Food"),
        "seasons": ("Winter", "Spring"),
        "budget": 8000,
        "days": 3,
        "rating": 4.4,
        "places": ["Lalbagh", "Cubbon Park", "Bangalore Palace"],
        "food": ["Dosa", "Idli", "Bisi Bele Bath"],
        "packing": ["Comfortable shoes", "Light clothes", "Water bottle"]
    },

    {
        "name": "Mysore",
        "state": "Karnataka",
        "region": "South",
        "types": ("Culture", "Historical"),
        "seasons": ("Winter", "Spring"),
        "budget": 7000,
        "days": 3,
        "rating": 4.5,
        "places": ["Mysore Palace", "Chamundi Hills", "Brindavan Gardens"],
        "food": ["Mysore Pak", "Dosa", "Idli"],
        "packing": ["Comfortable shoes", "Light clothes", "Sunglasses"]
    },

    {
        "name": "Ooty",
        "state": "Tamil Nadu",
        "region": "South",
        "types": ("Relaxation", "Nature"),
        "seasons": ("Summer", "Spring"),
        "budget": 9000,
        "days": 4,
        "rating": 4.5,
        "places": ["Ooty Lake", "Botanical Garden", "Doddabetta"],
        "food": ["Chocolate", "Dosa", "Biryani"],
        "packing": ["Light jacket", "Comfortable shoes", "Sunglasses"]
    },

    {
        "name": "Munnar",
        "state": "Kerala",
        "region": "South",
        "types": ("Relaxation", "Nature"),
        "seasons": ("Winter", "Spring"),
        "budget": 10000,
        "days": 4,
        "rating": 4.7,
        "places": ["Tea Gardens", "Eravikulam", "Mattupetty Dam"],
        "food": ["Appam", "Puttu", "Kerala Curry"],
        "packing": ["Light jacket", "Comfortable shoes", "Sunscreen"]
    },

    {
        "name": "Pondicherry",
        "state": "Tamil Nadu",
        "region": "South",
        "types": ("Beach", "Relaxation"),
        "seasons": ("Winter", "Spring"),
        "budget": 9000,
        "days": 3,
        "rating": 4.5,
        "places": ["Promenade Beach", "Auroville", "French Quarter"],
        "food": ["Dosa", "Crepes", "Seafood"],
        "packing": ["Beach clothes", "Sunscreen", "Sunglasses"]
    },

    {
        "name": "Hyderabad",
        "state": "Telangana",
        "region": "South",
        "types": ("City", "Food", "Culture"),
        "seasons": ("Winter", "Spring"),
        "budget": 8000,
        "days": 3,
        "rating": 4.5,
        "places": ["Charminar", "Golconda Fort", "Hussain Sagar"],
        "food": ["Biryani", "Haleem", "Qubani Ka Meetha"],
        "packing": ["Comfortable shoes", "Light clothes", "Water bottle"]
    },

    {
        "name": "Bhopal",
        "state": "Madhya Pradesh",
        "region": "Central",
        "types": ("City", "Culture"),
        "seasons": ("Winter", "Spring"),
        "budget": 5000,
        "days": 2,
        "rating": 4.3,
        "places": ["Upper Lake", "Van Vihar", "Sanchi"],
        "food": ["Poha", "Jalebi", "Bhopali Gosht"],
        "packing": ["Comfortable shoes", "Light clothes", "Water bottle"]
    },

    {
        "name": "Indore",
        "state": "Madhya Pradesh",
        "region": "Central",
        "types": ("Food", "City"),
        "seasons": ("Winter", "Spring"),
        "budget": 5000,
        "days": 2,
        "rating": 4.6,
        "places": ["Rajwada", "Sarafa Bazaar", "Lal Bagh"],
        "food": ["Poha", "Jalebi", "Bhutte Ka Kees"],
        "packing": ["Comfortable shoes", "Light clothes", "Water bottle"]
    },

    {
        "name": "Pachmarhi",
        "state": "Madhya Pradesh",
        "region": "Central",
        "types": ("Nature", "Relaxation"),
        "seasons": ("Summer", "Monsoon"),
        "budget": 6000,
        "days": 3,
        "rating": 4.4,
        "places": ["Bee Falls", "Dhupgarh", "Jatashankar"],
        "food": ["Poha", "Dal Bafla", "Jalebi"],
        "packing": ["Raincoat", "Comfortable shoes", "Light clothes"]
    },

    {
        "name": "Andaman",
        "state": "Andaman and Nicobar",
        "region": "Islands",
        "types": ("Beach", "Adventure"),
        "seasons": ("Winter", "Spring"),
        "budget": 18000,
        "days": 6,
        "rating": 4.8,
        "places": ["Radhanagar Beach", "Cellular Jail", "Elephant Beach"],
        "food": ["Seafood", "Fish Fry", "Coconut Curry"],
        "packing": ["Beach clothes", "Sunscreen", "Sunglasses"]
    }
]



favourites = []
trip_history = []



budget_array = array("i", [d["budget"] for d in destinations])



def save_data():
    data = {
        "favourites": favourites,
        "trip_history": trip_history
    }

    with open("smarttrip_data.json", "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    global favourites, trip_history

    try:
        with open("smarttrip_data.json", "r") as file:
            data = json.load(file)

            favourites = data.get("favourites", [])
            trip_history = data.get("trip_history", [])

    except FileNotFoundError:
        favourites = []
        trip_history = []



def get_positive_number(message):

    while True:

        try:
            number = int(input(message))

            if number > 0:
                return number

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


def get_budget():

    while True:

        try:
            budget = int(input("Enter your total budget (₹): "))

            if budget > 0:
                return budget

            print("Budget must be greater than 0.")

        except ValueError:
            print("Please enter a valid amount.")


def get_date():

    while True:

        date_text = input(
            "When do you want to travel? (DD-MM-YYYY): "
        )

        try:

            date = datetime.strptime(
                date_text,
                "%d-%m-%Y"
            )

            if date.date() < datetime.now().date():

                print("Please enter a future date.")

            else:
                return date

        except ValueError:

            print("Please use DD-MM-YYYY format.")



def get_season(date):

    month = date.month

    if month in [12, 1, 2]:
        return "Winter"

    elif month in [3, 4, 5]:
        return "Spring"

    elif month in [6, 7, 8]:
        return "Monsoon"

    else:
        return "Autumn"



def choose_trip_type():

    print("\nWhat kind of trip would you like?\n")

    trip_types = [
        "Adventure",
        "Relaxation",
        "Culture",
        "Beach",
        "City",
        "Wildlife",
        "Food",
        "Nature",
        "Any"
    ]

    for i in range(len(trip_types)):
        print(f"{i + 1}. {trip_types[i]}")

    while True:

        try:

            choice = int(
                input("\nEnter your choice (1-9): ")
            )

            if 1 <= choice <= len(trip_types):

                return trip_types[choice - 1]

            print("Please choose between 1 and 9.")

        except ValueError:

            print("Please enter a number.")



def choose_region():

    print("\nWhich region would you like to explore?\n")

    regions = [
        "North",
        "South",
        "East",
        "West",
        "Central",
        "Islands",
        "Any"
    ]

    for i in range(len(regions)):
        print(f"{i + 1}. {regions[i]}")

    while True:

        try:

            choice = int(
                input("\nEnter your choice (1-7): ")
            )

            if 1 <= choice <= len(regions):

                return regions[choice - 1]

            print("Please choose between 1 and 7.")

        except ValueError:

            print("Please enter a number.")



def recommend_destinations(
        budget,
        days,
        season,
        trip_type,
        region):

    recommendations = []

    for destination in destinations:

        if region != "Any":

            if destination["region"] != region:
                continue

        score = 0

        
        if destination["budget"] <= budget:
            score += 4

        elif destination["budget"] <= budget * 1.2:
            score += 2

        
        if destination["days"] <= days:
            score += 2

        
        if season in destination["seasons"]:
            score += 3

        
        if trip_type == "Any":
            score += 2

        elif trip_type in destination["types"]:
            score += 4

        recommendations.append(
            (score, destination)
        )

    
    recommendations.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return recommendations[:5]




def show_recommendations(recommendations):

    print("\n" + "=" * 60)
    print("              RECOMMENDED DESTINATIONS")
    print("=" * 60)

    for i, item in enumerate(
            recommendations, 1):

        score, destination = item

        print(
            f"{i}. {destination['name']} "
            f"| ₹{destination['budget']} "
            f"| {destination['days']} days "
            f"| ⭐ {destination['rating']}"
        )



def show_destination(destination):

    print("\n" + "=" * 60)
    print(
        f"                  {destination['name'].upper()}"
    )
    print("=" * 60)

    print(
        f"State: {destination['state']}"
    )

    print(
        f"Region: {destination['region']}"
    )

    print(
        f"Best Seasons: "
        f"{', '.join(destination['seasons'])}"
    )

    print(
        f"Trip Types: "
        f"{', '.join(destination['types'])}"
    )

    print(
        f"Estimated Budget: ₹{destination['budget']}"
    )

    print(
        f"Recommended Days: {destination['days']}"
    )

    print(
        f"Rating: ⭐ {destination['rating']}"
    )

    print("\nPlaces to Visit:")

    for place in destination["places"]:
        print(" •", place)

    print("\nLocal Food:")

    for food in destination["food"]:
        print(" •", food)



def budget_breakdown(destination, people):

    total = destination["budget"] * people

    transport = int(total * 0.25)
    hotel = int(total * 0.30)
    food = int(total * 0.20)
    activities = int(total * 0.15)
    emergency = total - (
        transport +
        hotel +
        food +
        activities
    )

    print("\n" + "=" * 60)
    print("                 BUDGET BREAKDOWN")
    print("=" * 60)

    print(f"Total Estimated Budget : ₹{total}")
    print(f"Transport              : ₹{transport}")
    print(f"Hotel                  : ₹{hotel}")
    print(f"Food                   : ₹{food}")
    print(f"Activities             : ₹{activities}")
    print(f"Emergency              : ₹{emergency}")




def create_itinerary(destination):

    print("\n" + "=" * 60)
    print("                    ITINERARY")
    print("=" * 60)

    places = destination["places"]

    for day in range(1, destination["days"] + 1):

        place = places[
            (day - 1) % len(places)
        ]

        print(f"\nDay {day}")

        print(
            f"Morning   → Visit {place}"
        )

        print(
            "Afternoon → Explore nearby attractions"
        )

        print(
            "Evening   → Local food and relaxation"
        )




def packing_suggestions(destination):

    print("\n" + "=" * 60)
    print("                PACKING SUGGESTIONS")
    print("=" * 60)

    for item in destination["packing"]:

        print(" ✓", item)

    print(" ✓ Phone charger")
    print(" ✓ ID proof")
    print(" ✓ Basic medicines")
    print(" ✓ Water bottle")




def add_favourite(destination):

    name = destination["name"]

    if name not in favourites:

        favourites.append(name)

        save_data()

        print(
            f"\n✓ {name} added to favourites!"
        )

    else:

        print(
            "\nThis destination is already "
            "in your favourites."
        )


def show_favourites():

    print("\n" + "=" * 60)
    print("                  FAVOURITES")
    print("=" * 60)

    if not favourites:

        print("No favourite destinations yet.")

        return

    for i, place in enumerate(
            favourites, 1):

        print(f"{i}. {place}")



def search_destination():

    print("\n" + "=" * 60)
    print("                SEARCH DESTINATION")
    print("=" * 60)

    search = input(
        "Enter destination name, state, region or type: "
    ).lower()

    found = []

    for destination in destinations:

        text = (
            destination["name"] + " " +
            destination["state"] + " " +
            destination["region"] + " " +
            " ".join(destination["types"])
        ).lower()

        if search in text:

            found.append(destination)

    if not found:

        print("\nNo matching destination found.")

        return

    

    found.sort(
        key=lambda x: x["rating"],
        reverse=True
    )

    print("\nSearch Results:\n")

    for i, destination in enumerate(
            found, 1):

        print(
            f"{i}. {destination['name']} "
            f"| ₹{destination['budget']} "
            f"| ⭐ {destination['rating']}"
        )




def show_regions():

    print("\n" + "=" * 60)
    print("                 AVAILABLE REGIONS")
    print("=" * 60)

    regions = set()

    for destination in destinations:

        regions.add(
            destination["region"]
        )

    for region in sorted(regions):

        print("•", region)



def destination_statistics():

    print("\n" + "=" * 60)
    print("              DESTINATION STATISTICS")
    print("=" * 60)

    print(
        f"Total Destinations: {len(destinations)}"
    )

    cheapest = min(
        destinations,
        key=lambda x: x["budget"]
    )

    highest = max(
        destinations,
        key=lambda x: x["budget"]
    )

    highest_rating = max(
        destinations,
        key=lambda x: x["rating"]
    )

    average_budget = sum(
        budget_array
    ) // len(budget_array)

    print(
        f"Cheapest Destination: "
        f"{cheapest['name']} "
        f"(₹{cheapest['budget']})"
    )

    print(
        f"Highest Budget Destination: "
        f"{highest['name']} "
        f"(₹{highest['budget']})"
    )

    print(
        f"Highest Rated Destination: "
        f"{highest_rating['name']} "
        f"(⭐{highest_rating['rating']})"
    )

    print(
        f"Average Destination Budget: "
        f"₹{average_budget}"
    )



def sort_destinations():

    print("\n" + "=" * 60)
    print("                 SORT DESTINATIONS")
    print("=" * 60)

    print("1. Lowest Budget")
    print("2. Highest Budget")
    print("3. Highest Rating")
    print("4. Shortest Trip")

    while True:

        try:

            choice = int(
                input("\nEnter your choice (1-4): ")
            )

            sorted_list = destinations.copy()

            if choice == 1:

                sorted_list.sort(
                    key=lambda x: x["budget"]
                )

            elif choice == 2:

                sorted_list.sort(
                    key=lambda x: x["budget"],
                    reverse=True
                )

            elif choice == 3:

                sorted_list.sort(
                    key=lambda x: x["rating"],
                    reverse=True
                )

            elif choice == 4:

                sorted_list.sort(
                    key=lambda x: x["days"]
                )

            else:

                print("Choose between 1 and 4.")
                continue

            print("\nResults:\n")

            for i, destination in enumerate(
                    sorted_list[:10], 1):

                print(
                    f"{i}. {destination['name']} "
                    f"| ₹{destination['budget']} "
                    f"| {destination['days']} days "
                    f"| ⭐{destination['rating']}"
                )

            break

        except ValueError:

            print("Please enter a number.")




def save_trip(destination, date, people):

    trip = {
        "destination": destination["name"],
        "date": date.strftime("%d-%m-%Y"),
        "people": people,
        "budget": destination["budget"] * people
    }

    trip_history.append(trip)

    save_data()


def show_history():

    print("\n" + "=" * 60)
    print("                    TRIP HISTORY")
    print("=" * 60)

    if not trip_history:

        print("No trips planned yet.")

        return

    for i, trip in enumerate(
            trip_history, 1):

        print(f"\nTrip {i}")

        print(
            f"Destination: {trip['destination']}"
        )

        print(
            f"Date: {trip['date']}"
        )

        print(
            f"People: {trip['people']}"
        )

        print(
            f"Budget: ₹{trip['budget']}"
        )



def after_trip_menu():

    while True:

        print("\n" + "=" * 60)
        print("              WHAT WOULD YOU LIKE TO DO?")
        print("=" * 60)

        print("1. Search another destination")
        print("2. View favourites")
        print("3. View trip history")
        print("4. View destination statistics")
        print("5. View available regions")
        print("6. Sort destinations")
        print("7. Start a new trip")
        print("8. Exit")

        try:

            choice = int(
                input("\nEnter your choice (1-8): ")
            )

            if choice == 1:

                search_destination()

            elif choice == 2:

                show_favourites()

            elif choice == 3:

                show_history()

            elif choice == 4:

                destination_statistics()

            elif choice == 5:

                show_regions()

            elif choice == 6:

                sort_destinations()

            elif choice == 7:

                return True

            elif choice == 8:

                print(
                    "\nThank you for using SmartTrip! ✈️"
                )

                return False

            else:

                print(
                    "Please choose a number from 1 to 8."
                )

        except ValueError:

            print("Please enter a number.")




def main():

    load_data()

    while True:

        print("\n" + "=" * 60)
        print("                    SMARTTRIP")
        print("               YOUR TRIP PLANNER")
        print("=" * 60)

        print(
            "\nLet's plan your trip step by step! ✈️"
        )

     
        print("\nSTEP 1: TRIP DETAILS")

        people = get_positive_number(
            "How many people are travelling? "
        )

        budget = get_budget()

        days = get_positive_number(
            "How many days do you want to travel? "
        )

        date = get_date()

        season = get_season(date)

        print(
            f"\nYour travel season is: {season}"
        )

       

        print("\nSTEP 2: TRIP TYPE")

        trip_type = choose_trip_type()


        print("\nSTEP 3: REGION")

        region = choose_region()

       
        print("\nFinding destinations for you...")

        recommendations = recommend_destinations(
            budget,
            days,
            season,
            trip_type,
            region
        )

        if not recommendations:

            print(
                "\nSorry, no destinations matched."
            )

            continue

       

        show_recommendations(
            recommendations
        )

      
        while True:

            try:

                choice = int(
                    input(
                        "\nChoose a destination (1-5): "
                    )
                )

                if 1 <= choice <= len(
                        recommendations):

                    selected = recommendations[
                        choice - 1
                    ][1]

                    break

                print(
                    "Please choose a valid number."
                )

            except ValueError:

                print(
                    "Please enter a number."
                )

      
        show_destination(selected)

       

        print(
            "\nWould you like to add this "
            "destination to favourites?"
        )

        print("1. Yes")
        print("2. No")

        while True:

            try:

                favourite_choice = int(
                    input(
                        "Enter your choice (1-2): "
                    )
                )

                if favourite_choice == 1:

                    add_favourite(selected)

                    break

                elif favourite_choice == 2:

                    break

                else:

                    print(
                        "Please choose 1 or 2."
                    )

            except ValueError:

                print(
                    "Please enter a number."
                )

        
        budget_breakdown(
            selected,
            people
        )

       
        create_itinerary(
            selected
        )

       

        packing_suggestions(
            selected
        )

        
        save_trip(
            selected,
            date,
            people
        )

        print("\n" + "=" * 60)
        print("             YOUR TRIP IS PLANNED! 🎉")
        print("=" * 60)

        
        new_trip = after_trip_menu()

        if not new_trip:

            break




main()