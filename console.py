import tkinter as tk
from console_out import console_out

class ConsoleApp:
    def __init__(self, root):
        self.console = root
        self.console.title("Console")
        self.console.geometry("800x500")
        self.console.config(bg=DEFAULT_COLOR)

        self.create_widgets()

    def create_widgets(self):
        # Create a Text widget to display text
        self.output_text = tk.Text(self.console)
        self.output_text.pack(side=tk.TOP, fill="both", expand=True)
        self.output_text.config(state=tk.DISABLED, bg=DEFAULT_COLOR, font=DEFAULT_FONT, fg=FONT_COLOR)  # Set font color
        
        # Create an Entry widget for text input
        self.text = tk.Entry(self.console, bg=DEFAULT_COLOR, font=DEFAULT_FONT, fg=FONT_COLOR)  # Set font color
        self.text.pack(side=tk.BOTTOM, fill="both")

        # Remove the white borders around the input text widget
        self.text.config(highlightthickness=0, highlightbackground=DEFAULT_COLOR)

        self.text.bind("<Return>", self.display_text)

    def display_text(self, event):
        if self.text.get() == "clear":
            self.clear_console()
            self.text.delete(0, tk.END)
            return

        info = console_out(self.text.get()).console_output()
        
        text = info[1]
        color = info[0]

        print(f"DEBUG: {text = }, {color = }, {self.text.get() = }")
        
        self.output_text.config(state=tk.NORMAL, fg=color)  # Set font color
        self.output_text.insert(tk.END, str(text) + "\n")
        self.output_text.config(state=tk.DISABLED)

        self.output_text.see(tk.END)
        
        self.text.delete(0, tk.END)  # Clear the input text box

    def clear_console(self):
        self.output_text.config(state=tk.NORMAL) 
        self.output_text.delete(1.0, tk.END) 
        self.output_text.config(state=tk.DISABLED)  

if __name__ == "__main__":
    DEFAULT_COLOR = "#404040"
    DEFAULT_FONT = ("Tahoma", 10)
    FONT_COLOR = "white"  # Change this to your desired font color
    
    console = tk.Tk()
    app = ConsoleApp(console)
    console.mainloop()
