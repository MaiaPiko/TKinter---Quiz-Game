THEME_COLOR = "#375362"
ques_font = ("Arial", 20, "italic")
from quiz_brain import QuizBrain
import tkinter

import data


class QuizzUserInterface:




    def __init__(self, quizbrain : QuizBrain):
        self.quiz = quizbrain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, pady=20,padx=20)



        self.score_label = tkinter.Label(text= "Score = 0", background=THEME_COLOR, foreground='white',  )
        self.score_label.grid(row =0, column=1)


        self.canvas = tkinter.Canvas(height=250, width=300)
        self.canvas.itemconfig(self.window,background = "white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question", font=ques_font )

        self.check_picture = tkinter.PhotoImage(file="images/true.png")
        self.check_button = tkinter.Button(image=self.check_picture,pady=100, command=self.check_answer_true)
        self.check_button.grid(row=2,column=0)

        self.cross_picture = tkinter.PhotoImage(file="images/false.png")
        self.cross_button = tkinter.Button(image=self.cross_picture, pady=100,command=self.check_answer_false)
        self.cross_button.grid(row=2, column=1)
        self.print_question()


        self.window.mainloop()

    def print_question(self):
        self.canvas.configure(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
            self.score_label.config(text=f"Score : {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text= f"Quiz Over: Your score is {self.quiz.score}/10." )
            self.cross_button.config(state="disabled")
            self.check_button.config(state="disabled")

    def check_answer_true(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))


    def check_answer_false(self):
        self.give_feedback(self.quiz.check_answer(user_answer="False"))


    def give_feedback(self,is_right):
        def green():
            self.canvas.configure(background="green")

        def red():
            self.canvas.configure(background="red")

        if is_right==True:
            green()
            self.quiz.score +=1

            self.canvas.after(1000,self.print_question)


        else:
            red()
            self.canvas.after(1000,self.print_question)
