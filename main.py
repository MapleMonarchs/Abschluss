from tkinter import *
import json, os, random

def displayQuestion(question, a1, a2, a3, a4):
    global questionBox, cA, cB, cC, cD

    questionBox.config(text=question)
    cA.config(text=a1)
    cB.config(text=a2)
    cC.config(text=a3)
    cD.config(text=a4)


def loadQuestions():
    global questions
    file = open(os.path.join("Questions", "questions.json"))
    questions = json.load(file)['questions']
    print(questions)


def chooseQuestion():
    global questions, correct, lastQuestionID

    choice = random.choice(questions)

    while choice['id'] == lastQuestionID:
        choice = random.choice(questions)

    print(choice)

    displayQuestion(choice['question'], choice['answerA'], choice['answerB'], choice['answerC'], choice['answerD'])
    correct = choice['correct']
    lastQuestionID = choice['id']

def displayCorrect(correctQuestion):
    global root, actionBox, correct, cA, cB, cC, cD
    nextButton = None

    def nextQuestion():
        actionBox.config(text="Wähle die richtige Antwort!")

        match correctQuestion:
            case "A":
                cA['state'] = "normal"
            case "B":
                cB['state'] = "normal"
            case "C":
                cC['state'] = "normal"
            case "D":
                cD['state'] = "normal"

        nextButton.pack_forget()

        chooseQuestion()

    actionBox.config(text="Antwort {} ist richtig!".format(correctQuestion))

    match correctQuestion:
        case "A":
            cA['state'] = "disabled"
        case "B":
            cB['state'] = "disabled"
        case "C":
            cC['state'] = "disabled"
        case "D":
            cD['state'] = "disabled"

    nextButton = Button(root, text="nächste Frage", command=nextQuestion)
    nextButton.pack()

def optionA():
    global correct
    print("A selected!")
    if correct == "0":
        print("A is correct!")
        displayCorrect("A")

def optionB():
    global correct
    print("B selected!")
    if correct == 1:
        print("B is correct!")
        displayCorrect("B")


def optionC():
    global correct
    print("C selected!")
    if correct == "2":
        print("C is correct!")
        displayCorrect("C")


def optionD():
    global correct
    print("D selected!")
    if correct == 3:
        print("D is correct!")
        displayCorrect("D")

def buildLayout():
    global root, selections, actionBox, questionBox, cA, cB, cC, cD

    selections = Frame(root)
    actionBox = Label(root, text="das wird getan")
    questionBox = Label(root, text="ja ich meine...?")

    cA = Button(selections, text="Option A", command=optionA)
    cB = Button(selections, text="Option B", command=optionB)
    cC = Button(selections, text="Option C", command=optionC)
    cD = Button(selections, text="Option D", command=optionD)

    cA.grid(row=1, column=0)
    cB.grid(row=1, column=1)
    cC.grid(row=2, column=0)
    cD.grid(row=2, column=1)

    actionBox.pack()
    questionBox.pack()
    selections.pack()


root = Tk()
root.geometry("800x600")

selections = None
actionBox = None
questionBox = None
cA = None
cB = None
cD = None
cC = None

questions = []
correct = None
lastQuestionID = None

buildLayout()
displayQuestion("NULL", "NULL", "NULL", "NULL", "NULL")
loadQuestions()
chooseQuestion()

if __name__ == "__main__":
    root.mainloop()
