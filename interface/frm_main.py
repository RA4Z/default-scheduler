import tkinter as tk
from tkinter import messagebox
import sys
import os
config_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(config_dir)

from services.language_dict import Language
from config.firebase import Firebase

if __name__ != "__main__": from interface.frm_history import History

class Application(tk.Tk):
    def __init__(self, automation_name:str, automation_description:str, automation_developer:str, automation_requester:str, columns, language:str):
        super().__init__()
        self.idiom = language
        self.language = Language(language)
        self.country_image = tk.PhotoImage(file=f"images/{language}.png")
        self.logo_image = tk.PhotoImage(file=f"images/logo.png")
        self.automation_name = automation_name
        self.automation_description = automation_description
        self.automation_developer = automation_developer
        self.automation_requester = automation_requester
        self.columns = columns
        self.title(self.automation_name)
        self.result = False
        self.firebase = Firebase()

        self.components_styles()
        self.components_position()
    
    # Declare the components styles
    def components_styles(self):
        self.title_label = tk.Label(self, text=f"{self.language.search('greeting').replace('$automation_name',self.automation_name)}", font=("Helvetica", 18, "bold"), wraplength=800)
        self.buttons_frame = tk.Frame(self)
        self.exec_history = tk.Button(self.buttons_frame, text=self.language.search('exec_history'), font=("Helvetica", 15, "bold"), command=self.exec_hist)
        self.run_button = tk.Button(self.buttons_frame, text=self.language.search('run_script'), font=("Helvetica", 15, "bold"), command=self.run_script)
        self.automation_label = tk.Label(self, text=self.automation_description, wraplength=500, font=("Helvetica", 14))

        self.bottom_frame = tk.Frame(self)
        self.automation_credits = tk.Label(self.bottom_frame, text=f"{self.automation_name}, {self.language.search('requested')} {self.automation_requester} {self.language.search('developed')} {self.automation_developer}", wraplength=1000, font=("Helvetica", 12, 'bold'), fg='#0078D7')
        if self.idiom == 'PT': self.quick_tips = tk.Label(self.bottom_frame, text=self.firebase.get_tips_or_news()[self.idiom], wraplength=800, font=("Helvetica", 10, 'bold'))

        self.columns_frame = tk.Frame(self)
        self.image_label = tk.Label(self, image=self.country_image)
        self.logo_label = tk.Label(self, image=self.logo_image)

    # Put the components into the Application interface
    def components_position(self):
        self.bottom_frame.pack(side="bottom",pady=5)
        self.automation_credits.pack()
        if self.idiom == 'PT': self.quick_tips.pack()

        self.title_label.place(relx=0.5, rely=0.05, anchor="center")
        self.buttons_frame.pack(side='bottom',pady=25)
        self.exec_history.pack(side='left',padx=10)
        self.run_button.pack(side='left',padx=10)
        self.logo_label.pack(side="top", anchor="nw")
        self.image_label.pack(side="right")

        self.columns_frame.pack(side="left",pady=100)
        self.data = []
        for column in self.columns:
            individual_column = tk.Frame(self.columns_frame)
            subtitle_label = tk.Label(individual_column, text=column, font=("Helvetica", 12, "bold"), wraplength=250)
            text_field = tk.Text(individual_column, height=30, width=20)
            self.data.append({'column_name':column,'text':text_field})
            individual_column.pack(side="left", padx=10)
            subtitle_label.pack()
            text_field.pack()

        self.automation_label.pack(pady=120, padx=50)
        self.update_idletasks()
        self.geometry(f"{self.winfo_reqwidth() + 50}x{self.winfo_reqheight() + 50}")

    def exec_hist(self):
        hist = History(self.automation_name, self.automation_developer, self.automation_requester,self.idiom)
        hist.mainloop()
        pass

    def run_script(self):
        if self.columns != []:
            if str(self.data[0]['text'].get("1.0", tk.END)).strip() == '':
                messagebox.showerror(title=f"{self.language.search('empty_title')}",message=f"{self.language.search('empty_body')}")
                return
            desired_rows = len(str(self.data[0]['text'].get("1.0", tk.END)).split('\n')[:-1])
        else:
            desired_rows = 1
        mid_time = self.firebase.get_mid_time(self.automation_name,desired_rows)

        if mid_time != None: 
            text_mid = f"{self.language.search('aproximately')} {mid_time}"
        else:
            text_mid = ''

        self.option_selected = messagebox.askquestion(title=f"{self.language.search('run_script')}", message=f"{self.language.search('run_sure')} {text_mid}")
        if self.option_selected == 'yes':
            for i in range(len(self.data)):
                self.data[i]['text'] = self.data[i]['text'].get("1.0", tk.END)
            self.result = True
            self.destroy()

if __name__ == "__main__":
    from frm_history import History
    app = Application('Python Default Script',
                      'Graphical interface model developed in Tkinter by Robert Aron Zimmermann, an interface was developed to be used as a basis in the development of other automations that are interactive with SAP, the entire algorithm was developed in Python with the intention of facilitating interaction between Developer/ SAP, thus developing high quality automation in a short period of time with several error treatments. Doubts or Suggestions contact Robert Aron Zimmermann robertn@weg.net',
                      'Robert Aron Zimmermann', 'Robert Aron Zimmermann', ['Test1', 'Test2', 'Test3', 'Test4'],'EN')
    app.mainloop()
