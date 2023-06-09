from tkinter import *
from  quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quize_brain: QuizBrain):
        self.quiz = quize_brain
        self.window = Tk()
        self.window.title("Quizzian")
        self.window.config(background=THEME_COLOR,padx=20,pady=20)
        self.score=0
        self.score_label = Label(text=f"Score: {self.score}")
        self.score_label.config(fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text =self.canvas.create_text(150,125,text="Some question test",fill=THEME_COLOR,font=("Arial",20,"italic"),width=280)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        img1 = PhotoImage(file="images/true.png")
        self.true_button = Button(image=img1,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2,column=0)

        img2 = PhotoImage(file="images/false.png")
        self.false_button = Button(image=img2,highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            q_text =self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz ")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)

        # self.get_next_question()
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        # self.get_next_question()
    def give_feedback(self,is_right):

        if is_right:
            self.score+=1
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
