import random


def generate_random_integer(min_value, max_value):
    """
    Generates a random integer between min_value and max_value (inclusive).

    Args:
        min_value (int): The minimum value of the range.
        max_value (int): The maximum value of the range.

    Returns:
        int: A randomly generated integer within the specified range.
    """
    return random.randint(min_value, max_value)


def choose_random_operator():
    """
    Selects a random mathematical operator from addition, subtraction, and multiplication.

    Returns:
        str: A randomly chosen operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])


def create_problem_and_answer(num1, num2, operator):
    """
    Creates a math problem string and calculates the incorrect answer.

    Args:
        num1 (int): The first number in the problem.
        num2 (int): The second number in the problem.
        operator (str): The math operator ('+', '-', or '*').

    Returns:
        tuple: A tuple containing the problem as a string and the incorrect answer as an integer.
    """
    problem = f"{num1} {operator} {num2}"

    # Introducing intentional incorrect answers for quiz
    if operator == '+':
        incorrect_answer = num1 - num2
    elif operator == '-':
        incorrect_answer = num1 + num2
    else:
        incorrect_answer = num1 * num2

    return problem, incorrect_answer


def math_quiz_game():
    """
    Runs a math quiz game where the player is presented with math problems
    and must provide answers. The game tracks the score based on correct answers.
    """
    score = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    print("But beware, the answers are intentionally incorrect to test your focus!")

    for question_number in range(1, total_questions + 1):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = choose_random_operator()

        problem, answer = create_problem_and_answer(num1, num2, operator)
        print(f"\nQuestion {question_number}: {problem}")

        try:
            user_answer = int(input("Your answer: "))

            if user_answer == answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer was {answer}.")
        except ValueError:
            print("Invalid input. Please enter a numerical answer.")

    print(f"\nGame over! Your final score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz_game()
