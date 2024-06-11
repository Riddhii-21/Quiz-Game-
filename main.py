print("Welcome to the quiz game")
questions = [
    {"text": "What does the CPU stand for?","answer":"A"},
    {"text":"The ability of one class to acquire methods and attributes of another class is called","answer":"D",},
    {"text":"Which of the following is a type of inheritance","answer":"D"},
    {"text":"What is the full form of 'AI'?","answer":"B"},
    {"text":"Which of the following is the branch of AI","answer":"A"}
]
options = [["A.Central Processing Unit","B.Computer Processing Unit","C.Computer Protection Unit","D.None Of These"],
           ["A.Abstraction","B.Polymorphism","C.Objects","D.Inheritance"],
           ["A.Single","B.Double","C.Multiple","D.Both A and C"],
           ["A.Artificially Intelligent","B.Artificial Intelligence","C.Artificially Intelligence","D.None of these"],
           ["A.Machine Learning","B.Cyber forensics","C.Full-Stack Developer","D.Network Design"]
]
score = 0
def check_answer(user_guess,correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False

for question_num in range(len(questions)):
    print("*************************")
    print(questions[question_num]["text"])
    for i in options[question_num]:
        print(i)

    guess = input("Enter your answer(A/B/C/D): ").upper()
    is_correct=check_answer(guess,questions[question_num]["answer"])
    if is_correct:
        print("Correct Answer")
        score = score+1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is {questions[question_num]['answer']}")
    print(f"Your current score is {score}/{question_num+1}")
print(f"Your final score is {score}")
print(f"Your score is {(score/len(questions))*100}%")
