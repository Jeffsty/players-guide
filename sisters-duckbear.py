# Create a program that lets the user enter the number of chocolate eggs gathered that day
# Using / and %, compute how many eggs each sister should get and how many are left over for the duckbear

eggs_gathered = input("How many eggs were gathered? ")
sisters = int(eggs_gathered) / 4
duckbear = int(eggs_gathered) % 4

print(f"The sisters get {int(sisters)} egg(s) each.")
print(f"The duckbear gets {duckbear} egg(s).") 