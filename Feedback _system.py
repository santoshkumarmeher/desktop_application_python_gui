import tkinter as tk
from tkinter import messagebox
import pandas as pd
from openpyxl import load_workbook
import customtkinter


def center_window(app, width, height):
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x_position = (screen_width - width) // 2
    y_position = (screen_height - height) // 2

    app.geometry(f"{width}x{height}+{x_position}+{y_position}")


def create_boxes():
    app = customtkinter.CTk()
    app.title("Feedback Form")
    def save_feedback():
        if full_name_entry.get() == "":
            messagebox.showwarning("Incomplete Form", "Name field is mandatory. Please fill it.")
        else:
            full_name = full_name_entry.get()
            email_id = email_entry.get()
            age = age_entry.get()
            feedback = feedback_dropdown.get()
            data = {'Full Name': [full_name], 'Email ID': [email_id], 'Age': [age], 'Feedback': [feedback]}
            df = pd.DataFrame(data)

            try:
                existing_df = pd.read_excel('feedback_data.xlsx', sheet_name='FeedbackData')
                updated_df = pd.concat([existing_df, df], ignore_index=True)
                updated_df.to_excel('feedback_data.xlsx', index=False, sheet_name='FeedbackData', engine='openpyxl')
                
            except FileNotFoundError:
                df.to_excel('feedback_data.xlsx', index=False, sheet_name='FeedbackData', engine='openpyxl')
            messagebox.showinfo("Submitted", "Thank you for your valuable feedback !")
        full_name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)


    customtkinter.CTkLabel(app, text="We Value Your Feedback",font=("",20)).grid(row=0, column=1, columnspan=3, sticky=tk.W, padx=70,pady=30)
    customtkinter.CTkLabel(app, text="Full Name:").grid(row=1, column=0, sticky=tk.W, padx=50, pady=5)
    customtkinter.CTkLabel(app, text="Email ID:").grid(row=2, column=0, sticky=tk.W, padx=50, pady=5)
    customtkinter.CTkLabel(app, text="Age:").grid(row=3, column=0, sticky=tk.W, padx=50, pady=5)
    customtkinter.CTkLabel(app, text="Feedback:").grid(row=3, column=2, sticky=tk.W, padx=10, pady=5)

    full_name_entry = customtkinter.CTkEntry(app,width=350)
    full_name_entry.grid(row=1, column=1, padx=10, pady=5,columnspan=3)
    email_entry = customtkinter.CTkEntry(app,width=350)
    email_entry.grid(row=2, column=1, padx=10, pady=5,columnspan=3)
    age_entry = customtkinter.CTkEntry(app,width=90)
    age_entry.grid(row=3, column=1, padx=10, pady=5)
    
    feedback_options = ["Excellent", "Good", "Average", "Poor"]
    feedback_dropdown = customtkinter.CTkComboBox(app,values=feedback_options,width=150)
    feedback_dropdown.grid(row=3, column=3, padx=10, pady=5)

    save_button = customtkinter.CTkButton(app, text="Submit", command=save_feedback)
    save_button.grid(row=4, column=3,pady=10)


    center_window(app, 600, 300)
    app.mainloop()
create_boxes()