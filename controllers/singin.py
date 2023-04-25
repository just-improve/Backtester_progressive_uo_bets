
class SignInController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["signin"]
        self._bind()

    def _bind(self):
        self.frame.si_home_btn.config(command=self.go_to_home)
        self.frame.si_sign_out_btn.config(command=self.go_to_sign_up)

    def go_to_home(self):
        self.view.switch("home")

    def go_to_sign_up(self):
        self.view.switch("signup")
