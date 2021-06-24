from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for entry in question_data:
    text = entry['text']
    answer = entry['answer']
    question = Question(text=text, answer=answer)
    question_bank.append(question)

print(question_bank)
quiz = QuizBrain(question_bank)

# here we check if the quiz still has questions to ask the user
while quiz.still_has_questions():
    quiz.next_question()

print("You have successfully completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}.")
