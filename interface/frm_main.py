import tkinter as tk
import getpass

class Application(tk.Tk):
    def __init__(self, automation_name, automation_description, automation_developer, automation_requester):
        super().__init__()
        self.automation_name = automation_name
        self.automation_description = automation_description
        self.automation_developer = automation_developer
        self.automation_requester = automation_requester
        self.title(self.automation_name)
        self.geometry("1000x750")

        self.components_styles()
        self.components_position()
    
    # Declare the components styles
    def components_styles(self):
        self.title_label = tk.Label(self, text=f"Welcome to {self.automation_name}, {getpass.getuser().upper()}", font=("Helvetica", 18, "bold"), wraplength=800)
        self.run_button = tk.Button(self, text="Run Automation", font=("Helvetica", 15, "bold"))
        self.subtitle_label = tk.Label(self, text="Example of a Data Column", font=("Helvetica", 12, "bold"), wraplength=250)
        self.text_field = tk.Text(self, height=30, width=25)
        self.automation_label = tk.Label(self, text=self.automation_description, wraplength=500, font=("Helvetica", 12))
        self.automation_credits = tk.Label(self, text=f'{self.automation_name}, requested by {self.automation_requester} and developed by {self.automation_developer}', wraplength=1000, font=("Helvetica", 12, 'bold'), fg='#0078D7')

    # Put the components into the Application interface
    def components_position(self):
        self.title_label.place(relx=0.5, rely=0.05, anchor="center")
        self.run_button.place(relx=0.90, rely=0.90, anchor="se")
        self.subtitle_label.place(relx=0.1, rely=0.1)
        self.text_field.place(relx=0.1, rely=0.15)
        self.automation_label.place(relx=0.4, rely=0.15)
        self.automation_credits.pack(pady=5, side="bottom")
        

if __name__ == "__main__":
    app = Application('Python Default Script',
                      'Description of the Automation generated with my own creativity during testing this Automation... Description of the Automation generated with my own creativity during testing this Automation... Description of the Automation generated with my own creativity during testing this Automation... Description of the Automation generated with my own creativity during testing this Automation... Description of the Automation generated with my own creativity during testing this Automation...',
                      'Robert Aron Zimmermann', 'Robert Aron Zimmermann')
    app.mainloop()
