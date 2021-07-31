import random
responses = ["yes I agree","sure","okay","yes","sure dude","my answer is yes","okay dude","yes","yes","yes","okay, but be careful!", "I'm not so sure", "not saying it's a yes or a no", "definitely no", "never", "are you crazy, absoulately no"]
while 1:
    check = input("check: ")
    def question():
        ques = input("ask question: ")
        print(random.choice(responses))
    if check == "okay":
        print(random.choice(responses))
    else:
        question()