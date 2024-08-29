import random
import time

def generate_question():
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    operator = random.choice(['+', '-', '×', '÷'])
    
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '×':
        correct_answer = num1 * num2
    else:
        # Ensure division result is an integer
        num1, num2 = num1 * num2, num2
        correct_answer = num1 // num2
    
    return f"{num1} {operator} {num2}", correct_answer

def math_tutor():
    num_questions = int(input("Enter the number of practice questions: "))
    correct_answers = 0
    start_time = time.time()

    for i in range(num_questions):
        question, correct_answer = generate_question()
        user_answer = int(input(f"Question {i + 1}: {question} = "))
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong. The correct answer is {correct_answer}.")

    end_time = time.time()
    total_time = end_time - start_time
    percent_correct = (correct_answers / num_questions) * 100

    print("\nThank you for playing!")
    print(f"Correct answers: {correct_answers}/{num_questions}")
    print(f"Percentage correct: {percent_correct:.2f}%")
    print(f"Total time taken: {total_time:.2f} seconds")
    print(f"Average time per question: {total_time / num_questions:.2f} seconds")

math_tutor()
