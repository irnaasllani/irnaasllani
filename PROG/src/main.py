import random

# This function loads the questions from a specified file
def load_questions(filename):
    questions = {}
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(';')
            # If line contains exactly two parts, a question and an answer
            if len(parts) == 2:
                question, answer = parts
                # Add the question and answer
                questions[question] = answer
            else:
                print(f"Skipping invalid line: {line}")
    # Return the dictionary of questions and answers
    return questions

# This function prints a question and captures the user's answer
def ask_question(question):
    print(question)
    # Return the user's input as the answer
    return input("Your answer: ")

# This function checks if the user's answer matches the correct answer
def check_answer(user_answer, correct_answer):
    # Compare answers case-insensitively and strip any leading/trailing whitespace
    return user_answer.lower().strip() == correct_answer.lower().strip()

# This is the main function for the quiz game, which takes the dictionary of questions and answers
def quiz_game(questions):
    # Initialize the score variable
    score = 0
    # Convert the questions dictionary into a list of items and shuffled them
    questions_list = list(questions.items())
    random.shuffle(questions_list)

    for question, correct_answer in questions_list:
        user_answer = ask_question(question)
        # Check if the user's answer is correct
        if check_answer(user_answer, correct_answer):
            print("Correct!\n")
            # Increment the score for a correct answer
            score += 1
        else:
            # Inform the user of the correct answer if they got it wrong
            print(f"Wrong! The correct answer is: {correct_answer}\n")
    
    # At the end of the quiz, print the user's final score
    print(f"Game over! Your final score is {score}/{len(questions)}.")

# This conditional checks if the script is being run as the main program
if __name__ == "__main__":
    # Define the path to the questions file
    questions_filename = "assets/questions.txt"
    # Load the questions from the file
    questions = load_questions(questions_filename)
    # Start the quiz game with the loaded questions
    quiz_game(questions)
