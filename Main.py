import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:

    def __init__(self, root):
        self.root = root
        self.root.title("AI Quiz Game")
        self.root.geometry("800x650")
        self.root.configure(bg="#1a1a2e")

        self.main_frame = tk.Frame(self.root, bg="#1a1a2e")
        self.main_frame.pack(fill="both", expand=True)
        self.main_frame.pack_propagate(False)

        self.questions = [
            {
                "question": "What does AI stand for?",
                "options": ["Artificial Intelligence", "Automated Information", "Advanced Integration", "Algorithmic Interface"],
                "answer": 0
            },
            {
                "question": "Which of the following is a type of machine learning?",
                "options": ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "All of the above"],
                "answer": 3
            },
            {
                "question": "What is a neural network inspired by?",
                "options": ["Computer circuits", "Human brain", "Mathematical equations", "Database systems"],
                "answer": 1
            },
            {
                "question": "Which algorithm is commonly used for classification?",
                "options": ["Linear Regression", "Decision Trees", "K-Means", "PCA"],
                "answer": 1
            },
            {
                "question": "What is the process of training an AI model called?",
                "options": ["Debugging", "Learning", "Compiling", "Rendering"],
                "answer": 1
            },
            {
                "question": "Which company developed ChatGPT?",
                "options": ["Google", "Microsoft", "OpenAI", "Meta"],
                "answer": 2
            },
            {
                "question": "What does NLP stand for in AI?",
                "options": ["Neural Language Processing", "Natural Language Processing", "Network Layer Protocol", "New Learning Pattern"],
                "answer": 1
            },
            {
                "question": "Which of these is a deep learning framework?",
                "options": ["Excel", "TensorFlow", "Photoshop", "WordPress"],
                "answer": 1
            },
            {
                "question": "What is overfitting in ML?",
                "options": ["Model performs well on training but poorly on new data", "Model is too simple", "Model trains too fast", "Model uses too little data"],
                "answer": 0
            },
            {
                "question": "Which technique helps prevent overfitting?",
                "options": ["Adding more layers", "Regularization", "Increasing LR", "Removing data"],
                "answer": 1
            }
        ]

        self.score = 0
        self.current_question = 0
        self.selected_answer = tk.IntVar()
        self.create_start_screen()

    def create_start_screen(self):
        self.clear_screen()

        title_label = tk.Label(
            self.main_frame,
            text="🤖 AI QUIZ GAME 🤖",
            font=("Arial", 36, "bold"),
            bg="#1a1a2e",
            fg="#00d4ff"
        )
        title_label.pack(pady=80)

        desc_label = tk.Label(
            self.main_frame,
            text="Test your knowledge about Artificial Intelligence!",
            font=("Arial", 16),
            bg="#1a1a2e",
            fg="#ffffff"
        )
        desc_label.pack(pady=20)

        count_label = tk.Label(
            self.main_frame,
            text=f"Total Questions: {len(self.questions)}",
            font=("Arial", 14),
            bg="#1a1a2e",
            fg="#ffcc00"
        )
        count_label.pack(pady=10)

        start_btn = tk.Button(
            self.main_frame,
            text="START QUIZ",
            font=("Arial", 18, "bold"),
            bg="#00d4ff",
            fg="#1a1a2e",
            activebackground="#00a8cc",
            activeforeground="#1a1a2e",
            bd=0,
            padx=40,
            pady=15,
            cursor="hand2",
            command=self.start_quiz
        )
        start_btn.pack(pady=30)

    def start_quiz(self):
        self.score = 0
        self.current_question = 0
        random.shuffle(self.questions)
        self.show_question()

    def clear_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_question(self):
        self.clear_screen()
        self.selected_answer.set(-1)

        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]

            progress_frame = tk.Frame(self.main_frame, bg="#1a1a2e")
            progress_frame.pack(fill="x", padx=20, pady=10)

            tk.Label(
                progress_frame,
                text=f"Question {self.current_question + 1} of {len(self.questions)}",
                font=("Arial", 12),
                bg="#1a1a2e",
                fg="#ffffff"
            ).pack(side="left")

            tk.Label(
                progress_frame,
                text=f"Score: {self.score}",
                font=("Arial", 12, "bold"),
                bg="#1a1a2e",
                fg="#00ff00"
            ).pack(side="right")

            tk.Label(
                self.main_frame,
                text=q["question"],
                font=("Arial", 20, "bold"),
                bg="#1a1a2e",
                fg="#ffffff",
                wraplength=700,
                justify="center"
            ).pack(pady=20)

            options_frame = tk.Frame(self.main_frame, bg="#1a1a2e")
            options_frame.pack(pady=10)

            for i, option in enumerate(q["options"]):
                tk.Radiobutton(
                    options_frame,
                    text=option,
                    variable=self.selected_answer,
                    value=i,
                    font=("Arial", 14),
                    bg="#16213e",
                    fg="#ffffff",
                    selectcolor="#0f3460",
                    activebackground="#16213e",
                    activeforeground="#00d4ff",
                    indicator=0,
                    width=50,
                    padx=20,
                    pady=15,
                    cursor="hand2",
                    borderwidth=2,
                    relief="raised"
                ).pack(pady=6)

            submit_btn = tk.Button(
                self.main_frame,
                text="SUBMIT ANSWER",
                font=("Arial", 16, "bold"),
                bg="#00ff00",
                fg="#1a1a2e",
                activebackground="#00cc00",
                activeforeground="#1a1a2e",
                bd=0,
                padx=30,
                pady=12,
                cursor="hand2",
                command=self.check_answer
            )
            submit_btn.pack(pady=30)

        else:
            self.show_results()

    def check_answer(self):
        if self.selected_answer.get() == -1:
            messagebox.showwarning("No Selection", "Please select an answer!")
            return

        correct_answer = self.questions[self.current_question]["answer"]

        if self.selected_answer.get() == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct! ✓", "Great job! That's the right answer!")
        else:
            correct_option = self.questions[self.current_question]["options"][correct_answer]
            messagebox.showerror("Incorrect ✗", f"Correct answer:\n{correct_option}")

        self.current_question += 1
        self.show_question()

    def show_results(self):
        self.clear_screen()

        tk.Label(
            self.main_frame,
            text="🎉 Quiz Completed! 🎉",
            font=("Arial", 32, "bold"),
            bg="#1a1a2e",
            fg="#00d4ff"
        ).pack(pady=40)

        tk.Label(
            self.main_frame,
            text=f"Your Score: {self.score}/{len(self.questions)}",
            font=("Arial", 24, "bold"),
            bg="#1a1a2e",
            fg="#ffcc00"
        ).pack(pady=20)

        tk.Button(
            self.main_frame,
            text="PLAY AGAIN",
            font=("Arial", 18, "bold"),
            bg="#00ff00",
            fg="#1a1a2e",
            padx=30,
            pady=12,
            bd=0,
            cursor="hand2",
            command=self.create_start_screen
        ).pack(pady=20)

        tk.Button(
            self.main_frame,
            text="EXIT",
            font=("Arial", 18, "bold"),
            bg="#ff4d4d",
            fg="#1a1a2e",
            padx=30,
            pady=12,
            bd=0,
            cursor="hand2",
            command=self.root.quit
        ).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()