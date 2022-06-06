#Note: THE FILES MUST BE NAMED: subject.txt

def format_QandAFromFile():
    """Asks a user for the subject an opens a text file under that name. converts the text file into nested list"""
    stop = False
    while not stop: #starting a loop
        try: #try and except to keep making sure that the file the user wants to study acctualy exists.  
            subjects = ["History", "Spanish", "Math"] #list of subjects to make adding subjects easier
            print("The subjects that are avalible are:") 
            for subject in subjects: #printing the avalible subjects
                print(subject)
            fileInput = input("Which subject do you want to study? ") #getting the subject the user wants to study
            fileInput = str(fileInput+".txt")   

            with open(fileInput, 'r') as subjectFile: #opening the file. if there is an error and the file isnt found the program loops
                lines = subjectFile.readlines()
                for line in lines:
                    if line.strip() == "": #if the line is empty the program removes it so there are no left over "\n"s
                        lines.remove(line)
                questionsAndAnswers = []
                for x in range(0,len(lines),2): #making a for loop that runs as many times as there are a set of questions and answers
                    questionsAndAnswers.append([]) #appending a list to the list
                    for i in range(1):
                        questionsAndAnswers[int(x/2)].append(lines[x].strip("\n")) #appening the question to the list inside the list
                        questionsAndAnswers[int(x/2)].append(lines[x+1].strip("\n")) #appening the answer to the list inside the list
                stop = True
                return questionsAndAnswers #returns the list
        except TypeError:
            print("This is not a subject that you can study. please check your spelling and try agian") #checking for a error with the file opening procces
        except IOError:
            print("This is not a subject that you can study. please check your spelling and try agian")        

def Ask_Questions(QandAlist):
    """Asks the user the questions and returns a score"""
    score = 0
    total = 0
    for x in range(0,len(QandAlist)): #for the ammount of question and answer pairs in the q and a list the program asks the user the questions
        for i in range(0,1):
            answer = input(QandAlist[x][i]+"\nYour Answer: ")
            if answer.lower() == QandAlist[x][i+1].lower(): #checks to see if the answer is correct 
                print("correct!\n")
                score += 1
                total += 1
            else:
                print("Inccorect")
                total += 1
                print("The correct answer was: ",QandAlist[x][i+1],"\n") #displaying the correct answer
    return score, total


def main():
    """The main function that gives the output of the score to the user"""
    questionsAndAnswers = format_QandAFromFile()
    score, numOfQuestions = Ask_Questions(questionsAndAnswers)
    percentScore = (score/numOfQuestions)*100

    keepGoing = True #loop to keep asking until user gives a valid response
    while keepGoing:
        wantGrade = str(input("do you want a grade on this quiz? ")) #asking the user if they want their score
        print("\n")
        if wantGrade.strip().lower() == "yes" or wantGrade.strip().lower() == "y":
            print(f"you got {score}/{numOfQuestions} questions correct.")
            print(f"that is a score of: {percentScore:.0f}%")
            if percentScore > 75: #if the user's score is above 75 the program prints a message congradualting them.
                print("Good Job!")
            keepGoing = False
        elif wantGrade.strip().lower() == "no" or wantGrade.strip().lower() == "n":
            print("Okee Dokee")
            keepGoing = False
        else:
            print("This is not a valid responce")


main()
keepGoing = True
while keepGoing:
    keepQuizing = input("Do you want to keep taking quizes? ") #looping the main function until user no longer wants to be quized 
    keepQuizing = str(keepQuizing.lower())
    if keepQuizing == "y" or keepQuizing == "yes":
        main()
    elif keepQuizing == "n" or keepQuizing == "no":
        print("bye!")
        keepGoing = False        
    else:
        keepGoing = True

