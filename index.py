"""
Write a function first_missing_positive(numbers) that finds the smallest 
positive integer that is missing from a given list
"""
def first_missing_positive(numbers):
    # Save the lowest positive integer
    first_positive = 1

    for i in range (len(numbers)):
        # If the value at index i equals 1, increment first_positive by 1
        if numbers[i] == first_positive:
            first_positive += 1
       
    return first_positive

#array = [3,4,-1,1]
#array = [1, 2, 0]
numbers_list = []

try:

    list_size = int(input("How many numbers would you like to add to the list? "))

    #Collect numbers from the user based on the specified list size
    for i in range (list_size):

        num = int(input(f"Enter nb{i + 1}: "))
        numbers_list.append(num)

    print(f"The List: {numbers_list}")
    print(f"The first missing positive number: {first_missing_positive(numbers_list)}")

except ValueError:
     #Handle any input that is not a number
    print("Enter numbers only!") 
            
        
