# Read in three numbers from the user
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

# Create a list of the three numbers and sort in ascending order
numb_sorted = sorted([num_1, num_3, num_2])

# Print the sorted list
print("The numbers in sorted order are:", numb_sorted)