class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.question_list = questions_list
        self.score = 0

    def next_question(self):
        ques = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {ques.text} (True/False): ")
        self.check_answer(response, ques.answer)

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def check_answer(self, user_answer, right_answer):
        if user_answer.lower() == right_answer.lower():
            print("You're right!")
            self.score += 1
        else:
            print("Sorry, that's wrong.")
        print(f"The correct answer was: {right_answer}.\nYour current score is: {self.score}/{self.question_number}.\n")
