# Ask the user for an x and a y value. These are coordinates of the enemy relative to the watchtower's location
# Using the image, if statements, and relational operators, display a message about what direction the enemy is coming from. For example, "The enemy is to the northwest!" or "The enemy is here!"

x = int(input("X: "))
y = int(input("Y: "))

if x < 0:
    print("The enemy is to the northwest!")
elif x == 0:
    print("The enemy is to the north!")
else:
    print("The enemy is to the northeast!")