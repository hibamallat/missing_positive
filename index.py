"""
Write a function first_missing_positive(numbers) that finds the smallest 
positive integer that is missing from a given list
"""
def first_missing_positive(numbers):

    first_positive = 1

    for i in range (len(numbers)):
        if numbers[i] == first_positive:
            first_positive += 1
       
    return first_positive

#array = [3,4,-1,1]
#array = [1, 2, 0]
numbers_list = []
list_size = int(input("How many numbers would you like to add to the list? "))

for i in range (list_size):

    num = int(input(f"Enter nb{i+1}: "))
    numbers_list.append(num)

print(f"The List: {numbers_list}")
print(f"The first missing positive number: {first_missing_positive(numbers_list)}")
            
        
