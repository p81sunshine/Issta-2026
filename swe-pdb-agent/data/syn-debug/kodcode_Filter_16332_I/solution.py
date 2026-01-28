import random

class QuizGame:
    def __init__(self):
        self.questions = []
        self.high_score = 0

    def menu(self):
        while True:
            print("1. Start Quiz")
            print("2. View High Score")
            print("3. Add Question")
            print("4. Exit")
            
            choice = input("Select an option: ")
            
            if choice == '1':
                self.start_quiz()
            elif choice == '2':
                self.view_high_score()
            elif choice == '3':
                self.add_question()
            elif choice == '4':
                break
            else:
                print("Invalid option, please try again")

    def start_quiz(self):
        if not self.questions:
            print("No questions available. Please add questions first.")
            return
        
        question, answer = random.choice(self.questions)
        user_answer = input(f"Question: {question} ")
        
        if user_answer.strip().lower() == answer.strip().lower():
            print("Correct!")
            self.high_score += 1
        else:
            print(f"Wrong! The correct answer is '{answer}'")
        
        print(f"Your current score is {self.high_score}")

    def view_high_score(self):
        print(f"High Score: {self.high_score}")

    def add_question(self):
        question = input("Enter the question: ")
        answer = input("Enter the answer: ")
        self.questions.append((question, answer))
        print("Question added successfully.")