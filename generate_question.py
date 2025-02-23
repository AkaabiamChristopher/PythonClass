import random

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    question = f"What is {num1} {operator} {num2}?"

    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    elif operator == '/':
        correct_answer = num1 / num2

    return question, correct_answer

correct_answers = 0

for i in range(10):
    question, correct_answer = generate_question()
    print(question)
    player_answer = input("Your answer: ")
    
    if float(player_answer) == correct_answer:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")

print(f"You got {correct_answers} out of 10 questions correct.")
print(f"Your score: {correct_answers}/10")
