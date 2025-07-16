 
#Another way to check Armstrong number using recursion
# def is_armstrong(num, num_digits=None):
#     if num_digits is None:    
#         str_num = str(num)
#         num_digits = len(str_num)
#     if num == 0:
#         return 0
#     last_digit = num % 10
#     remaining_num = num // 10
#     return (last_digit ** num_digits) + is_armstrong(remaining_num, num_digits)
# # Example usage
# number = int(input("Enter a number to check if it is an Armstrong number: "))
# if is_armstrong(number) == number:   
#     print(f"{number} is an Armstrong number.")
# else:
#     print(f"{number} is not an Armstrong number.")  













