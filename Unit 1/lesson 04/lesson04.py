
#Opening a file in Python
# To open a file in Python, you can use the built-in `open()` function.
#file = open('file_name.txt', 'mode')

file = open('file_name.txt', 'r')
print(file.read())

#reading a file with

with open('file_name.txt', 'r') as file:
    content = file.read()
    print(f'{content}')

# Read the file line by line

print('#######################################################')
with open('file_name.txt', 'r') as file:
    for line in file:
        if 'feliciti' in line:
            print('found her')
        print(f'Read by line: 🦓 {line.strip()}')

print('#######################################################')

# Writing a file

with open('file_name.txt', 'w') as file:
    file.write('This is a new line.\n')

print('#######################################################')

# Creating a new file or overwriting an existing file
with open('file_name_2.txt', 'w') as file:
    file.write('This line overwrites the file.\n')

print('#######################################################')

# Appending to a file
with open('file_name.txt', 'a') as file:
    file.write('This line is appended to the file.\n')

#Error handling with files
#Basic try-except block

try:
    num = int(input('Enter a number: ')) # throws an error if input is not a number
    print(num + 10)
except TypeError as e:
    print('TypeError: ', e)
except:
    print('An error occurred. Please enter a valid number.')
