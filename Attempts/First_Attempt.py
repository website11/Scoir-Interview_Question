import csv



def swap(data, first, second):
    temp = data[first]
    data[first] = data[second]
    data[second] = temp


def partition(data, start, stop):
    pivot = start
    for i in range(start, stop):
        if data[i] > data[stop]:
            swap(data, pivot, i)
            pivot += 1
    swap(data, pivot, stop)

    return pivot


def quickSort(data, start, stop):
    if start < stop:
        p = partition(data, start, stop)
        quickSort(data, p + 1, stop)
        quickSort(data, start, p - 1)


if __name__ == "__main__":

    file_path = input("Enter file path location: ")
    user_input = input("Search names by: (1) First Name | (2) Last Name | (3) Date of Birth\n Pick an option (1, 2, or 3): ")
    with open(file_path,'r') as names_list:
        total_rows = len(open(file_path).readlines())
        table = csv.reader(names_list)

        first_name_list = []
        last_name_list = []
        dob_list = []

        for row in table:
            first_name_list.append(row[0])
            last_name_list.append(row[1])
            dob_list.append(row[2])
        list_of_all_elements = list(table)

        if user_input == '1':
            quickSort(first_name_list,0,total_rows - 1)
            print(first_name_list)

        elif user_input == '2':
            quickSort(last_name_list, 0, total_rows - 1)
            print(last_name_list)

        elif user_input == '3':
            quickSort(dob_list, 0, total_rows - 1)
            print(dob_list)

        else:
            print("Input not valid!")


#C:/Users/alexa/OneDrive/Documents/Coding-Practice-Projects/Interview-Coding-Assignments/Scoir/names.csv