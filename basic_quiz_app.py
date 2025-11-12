def run_quiz(questions):
    score = 0
    print("🧠 Welcome to the Python Quiz!\n")

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}. {q['question']}")
        for option in q["options"]:
            print(option)

        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

    print(f"🏁 You got {score} out of {len(questions)} correct!")
    percentage = (score / len(questions)) * 100
    print(f"Your score: {percentage:.2f}%")

    if percentage == 100:
        print("🔥 Perfect score! You're a pro!")
    elif percentage >= 70:
        print("👏 Great job!")
    else:
        print("💡 Keep practicing!")


def main():
    
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. Rome", "C. Madrid", "D. Berlin"],
            "answer": "A"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. func", "B. define", "C. def", "D. lambda"],
            "answer": "C"
        },
        {
            "question": "What data type is returned by the input() function?",
            "options": ["A. int", "B. str", "C. bool", "D. float"],
            "answer": "B"
        }
    ]

    run_quiz(questions)


if __name__ == "__main__":
    main()
