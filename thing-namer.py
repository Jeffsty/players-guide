# Rebuild the example program
# add comments near each of the four variables that describe what they store
# Find the bug in the text displayed and fix it
# Answer this question: aside from comments, what is one thing you could do to make this code more understandable?

# asks the user for a noun
string_a = input("What kind of thing are we talking about?\n")
# asks the user for an adjective to describe the noun
string_b = input("How would you describe it? Big? Azure? Tattered?\n")
string_c = "of Doom"
string_d = "3000"
print(f"The {string_b} {string_a} {string_c} {string_d}!")

# change the variable names to makes the code more understandable
# string_a = thing
# string_b = adjective
# string_c = of_doom
# string_d = 3000
# or not use variables for string_c and string_d. instead just make them part of the printed string literally