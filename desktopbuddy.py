from cProfile import run
from secrets import choice

#Start
print("Hello buddy")
print("From 1 to 10 how would you rate your day so far?")


number = int(input('Enter a number: '))
#take input from user to answer
if number > 5:
    print("That's good, I hope I can make it even better")
if number < 5:
    print("That's very unfortunate, I hope i can make it better")

#Start options
print("What do you want me to do?")
print("1.Calculate")
print("2.Tell me a joke")
print("3.Run programs")
print("4.Search")
print("5.Random facts")

while True: 
    #take input from user
    choice = input("Enter choice(1/2/3/4/5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):
        if choice == '1':
            #calculator
            # This function adds two numbers
            def add(x, y):
                return x + y

            # This function subtracts two numbers
            def subtract(x, y):
                return x - y

            # This function multiplies two numbers
            def multiply(x, y):
                return x * y

            # This function divides two numbers
            def divide(x, y):
                return x / y
            
            print("Select operation.")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")

            while True:
                # take input from the user
                choice = input("Enter choice(1/2/3/4): ")

                # check if choice is one of the four options
                if choice in ('1', '2', '3', '4'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        print(num1, "+", num2, "=", add(num1, num2))

                    elif choice == '2':
                        print(num1, "-", num2, "=", subtract(num1, num2))

                    elif choice == '3':
                        print(num1, "*", num2, "=", multiply(num1, num2))

                    elif choice == '4':
                        print(num1, "/", num2, "=", divide(num1, num2))
                    
                    # check if user wants another calculation
                    # break the while loop if answer is no
                    next_calculation = input("Let's do next calculation? (yes/no): ")
                    if next_calculation == "no":
                        break 
                
                else:
                    print("Invalid Input")

        if choice == '2':
            # selects a random joke from the list
            import random
            
            jokes = ['Whats the best thing about Switzerland? I dont know, but the flag is a big pluss.',
            'Im afraid for the calendar. Its days are numbered.',
            'I only know 25 letters of the alphabet. I dont know y.',
            'I dont trust stairs. Theyre always up to something.',
            'I dont trust those trees. They seem kind of shady.',
            ]
            print(random.choice(jokes))
                  
        if choice == '3':
            # take input from the user and shows options
            print ("1. Notepad")
            print ("2. Browser")
            choice = input("Enter choice: ")
            
            if choice in ('1', '2', '3'):
                # runs the program
                if choice: '1'
                import subprocess
                subprocess.call('notepad.exe')

        if choice == '5':
            import random

            fax = ['I was made by Kamil Stefan Szynalski',
            'The earth is not flat',
            'You look good today', 
            'A shrimps heart is in its head',
            'A shark is the only known fish that can blink with both eyes',
            'I was inspired by Bonzibuddy',
            'Hawaii is moving closer to Alaska by 7.5cm every year',
            'Water makes different sounds depending on its temperature',
            'Humans are the only animals that blush!',
            'McDonalds invented a sweet-tasting type of broccoli',
            'There are bodies of over 150 dead hikers on Mount Everest, and they are used as landmarks',
            'I was developed in 2022',
            'Sharks do not have bones',
            'The blue whales blood vessels are so big that a human could swim through them',
            'A group of pandas is called an embarrassment',
            ]
            print(random.choice(fax))

        


        

           
                

