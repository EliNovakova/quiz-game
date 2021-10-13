from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    """Creates Tkinter window with all the graphics"""
    def __init__(self, quiz_brain: QuizBrain):     # we need to provide quiz brain in order to show question texts, we specify of what datatype it is by adding it here (class)
        self.quiz = quiz_brain  # to get access to the quiz brain in this class
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {0}", font=("Arial", 12), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="question", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_check)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_check)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        """Is able to fetch the question text from quiz brain's next_question"""
        self.canvas.config(bg="white")  # changes bg color back to white for a new question after it shines green or red
        if self.quiz.still_has_questions():     # if there are still questions (10), we check this by using still_has_question function from quiz brain
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")   # fetches score from quiz brain and displays it here
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")   # deactivates the button
            self.false_button.config(state="disabled")  # deactivates the button

    def true_check(self):
        """User pressed True, function checks if it's correct by calling check answer method in quiz brain"""
        is_right = self.quiz.check_answer("True")   # check_answer function from quiz brain returns True in this case
        self.give_feedback(is_right)    # canvas changes color based on user's answer

    def false_check(self):
        """User pressed False, function checks if it's correct by calling check answer method in quiz brain"""
        is_right = self.quiz.check_answer("False")   # check_answer function from quiz brain returns False in this case
        self.give_feedback(is_right)    # canvas changes color based on user's answer

    def give_feedback(self, is_right):
        """Let's user know if they got it right or wrong"""
        if is_right:
            self.canvas.config(bg="green")  # if the user got it right, canvas shines green
        else:
            self.canvas.config(bg="red")    # if they got it wrong, it turns red

        self.window.after(1000, self.get_next_question)     # after 1 second, it calls new_question function, which turns the bg color back to white
