import subprocess

class console_out:
    def __init__(self, text) -> None:
        self.text = text

    def console_output(self):
        return ("white", f"{self.text = }")