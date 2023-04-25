from .root import Root
from .home import HomeView
from .singin import SignInView
from .singup import SignUpView

class View:
    def __init__(self):
        self.root = Root()
        self.frames = {}

        self._add_frame(SignUpView, "signup")
        self._add_frame(SignInView, "signin")
        self._add_frame(HomeView, "home")

    def _add_frame(self, Frame, name):
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self):
        self.root.mainloop()



# delete robi
#
#
# from .root import Root
# from .home import HomeView
# from .signin import SignInView
# from .signup import SignUpView
#
# class View:
#     def __init__(self):
#         self.root = Root()
#         self.frame_classes = {
#             "signin": SignInView,
#             "signup": SignUpView,
#             "home": HomeView,
#         }
#         self.current_frame = None
#
#     def switch(self, name):
#         new_frame = self.frame_classes[name](self.root)
#         if self.current_frame is not None:
#             self.current_frame.destroy()
#         self.current_frame = new_frame
#         self.current_frame.grid(row=0, column=0, sticky="nsew")
#
#     def start_mainloop(self):
#         self.root.mainloop()