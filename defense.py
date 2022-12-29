# Ask the user for the target row and column
# Compute the neighbouring rows and columns of where to deploy the squad
# Display the deployment instructions in a different colour of your choosing
# Change the window title to be "Defense of Consolas"
# Play a sound when the results have been computed and displayed

target_row = input("Target row? ")
target_column = input("Target column? ")

# changes the text color
print('\033[5;35;40m CHEESY \033[0;0m')