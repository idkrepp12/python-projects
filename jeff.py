import random

print("Hi")
while True:
    print("ask me your question...")
    question = input("> ")

    answers = ['yes','no','maybe','i dont know','most likley']
    answer = random.choice(answers)
    print(answer)
