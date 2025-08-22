import tkinter as tk
import random


answers = [
    "Yes, definitely.",
    "Without a doubt.",
    "Ask again later.",
    "Better not tell you now.",
    "Don't count on it.",
    "My reply is no.",
    "Outlook not so good.",
    "Signs point to yes."
]


def get_answer():
    response = random.choice(answers)
    result_label.config(text=response)


root = tk.Tk()
root.title("Magic 8 Ball 🎱")
root.geometry("400x300")
root.config(bg="black")


title_label = tk.Label(root, text="Ask the Magic 8 Ball", font=("Arial", 16, "bold"), fg="white", bg="black")
title_label.pack(pady=10)

question_entry = tk.Entry(root, font=("Arial", 14), width=30)
question_entry.pack(pady=10)


ask_button = tk.Button(root, text="Ask 🎱", font=("Arial", 14, "bold"), bg="purple", fg="white", command=get_answer)
ask_button.pack(pady=10)


result_label = tk.Label(root, text="", font=("Arial", 14, "italic"), fg="cyan", bg="black", wraplength=350)
result_label.pack(pady=20)


root.mainloop()
