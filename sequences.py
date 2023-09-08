# Write a function remove_duplicates(sequence) that takes a 
# sequence (list or tuple) and returns a new sequence with duplicates 
# removed while maintaining the original order of elements. 

# sample input = 

# input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
# result = remove_duplicates(input_sequence)
# print(result)  # Output: [2, 3, 4, 5, 6, 7]

def remove_duplicates(sequence):
    number=set() #using a set to keep track of unique values
    result=[]
    for item in sequence:
        if item not in number:
            number.add(item)
            result.append(item)
    return result

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)

