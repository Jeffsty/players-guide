# Create a program that allows the user to enter how many provinces, duchies, and estates they have
# Add up the user's total score, giving 1 point per estate, 3 per duchy, and 6 per province
# Display the point total to the user

province = input("How many provinces do you own? ")
duchy = input("How many duchies do you own? ")
estate = input("How many estates do you own? ")

score = (int(estate) * 1) + (int(duchy) * 3) + (int(province) * 6)

print(f"{score} points")