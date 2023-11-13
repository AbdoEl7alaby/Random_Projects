import random
print("================================")
print("|  O = right letter and place  |\n| C = right letter wrong place |\n|  X = wrong letter and place  |\n|        ! # NO CAPS #!        |")
print("================================")
words = ['happy','water','house','juice','power','knife','hello','penta','apple','horse','flash','glass','board','creed','mouse','cable','sound','speed','spoon','fight','queen','novel','black','width','eight','plane','virus','right','teeth','tower','drama']
answer = ""
for k in range (len(words)):
    word = random.choice(words)
    for j in range (5):
        guess = input("Enter your guess : ")
        nguess = guess.lower()
        for i in range (len(nguess)) :
            if nguess[i] in word :
                if nguess[i] == word[i] :
                    answer += "O "
                else :
                    answer += "C "
            else :
                    answer += "X "
        print(answer)
        if answer == "O O O O O ":
            print("Congrates u got it\n------------------------------")
            answer = ""
            break
        else :
            print("Try again")
            answer = ""
print("THE END")
