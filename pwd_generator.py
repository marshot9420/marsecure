import tkinter as tk
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

url_label = tk.Label(root, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

base_password_label = tk.Label(root, text="Enter Base Password:")
base_password_label.pack()

base_password_entry = tk.Entry(root, show="*")
base_password_entry.pack()

generate_button = tk.Button(
    root, text="Generate Password", command=generate_password)
generate_button.pack()

generated_password_label = tk.Label(root, text="Generated Password: ")
generated_password_label.pack()

root.mainloop()
