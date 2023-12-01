import tkinter as tk
from tkinter import ttk
import pandas as pd
from openpyxl import load_workbook

def save_feedback():
    full_name = full_name_entry.get()
    email_id = email_entry.get()
    age = age_entry.get()
    feedback = feedback_var.get()

    data = {'Full Name': [full_name], 'Email ID': [email_id], 'Age': [age], 'Feedback': [feedback]}
    df = pd.DataFrame(data)

    try:
        existing_df = pd.read_excel('feedback_data.xlsx', sheet_name='FeedbackData')
        updated_df = pd.concat([existing_df, df], ignore_index=True)
        updated_df.to_excel('feedback_data.xlsx', index=False, sheet_name='FeedbackData', engine='openpyxl')
    except FileNotFoundError:

        df.to_excel('feedback_data.xlsx', index=False, sheet_name='FeedbackData', engine='openpyxl')

    full_name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Feedback Form")

tk.Label(root, text="Full Name:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
tk.Label(root, text="Email ID:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
tk.Label(root, text="Age:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
tk.Label(root, text="Feedback:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)

full_name_entry = tk.Entry(root)
full_name_entry.grid(row=0, column=1, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5)

feedback_var = tk.StringVar()
feedback_options = ["Excellent", "Good", "Average", "Poor"]
feedback_dropdown = ttk.Combobox(root, textvariable=feedback_var, values=feedback_options)
feedback_dropdown.grid(row=3, column=1, padx=10, pady=5)

save_button = tk.Button(root, text="Save Feedback", command=save_feedback)
save_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
