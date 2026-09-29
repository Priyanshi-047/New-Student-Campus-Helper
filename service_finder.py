
def find_service(campus_places):

    service_name = input("Enter service:")

    found = False

    for place in campus_places:
        if service_name.lower() in [service.lower() for service in place["services"]]:
           print("Service:",service_name)
           print("Available at:",place["name"])
           print("Location:",place["location"])
           found = True

    if found == False:
        print("Service not found.")
