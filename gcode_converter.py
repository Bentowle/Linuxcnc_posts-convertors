#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog

def replace_m6_m06_with_m600(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        # Replace M6 or M06 with M600
        modified_content = content.replace('M6', 'M600').replace('M06', 'M600')

        with open(file_path, 'w') as file:
            file.write(modified_content)

        print(f"Conversion successful: {file_path}")

    except Exception as e:
        print(f"Error: {e}")

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("G-code files", "*.txt;*.ngc;*.nc")])
    if file_path:
        replace_m6_m06_with_m600(file_path)

# Create a simple GUI
root = tk.Tk()
root.title("G-code Converter")

button = tk.Button(root, text="Choose G-code File", command=choose_file)
button.pack(padx=20, pady=20)

root.mainloop()
