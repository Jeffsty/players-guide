# Take a number as input from the console
# Display 'Tick' if the number is even or 'Tock' if the number is odd

number = int(input("Enter a number: "))
remainder = number % 2

if remainder == 0:
    print("Tick")
else:
    print("Tock")