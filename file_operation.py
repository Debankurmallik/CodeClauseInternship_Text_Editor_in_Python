import tkinter as tk
from tkinter import filedialog, Text
import keyword


project = tk.Tk()
project.title("Simple Text Editor")


text_area = Text(project, wrap='word')
text_area.pack(expand=1, fill='both')


def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))


menu_bar = tk.Menu(project)
project.config(menu=menu_bar)


file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=project.quit)


def highlight_syntax(event=None):
    text = text_area.get(1.0, tk.END)
    for kw in keyword.kwlist:
        start_idx = '1.0'
        while True:
            start_idx = text_area.search(kw, start_idx, stopindex=tk.END)
            if not start_idx:
                break
            end_idx = f"{start_idx}+{len(kw)}c"
            text_area.tag_add(kw, start_idx, end_idx)
            text_area.tag_config(kw, foreground='blue')
            start_idx = end_idx

text_area.bind("<KeyRelease>", highlight_syntax)


def update_word_count(event=None):
    text = text_area.get(1.0, tk.END)
    word_count = len(text.split())
    project.title(f"Simple Text Editor - {word_count} Words")

text_area.bind("<KeyRelease>", update_word_count)


project.mainloop()
