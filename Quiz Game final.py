from tkinter import *
from tkinter import messagebox

class Quiz:
    def __init__(self):
        self.questions = [
            {'question': 'What is 3x5x7?', 'options': ['103', '104', '105', '106'], 'answer': '105'},
            {'question': 'What is 2^4x2^5?', 'options': ['502', '510', '512', '516'], 'answer': '512'},
            {'question': 'What is the ones digit of 2^159?', 'options': ['4', '6', '2', '8'], 'answer': '2'},
            {'question': 'What is the value of y in this equation; 2x+y=10,x-y=6?', 'options': ['-1.5', '1', '-2', '-3'], 'answer': '-1.5'},
            {'question': 'which one is a prime number?', 'options': ['1', '3', '8', '6'], 'answer': '3'},
            {'question': 'In how many ways can you choose 2 balls out from a box that contains 15 balls?', 'options': ['135', '170', '105', '119'], 'answer': '105'},
        ]
        self.score = 0
        self.current_question = 0

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]['answer']
        if selected_option == correct_answer:
            self.score += 1
            return True
        else:
            return False

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            return True
        else:
            return False

class App(Tk):
    def __init__(self, quiz):
        super().__init__()
        self.title('Quiz')
        self.my_quiz = quiz
        self.config(bg='lightblue')
        self.geometry('600x400')

        self.title_label = Label(self, text='Quiz Time')
        self.title_label.config(font=('Courier', 15))
        self.title_label.pack(pady=10)

        self.question_label = Label(self, text='', wraplength=400)
        self.question_label.config(font=('Arial', 12))
        self.question_label.pack(pady=20)

        self.option_list = StringVar(value='')
        self.option_buttons = []

        for i in range(4):  # Create three option buttons
            rb = Radiobutton(self, text='', variable=self.option_list, value='', wraplength=400)
            rb.pack(anchor=W, padx=20, pady=5)
            self.option_buttons.append(rb)

        # Submit Button
        self.submit_button = Button(self, text='Submit', command=self.submit_answer)
        self.submit_button.config(font=('Arial', 12))
        self.submit_button.pack(pady=20)

        # Answer Label
        self.answer_label = Label(self, text='')
        self.answer_label.config(font=('Courier', 12))
        self.answer_label.pack(pady=20)

        # Score Label
        self.score_label = Label(self, text='Score: 0')
        self.score_label.config(font=('Courier', 12))
        self.score_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        question_data = self.my_quiz.questions[self.my_quiz.current_question]
        self.question_label.config(text=question_data['question'])
        for i, option in enumerate(question_data['options']):
            self.option_buttons[i].config(text=option, value=option)
        self.option_list.set('')  # Clear previous selection
        self.answer_label.config(text='')

    def submit_answer(self):
        selected_option = self.option_list.get()
        if self.my_quiz.check_answer(selected_option):
            self.answer_label.config(text='Correct!', fg='green')
        else:
            correct_answer = self.my_quiz.questions[self.my_quiz.current_question]['answer']
            self.answer_label.config(text=f'Wrong! Correct Answer: {correct_answer}', fg='red')

        self.score_label.config(text=f'Score: {self.my_quiz.score}')
        if self.my_quiz.next_question():
            self.load_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        total_questions = len(self.my_quiz.questions)
        score_text = f"Your final score is: {self.my_quiz.score}/{total_questions}"
        messagebox.showinfo("Quiz Over", score_text)
        self.submit_button.config(state=DISABLED)
        self.destroy()

# Launch the App
my_quiz = Quiz()
app = App(my_quiz)
app.mainloop()
