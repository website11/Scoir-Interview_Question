import pandas as pd

if __name__ == "__main__":
    file_path = input("Enter file path location: ")
    while True:
        user_input = input("Search names by: (1) First Name | (2) Last Name | (3) Date of Birth\n Pick an option (1, 2, or 3): ")
        csv_wb = pd.read_csv(file_path, usecols=range(0, 3))

        if user_input == '1':
            first_name = input("Enter the first name of the person you are searching for: ")
            name_search = csv_wb[csv_wb.FirstName == first_name]
            print(name_search)
            break

        elif user_input == '2':
            last_name = input("Enter the last name of the person you are searching for: ")
            name_search = csv_wb[csv_wb.LastName == last_name]
            print(name_search)
            break

        elif user_input == '3':
            user_dob = input("Enter the date of birth of the person you are searching for: ")
            dob_search = csv_wb[csv_wb.DOB == user_dob]
            print(dob_search)
            break

        else:
            print("Invalid Input! Try another input!")
            continue

    # C:/Users/alexa/OneDrive/Documents/Coding-Practice-Projects/Interview-Coding-Assignments/Scoir/names.csv
