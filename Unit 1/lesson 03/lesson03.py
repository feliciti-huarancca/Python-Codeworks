def user(name, age, city):
  print(f'Name: {name}')
  print(f'Age: {age}')
  print(f'City: {city}')

user('Alice', 30, 'Boise')

# Systax List Comprehension Example
# new_list = [expression for item in collection if condition]
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]

#print(squared_numbers)
#
#for number in numbers:
#  squared_numbers.append(number ** 2)

print(squared_numbers)

numbers = [1, 2, 3, 4, 5]
