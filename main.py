import json


def main():
    # Load Baby Data from File
    file = open("baby-names-data.json")
    baby_data = json.load(file)
    file.close()

    # Main Menu
    loop = True
    while loop:
        selection = getMenuSelection()

        if selection == "1":
            displayAll(baby_data)
        elif selection == "2":
            searchGender(baby_data)
        elif selection == "3":
            searchRank(baby_data)
        elif selection == "4":
            searchStartLetter(baby_data)
        elif selection == "5":
            searchNameLength(baby_data)
        elif selection == "6":
            print("\nGOODBYE!\n")
            loop = False


def getMenuSelection():
    # Print Menu & Return User Selection
    print("\n*** BABY DATA - MAIN MENU ***")
    print("* 1: Display All")
    print("* 2: Search by Gender")
    print("* 3: Search by Rank")
    print("* 4: Search by Starting Letter")
    print("* 5: Search by Name Length")
    print("* 6: Exit")

    return input("* Enter Option #: ")


def displayAll(baby_data):
    # Display All Baby Data
    print("\nDISPLAY ALL")
    for entry in baby_data:
        print(f"{entry['Name']} (Rank: {entry['Rank']}, Gender: {entry['Gender']})")


def searchGender(baby_data):
    # Dislay All Baby Names based on Gender
    print("\nSEARCH BY GENDER")
    gender = input("Enter a gender (Boy/Girl): ").capitalize()
    for entry in baby_data:
        if entry['Gender'] == gender:
            print(f"{entry['Name']} (Rank: {entry['Rank']}, Gender: {entry['Gender']})")


def searchRank(baby_data):
    # Display All Baby Names based on Rank
    print("\nSEARCH BY RANK")
    min_rank = int(input("Enter a minimum rank: "))
    max_rank = int(input("Enter a maximum rank: "))
    for entry in baby_data:
        if min_rank <= entry['Rank'] <= max_rank:
            print(f"{entry['Name']} (Rank: {entry['Rank']}, Gender: {entry['Gender']})")


def searchStartLetter(baby_data):
    # Display Baby Names starting with a letter
    print("\nSEARCH BY START LETTER")
    start_letter = input("Enter a starting letter: ").capitalize()
    for entry in baby_data:
        if entry['Name'].startswith(start_letter):
            print(f"{entry['Name']} (Rank: {entry['Rank']}, Gender: {entry['Gender']})")


def searchNameLength(baby_data):
    # Display Baby Names of a specific length
    print("\nSEARCH BY NAME LENGTH")
    name_length = int(input("Enter a name length: "))
    for entry in baby_data:
        if len(entry['Name']) == name_length:
            print(f"{entry['Name']} (Rank: {entry['Rank']}, Gender: {entry['Gender']})")


# Invoke main to begin program
if __name__ == "__main__":
    main()
