# Simple Quiz Application
print('######################### QUIZ APPLICATION #########################')
score = 0

questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['A) Paris', 'B) London', 'C) Berlin', 'D) Madrid'],
        'answer': 'A'
    },
    {
        'question': 'What is 2 + 2?',
        'options': ['A) 3', 'B) 4', 'C) 5', 'D) 6'],
        'answer': 'B'
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'options': ['A) Earth', 'B) Mars', 'C) Jupiter', 'D) Saturn'],
        'answer': 'C'
    }
]

star = ''

for question in questions:
  print(f' ❓ {question["question"]}')
  
  for option in question['options']:
    print(f'{option}')

  user_answer = input('Your answer (A, B, C, D): ').upper()

  if user_answer == question['answer']:
    star += '🌟'
    print(f'✅ Correct!\n {star}')
    score += 1
  else:
    print(f'❌ Incorrect! The correct answer is {question["answer"]}.\n')

print('######################### FINAL SCORE ##############################')
print(f'Your total score is: {score}')