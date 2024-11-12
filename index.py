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
#array = [1,2,3]
array = [1, 2, 0]
print(array)
print(first_missing_positive(array))
            
        
