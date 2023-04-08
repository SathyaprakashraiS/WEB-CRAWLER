#base test
'''
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("First_Program")
label = Label(root, text ="Hello World !").pack()
root.mainloop()

'''

import tkinter as tk

class ScrollableText(tk.Frame):
    def __init__(self, master, text="", *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)
        
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        
        self.paragraph = tk.Label(self.scrollable_frame, text=text, wraplength=450)
        self.paragraph.pack(fill="both", padx=20, pady=10)

class InputLoader(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.input_label = tk.Label(self, text="Enter your text here:")
        self.input_entry = tk.Entry(self, width=50)
        self.submit_button = tk.Button(self, text="Submit", command=self.load_paragraph)
        
        self.input_label.pack(pady=10)
        self.input_entry.pack(pady=10)
        self.submit_button.pack(pady=10)
    
    def load_paragraph(self):
        input_text = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        
        text_frame = ScrollableText(root, text=input_text)
        text_frame.pack(fill="both", expand=True)

root = tk.Tk()
root.title("Input and Loader")

input_loader = InputLoader(root)
input_loader.pack(fill="both", expand=True)

root.mainloop()


'''
#working best test
import tkinter as tk
import time

def submit_input():
    user_input = entry.get()  # get the user input
    #entry.delete(0, tk.END)  # clear the input field
    entry.config(state="disabled")
    button.config(state="disabled")
    sentence_label.config(text="Loading...")  # update label text
    root.after(2000, lambda: display_sentence(user_input))  # wait for 2 seconds and display the sentence
    #sentence_label.config(text="ithu thanda text :)")

def display_sentence(user_input):
    # do some processing with the user input
    #sentence = f"The input was: {user_input}"
    #label.config(text=sentence)  # update label text
    content=f"ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input} ithu thanda text :) and your input was {user_input}"
    sentence_label.config(text=content,wraplength=200)

root = tk.Tk()
root.geometry("400x300")
root.title("Input and Load Example")

label = tk.Label(root, text="Enter some input:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=submit_input)
button.pack()

sentence_label = tk.Label(root, text="")
sentence_label.pack()

root.mainloop()
'''

#test3
'''
import tkinter as tk
import time

def display_sentence():
    # This function will display the sentence after some time
    sentence_label.config(text="This is the sentence to display!")

def submit_input():
    # This function will be called when the user clicks the "Submit" button
    input_text = input_entry.get()
    print("User input:", input_text)
    # Disable the input field and submit button
    input_entry.config(state="disabled")
    submit_button.config(state="disabled")
    # Display a message to indicate that the program is processing
    processing_label.config(text="Processing...")
    # Wait for some time before displaying the sentence
    time.sleep(2)
    # Display the sentence
    display_sentence()
    

# Create the main window
window = tk.Tk()
window.title("Input Window")

# Create the input field and submit button
input_label = tk.Label(window, text="Enter some input:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()
submit_button = tk.Button(window, text="Submit", command=submit_input)
submit_button.pack()

# Create a label to indicate that the program is processing
processing_label = tk.Label(window, text="")
processing_label.pack()

# Create a label to display the sentence
sentence_label = tk.Label(window, text="")
sentence_label.pack()

# Start the main loop
window.mainloop()
'''