
def show_summary(campus_places):

    print("Campus Summary")
    print("----------------")

    print("Total places:", len(campus_places))

    categories = []

    for place in campus_places:
       if place["category"] not in categories:
        categories.append(place["category"])

    print("Total categories:", len(categories))
    print("Categories:", categories)
