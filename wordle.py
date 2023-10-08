word = "hello"
answer = ""
X = "X"
O = "O"
C = "C"
for j in range (5):
    guess = input("Enter your guess")
    nguess = guess.lower()
    for i in range (len(nguess)) :
        if nguess[i] in word :
            if nguess[i] == word[i] :
                answer += "O"
            else :
                answer += "C"
        else :
                answer += "X"
    print(answer)
    if answer == "OOOOO":
        print("Congrates u got it")
        break
    else :
        print("Try again")
        answer = ""
