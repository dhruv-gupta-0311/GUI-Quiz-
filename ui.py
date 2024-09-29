from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="some question",
                                                     fill="black",
                                                     font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.True_button = Button(image=true_image, highlightthickness=0, command=self.true_press)
        self.True_button.grid(row=2, column=0)
        self.False_button = Button(image=false_image, highlightthickness=0, command=self.false_press)
        self.False_button.grid(row=2, column=1)

        self.get_ques()

        self.window.mainloop()

    def get_ques(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            ques_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=ques_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of quiz")
            self.True_button.config(state="disabled")
            self.False_button.config(state="disabled")

    def true_press(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_press(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_ques)
