# def product_of_elements(lst):
#     product = 1
#     for num in lst:
#         product *= num
#     return product


# numbers = [1, 2, 3, 4, 5]
# result = product_of_elements(numbers)
# print(result)







# def find_minimum(list):
#     if not list:  
#         raise ValueError("Список не повинен бути порожнім")
    
#     minimum = list[0]
#     for num in list:
#         if num < minimum:
#             minimum = num
#     return minimum

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# result = find_minimum(numbers)
# print(result)  




# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# def count_primes(lst):
#     prime_count = 0
#     for num in lst:
#         if is_prime(num):
#             prime_count += 1
#     return prime_count

# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# result = count_primes(numbers)
# print(result)  






# def remove_element(lst, value):
#     count_removed = 0
#     while value in lst:
#         lst.remove(value)
#         count_removed += 1
#     return count_removed

# numbers = [1, 2, 3, 4, 2, 2, 5, 2]
# value_to_remove = 2
# result = remove_element(numbers, value_to_remove)
# print(result) 
# print(numbers)







# def combine_lists(list1, list2):
#     return list1 + list2

# list_a = [1, 2, 3]
# list_b = [4, 5, 6]
# result = combine_lists(list_a, list_b)
# print(result)  







def power_elements(lst, power):
    return [x ** power for x in lst]

numbers = [1, 2, 3, 4, 5]
power = 2
result = power_elements(numbers, power)
print(result)  