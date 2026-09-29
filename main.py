
from campus_data import campus_places
from campus_info import display_places
from search import search_places
from service_finder import find_service
from quick_help import quick_help
from summary import show_summary
from validation import is_valid_menu_choice

while True:
    print("\n=====New Student Campus Helper=====")
    print("1. View Campus Places")
    print("2. Search Places")
    print("3. Find Service")
    print("4. Campus Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if not is_valid_menu_choice(choice):
      print("Invalid choice.Please try again ")
      continue

    if choice == "1":
        display_places(campus_places)

    elif choice =="2":
      search_places(campus_places)

    elif choice =="3":
      find_service(campus_places)

    elif choice =="4":
      show_summary(campus_places)

    elif choice =="5":
      quick_help()

    elif choice =="6":
      print("Thank you for using Campus Heelper!")
      break
