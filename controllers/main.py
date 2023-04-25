from models.main import Model
from views.main import View
from .home import HomeController
from .singin import SignInController
from .singup import SignUpController


class Controller:
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model
        self.signin_controller = SignInController(model, view)
        self.signup_controller = SignUpController(model, view)
        self.home_controller = HomeController(model, view)

    def start(self):
        # self.model.auth.load_auth_state()
        # self.view.switch("home")

        # self.view.switch("signin")

        self.view.start_mainloop()