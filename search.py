
def search_places(campus_places):

    search_name = input("Enter place name:")

    found = False

    for place in campus_places:
       if place["name"].lower()==search_name.lower():
           print("Name:",place["name"])
           print("Category:",place["category"])
           print("Location:",place["location"])
           print("Purpose:",place["purpose"])
           print("Services:",place["services"])
           found = True

    if found == False:
        print("Place not found.")
