import tkinter as tk
from tkinter import ttk
from urllib.parse import urlparse


def generate_password():
    url = url_entry.get()
    base_password = base_password_entry.get()

    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split(".")[0]

    first_three = domain[:3].capitalize()

    generated_password = f"{first_three}{base_password}!!"

    generated_password_label.config(
        text=f"Generated Password: {generated_password}")


root = tk.Tk()
root.title("Password Generator")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 14))
style.configure("TButton", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

url_label = ttk.Label(root, text="URL 입력:")
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = ttk.Entry(root)
url_entry.grid(row=0, column=1, padx=10, pady=10)

base_password_label = ttk.Label(root, text="기본 비밀번호 입력:")
base_password_label.grid(row=1, column=0, padx=10, pady=10)

base_password_entry = ttk.Entry(root, show="*")
base_password_entry.grid(row=1, column=1, padx=10, pady=10)

generate_button = ttk.Button(
    root, text="비밀번호 생성", command=generate_password)
generate_button.grid(row=2, columnspan=2, pady=10)

generated_password_label = ttk.Label(root, text="생성된 비밀번호: ")
generated_password_label.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
