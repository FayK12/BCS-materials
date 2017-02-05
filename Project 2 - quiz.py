while (input("Are you ready for a quiz? Type 'Y' or 'N' only: ")=="N"):  #loop runs while user says N to doing the quiz.
    #if(input("Are you ready for a quiz? Type 'Y' or 'N'only: ")=="N"): #if stmt evaluates if input is Y or N to taking the quiz
        print("That's too bad. Let's try this again")
        print ()

print("Okay, here it comes!")
print()
print("Q1) Who should've been the US president in the Nov 8, 2016 president elections?")
print("     1) Hillary Clinton")
print("     2) Donald Trump")
print("     3) Bernie Sanders")
score = 0
A1=int(input("A1): "))

#if(int(input("A1)")) == 3): #tried to evaluate the input to answer and convert it to int. Didn't work
if(A1 == 3):
    print("Good job, we just might become friends")
    score = score + 1
#elif(input("A1)") == 2):
elif(A1 == 2):
    print("That's incorrect. The likelihood of him being President should have been the same likelihood as me eating a ham sandwich")
#elif(input("A1)") == 1):
elif(A1 == 1):
     print("I applaud your attempt")
else:
     print("You had to choose 1, 2, or 3.")

#print("Your current score is", score)
print()
print("Q2) Which country does not share a border with Cambodia?")
print("     1) Malaysia")
print("     2) Vietnam")
print("     3) Thailand")

A2=int(input("A2): ")) #user input
if(A2 == 1):
    print("Nicely done")
    score = score + 1
elif((A2 == 2) | (A2 == 3)):
    print("This country does share a border with Cambodia. This answer is Malaysia")
else:
    print("You had to choose 1, 2, or 3. Just like before...")
    
#print("Your current score is", score)
print()

print("Q3) Nov 11, 1918 is Remembrance Day, commemorating the end of what?")
print("     1) WWIII")
print("     2) Cold War")
print("     3) WWI")

A3=int(input("A3): ")) #user input
if(A3 == 3):
    print("Good job comrade!")
    score = score + 1
elif(A3 == 2):
    print("No, the answer is WWI")
elif(A3 == 1):
     print("Um..this event hasn't occurred in historical or present times so..No")
else:
    print("You had to choose 1, 2, or 3. Sigh.")
    
print("Overall, your current score is", score, "of 3. Was that so bad?")
print()

