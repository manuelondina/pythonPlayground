##############################################
###      Please remember to install        ###
###      all the libs needed for           ###
###      this to work properly.            ###
###                                        ###     
###      w/Love -- Manuel Ondina           ###
##############################################

import PyPDF2
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import docx
import requests
from io import BytesIO

def count_words_pdf(pdf_file):
    with open(pdf_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        num_pages = len(pdf_reader.pages)
        count = 0
        for i in range(num_pages):
            page = pdf_reader.pages[i]
            text = page.extract_text()
            count += len(text.split())
    return count



def count_words_docx(docx_file):
    doc = docx.Document(docx_file)
    count = 0
    for para in doc.paragraphs:
        count += len(para.text.split())
    return count

def browse_file():
    filename = filedialog.askopenfilename()
    file_ext = filename.split(".")[-1]
    file_label.config(text=filename)
    if file_ext == "pdf":
        word_count = count_words_pdf(filename)
        word_count_label.config(text=f"Word Count: {word_count}")
    elif file_ext == "docx":
        word_count = count_words_docx(filename)
        word_count_label.config(text=f"Word Count: {word_count}")
    else:
        word_count_label.config(text="File type not supported")

root = tk.Tk()
root.title("Word Count")
root.geometry("560x150")

response = requests.get("https://cdn-icons-png.flaticon.com/512/4002/4002506.png", verify=False)
icon_data = response.content
icon = tk.PhotoImage(data=icon_data)

root.iconphoto(True, icon)

style = ttk.Style()
style.configure("Modern.TButton", padding=10, background="#2edd71", foreground="black", font=('Segoe UI', 12))

browse_button = ttk.Button(root, text="Browse File", command=browse_file, style="Modern.TButton")
browse_button.pack(pady=10)

file_label = tk.Label(root, text="No file selected.")
file_label.pack()

word_count_label = tk.Label(root, text="Word Count: 0")
word_count_label.pack(pady=10)

root.mainloop()