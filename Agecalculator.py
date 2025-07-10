import tkinter as tk
from datetime import date


def calculate_age():
    today = date.today()
    birth_date = date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    result_label.config(text=f"You are {age} years old.")


# Create a tkinter window
window = tk.Tk()
window.title("Age Calculator")

# Add labels and input fields
tk.Label(window, text="Day").grid(row=0, column=0)
day_entry = tk.Entry(window)
day_entry.grid(row=0, column=1)

tk.Label(window, text="Month").grid(row=1, column=0)
month_entry = tk.Entry(window)
month_entry.grid(row=1, column=1)

tk.Label(window, text="Year").grid(row=2, column=0)
year_entry = tk.Entry(window)
year_entry.grid(row=2, column=1)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2)

# Add a button to trigger age calculation
calculate_button = tk.Button(window, text="Calculate Age", command=calculate_age)
calculate_button.grid(row=4, column=0, columnspan=2)

window.mainloop()
