class SignUpController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["signup"]
        self._bind()

    def _bind(self):
        self.frame.su_sign_in_btn.config(command=self.go_to_sign_in)
        self.frame.su_home_btn.config(command=self.go_to_home)

    def go_to_sign_in(self):
        self.view.switch("signin")

    def go_to_home(self):
        self.view.switch("home")


    def store_inputs(self):
        data = {
            "fullname": self.frame.fullname_input.get(),
            "username": self.frame.username_input.get(),
            "password": self.frame.password_input.get(),
            "has_agreed": self.frame.has_agreed.get(),
        }