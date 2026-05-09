print("WELCOME...")

player=input("do you want to play? ")

if player.lower() !="yes":
    quit()

print("okk lets play")
score=0

question=input("How many days do we have in a week? ")
if question.lower() =="seven":
    print("correct answer")
    score += 1
else:
    print("wrong answer")

question = input("Which direction the sun raise? ")
if question.lower() == "east":
    score += 1
    print("correct answer")
else:
    print("wrong answer")

question = input("What is the capital of India?")
if question.lower() == "delhi":
    score += 1
    print("correct answer")
else:
    print("wrong answer")

question = input("What is the national animal of India?")
if question.lower()== "tiger":
    score += 1
    print("correct answer")
else:
    print("wrong answer")

question = input("Which is the smallest prime number?")
if question.lower() == "two":
    score += 1
    print("correct answer")
else:
    print("wrong answer")

question = input("Which festival is called the Festival of Lights in India?")
if question.lower() == "diwali":
    score +=1
    print("correct answer")
else:
    print("wrong answer")

question = input("How many colors are there in a rainbow?")
if question.lower() == "seven":
    score +=1
    print("correct answer")
else:
    print("wrong answer")

question = input("What is the national bird of India?")
if question.lower() == "peacock":
    score +=1
    print("correct answer")
else:
    print("wrong answer")

question = input("What is the national flower of India?")
if question.lower() == "lotus":
    score +=1
    print("correct answer")
else:
    print("wrong answer")

question = input("What is the currency of India?")
if question.lower() == "rupee":
    score +=1
    print("correct answer")
else:
    print("wrong answer")

print("your score"+str(score))