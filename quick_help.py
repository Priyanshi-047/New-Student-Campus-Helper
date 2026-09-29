
def quick_help():

    help_type = input("What help do you need?")

    if help_type.lower() == "study":
        print("For study,visit the Library.")
        print("location:","Main Academics Block")

    elif help_type.lower() == "medical":
       print("For medical help, visit the Medical Room.")
       print("Location:", "Main Campus")

    elif help_type.lower() == "books":
       print("For books,visit the library.")
       print("Location:","Main Academic Block")

    else:
        print("Sorry, help option not found.")
