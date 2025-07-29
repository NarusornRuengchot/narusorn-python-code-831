"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Baimon", 20, "Chachoengsao", "Thailand")  # name, age, city, country
    hobbies = []

    while True:
        choice = input("Please select options (1.Display info 2.Add hobby 3.Remove hobby 4.Edit age 5.Exit) : ")
        
        # Your code here
        # Display info
        if choice == "1":
            print("Name : ",person[0])
            print("Age : ",person[1])
            print("City : ",person[2])
            print("Country : ",person[3])
            print("Hobbies : ",hobbies)

        # Add hobby
        elif choice == "2":
            hobby = input("What is your hobby? : ")
            hobbies.append(hobby)

        # Remove hobby
        elif choice == "3":
            del hobbies[0]

        # Edit age
        elif choice == "4":
            person_list = list(person)
            age = int(input("How lod are you? : "))
            person_list[1] = age
            person = tuple(person_list)

        elif choice == '5':
            break  

if __name__ == "__main__":
        personal_info_manager()