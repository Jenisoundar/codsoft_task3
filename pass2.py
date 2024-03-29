import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.label_username = tk.Label(master, text="Username:")
        self.label_username.grid(row=0, column=0, padx=10, pady=10)

        self.entry_username = tk.Entry(master)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        self.label_id = tk.Label(master, text="ID:")
        self.label_id.grid(row=1, column=0, padx=10, pady=10)

        self.entry_id = tk.Entry(master)
        self.entry_id.grid(row=1, column=1, padx=10, pady=10)

        self.label_length = tk.Label(master, text="Password Length:")
        self.label_length.grid(row=2, column=0, padx=10, pady=10)

        self.entry_length = tk.Entry(master)
        self.entry_length.grid(row=2, column=1, padx=10, pady=10)

        self.button_generate = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.button_generate.grid(row=3, columnspan=2, padx=10, pady=10)

        self.label_generated_password = tk.Label(master, text="")
        self.label_generated_password.grid(row=4, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        username = self.entry_username.get()
        user_id = self.entry_id.get()
        password_length = int(self.entry_length.get())

        if password_length <= 0:
            self.label_generated_password.config(text="Invalid length")
            return

        password_characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(password_characters) for i in range(password_length))

        generated_password_with_info = f"Username: {username}\nID: {user_id}\nPassword: {generated_password}"
        self.label_generated_password.config(text=generated_password_with_info)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
