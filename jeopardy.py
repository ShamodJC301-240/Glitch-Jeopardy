import random
import time

questions = [
    {"question": "This planet is closest to the sun.", "answer": "Mercury"},
    {"question": "The largest ocean on Earth.", "answer": "Pacific"},
    {"question": "The author of '1984'.", "answer": "George Orwell"},
]

print("Welcome to Glitch Jeopardy! Or… maybe not.")

score = 0

for q in questions:
    print("\nQuestion: " + q["question"])
    user_answer = input("Your answer: ")

    # Randomly decide if the game glitches
    glitch = random.choice([True, False, False])  # More likely to be False first
    if glitch:
        print("Hmm… are you sure? Wait… maybe not!")
        time.sleep(1)
        # Change the answer randomly
        fake_answer = random.choice(["Banana", "Mars", "Shakespeare"])
        print(f"The correct answer is: {fake_answer}")
        score -= 1
    else:
        print("Correct… maybe…?")
        score += 1

    print(f"Your score: {score}")

print("\nThanks for playing Glitch Jeopardy! Or… did you really play?")