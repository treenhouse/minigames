from tkinter import *

root = Tk()

AnswerVar = IntVar()
AnswerBox = Entry(topFrame)
AdditionQuestionLeftSide = random.randint(0, 10)
AdditionQuestionRightSide = random.randint(0, 10)
AdditionQuestionRightSide = Label(topFrame, text= AdditionQuestionRightSide).grid(row=0,column=0)
AdditionSign = Label(topFrame, text="+").grid(row=0,column=1)
AdditionQuestionLeftSide= Label(topFrame, text= AdditionQuestionLeftSide).grid(row=0,column=2)
EqualsSign = Label(topFrame, text="=").grid(row=0,column=3)
AnswerBox.grid(row=0,column=4)
answerVar = AnswerBox.get()
    
root.mainloop() 
(


)