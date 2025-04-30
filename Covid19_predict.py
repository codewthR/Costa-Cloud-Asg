from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import random


root = Tk()
root.title("COVID-19 Risk Prediction")
root.geometry("550x700")


root.minsize(500,600)
root.maxsize(600,700)
# root.configure(bg="#f0f4f7")


style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 11))
style.configure("TButton", font=("Helvetica", 20), padding=6)
style.configure("TCombobox", font=("Helvetica", 11))


main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill="both", expand=True)


inputs = {}   


def update_fields(*args):
    # Patient Type Logic
    if inputs["Patient Type"].get() == "Not Hospitalized":
        inputs["Intubed"].set("Does not apply")
        intubed_combo.config(state="disabled")
        inputs["ICU"].set("Does not apply")
        icu_combo.config(state="disabled")
    else:
        intubed_combo.config(state="readonly")
        if inputs["Intubed"].get() == "Does not apply":
            inputs["Intubed"].set("No")
        icu_combo.config(state="readonly")
        if inputs["ICU"].get() == "Does not apply":
            inputs["ICU"].set("No")

  
    if inputs["Sex"].get() == "Male":
        inputs["Pregnancy"].set("Does not apply")
        pregnancy_combo.config(state="disabled")
    else:
        pregnancy_combo.config(state="readonly")
        if inputs["Pregnancy"].get() == "Does not apply":
            inputs["Pregnancy"].set("No")


def predict():
    chance = random.randint(1, 100)
    messagebox.showinfo("Prediction Result", f"{chance}% chance of you being COVID Positive (+ve)")


def create_labeled_dropdown(parent, label_text, options, default, row):
    ttk.Label(parent, text=label_text).grid(row=row, column=0, sticky='w', padx=5, pady=5)
    var = tk.StringVar(value=default)
    combo = ttk.Combobox(parent, textvariable=var, values=options, state="readonly", width=25)
    combo.grid(row=row, column=1, sticky='w', padx=5, pady=5)
    inputs[label_text] = var
    return combo


# tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky='w')

ttk.Label(main_frame, text="Age").grid(row=0, column=0, sticky='w', padx=5, pady=5)
age_var = tk.StringVar()
ttk.Entry(main_frame, textvariable=age_var, width=27).grid(row=0, column=1, sticky='w', padx=5, pady=5)
inputs["Age"] = age_var


dropdowns = [
    ("Sex", ["Male", "Female"], "Female"),
    ("Patient Type", ["Hospitalized", "Not Hospitalized"], "Not Hospitalized"),
    ("Intubed", ["Yes", "No", "Does not apply"], "No"),
    ("Pneumonia", ["Yes", "No"], "No"),
    ("Pregnancy", ["Yes", "No", "Does not apply"], "No"),
    ("Diabetes", ["Yes", "No"], "No"),
    ("COPD", ["Yes", "No"], "No"),
    ("Asthma", ["Yes", "No"], "No"),
    ("INMSUPR", ["Yes", "No"], "No"),
    ("Hypertension", ["Yes", "No"], "No"),
    ("Other Disease", ["Yes", "No"], "No"),
    ("Cardiovascular", ["Yes", "No"], "No"),
    ("Obesity", ["Yes", "No"], "No"),
    ("Renal Chronic", ["Yes", "No"], "No"),
    ("Tobacco", ["Yes", "No"], "No"),
    ("Contact with other COVID patient", ["Yes", "No"], "No"),
    ("ICU", ["Yes", "No", "Does not apply"], "No"),
]


combos = {}
for i, (label, options, default) in enumerate(dropdowns):

    # print(f"{i}, {label}, {options}, {default}")
    combo = create_labeled_dropdown(main_frame, label, options, default, int(i)+1)
    combos[label] = combo


intubed_combo = combos["Intubed"]
icu_combo = combos["ICU"]
pregnancy_combo = combos["Pregnancy"]


inputs["Sex"].trace_add("write", update_fields)
inputs["Patient Type"].trace_add("write", update_fields)


ttk.Button(main_frame, text="Predict", command=predict).grid(row=len(dropdowns) + 2, column=0, columnspan=2, pady=20)
update_fields()
root.mainloop()
