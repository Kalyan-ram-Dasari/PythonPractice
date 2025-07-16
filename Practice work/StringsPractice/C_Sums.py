#find the sum of numbers
# l =  input("Enter a list of numbers separated by spaces: ")
# l = l.split()
# s = 0
# for i in range(len(l)):
#     s += int(l[i])
# print("The sum of the numbers is:", s)


# l = input("Enter a list of numbers separated by spaces: ")
# l = l.split()
# s=0 
# for i in l :
#     s += int(i)
# print("The sum of the numbers is:", s)


# find the sum of numbers in a string
# def sum_of_numbers_in_string(s):
#     numbers = s.split()
#     total_sum = 0
#     for num in numbers:
#         try:
#             total_sum += int(num)
#         except ValueError:
#             continue  # Skip non-integer values
#     return total_sum

# s = input("Enter a string with numbers separated by spaces: ")
# print(sum_of_numbers_in_string(s))


#find the highest number in a list of numbers

# def find_highest_number(numbers):
#     if not numbers: 
#         return None  # Return None if the list is empty
#     highest = int(numbers[0])  # Initialize with the first number
#     for num in numbers:
#         if int(num) > highest:
#             highest = int(num)
#     return highest  

# # Example usage
# numbers = input("Enter a list of numbers separated by spaces: ").split()
# highest_number = find_highest_number(numbers)
# if highest_number is not None:
#     print("The highest number is:", highest_number)
# else:
#     print("The list is empty, no highest number found.")


# find the lowest number in a list of numbers
# def find_lowest_number(numbers):
#     if not numbers: 
#         return None  # Return None if the list is empty
#     lowest = int(numbers[0])   # Initialize with the first number
#     for num in numbers:
#         if int(num) < lowest:
#             lowest = int(num)
#     return lowest            
# # Example usage
# numbers = input("Enter a list of numbers separated by spaces: ").split()
# lowest_number = find_lowest_number(numbers)
# if lowest_number is not None:
#     print("The lowest number is:", lowest_number)
# else:
#     print("The list is empty, no lowest number found.")
    
    
# find the average of numbers in a list
# def find_average(numbers):
#     if not numbers: 
#         return None  # Return None if the list is empty
#     total_sum = 0
#     for num in numbers:
#         total_sum += int(num)
#     average = total_sum / len(numbers)
#     return average
# # Example usage
# numbers = input("Enter a list of numbers separated by spaces: ").split()
# average_number = find_average(numbers)
# if average_number is not None:
#     print("The average of the numbers is:", average_number)
# else:
#     print("The list is empty, no average found.") 
    
    
#Swap the list elements
def swap_elements(lst):
    if len(lst) < 2:
        return lst  # No swap needed for lists with less than 2 elements
    lst[0], lst[-1] = lst[-1], lst[0]  # Swap first and last elements
    return lst
# Example usage
lst = input("Enter a list of elements separated by spaces: ").split()       
swapped_list = swap_elements(lst)
print("List after swapping first and last elements:", swapped_list)

# swap of all elements in a list
def swap_all_elements(lst):
    if len(lst) < 2:
        return lst  # No swap needed for lists with less than 2 elements
    for i in range(len(lst) // 2):
        lst[i], lst[-(i + 1)] = lst[-(i + 1)], lst[i]  # Swap elements
    return lst
# Example usage
lst = input("Enter a list of elements separated by spaces: ").split()
swapped_all_list = swap_all_elements(lst)  

