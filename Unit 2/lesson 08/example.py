import re

text = 'My cat is being so lazy, my cat does not like to be pet sometimes, my cat is a grumpy old cat'

is_match = re.search(r'cat', text)
print(is_match)

if is_match:
  print('🙀')
else:
  print('No cat')

email_pattern = r'[a-zA-Z.-_]+@[a-z]+\.(?:com|edu|net)'

email_01 = 'coreyjefferson@bogusemail.edu'

#Testing Changes in Github