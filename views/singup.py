from tkinter import Frame, Label, Entry, Checkbutton, Button, BooleanVar


class SignUpView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.has_agreed = BooleanVar()
        self.agreement = Checkbutton(
            self,
            text="I've agreed to the Terms & Conditions",
            variable=self.has_agreed,
            onvalue=True,
            offvalue=False,
        )
        self.agreement.grid(row=4, column=1, padx=0, sticky="w")

        self.su_sign_in_btn = Button(self, text="Go to sign in")
        self.su_sign_in_btn.grid(row=5, column=1, padx=0, pady=10, sticky="w")

        self.su_home_btn = Button(self, text="Go to home")
        self.su_home_btn.grid(row=7, column=1, sticky="w")