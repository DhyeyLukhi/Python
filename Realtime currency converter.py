import requests
import tkinter as tk
from tkinter import ttk


class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = CurrencyConverter(url)


def main():
    root = tk.Tk()
    root.title("Currency Converter")
    root.geometry("400x200")

    # Define labels and entry boxes for user input
    amount_label = ttk.Label(root, text="Amount:")
    amount_label.grid(row=0, column=0, padx=5, pady=5)
    amount_entry = ttk.Entry(root)
    amount_entry.grid(row=0, column=1, padx=5, pady=5)

    from_label = ttk.Label(root, text="From:")
    from_label.grid(row=1, column=0, padx=5, pady=5)
    from_box = ttk.Combobox(root, values=list(converter.currencies.keys()))
    from_box.current(0)
    from_box.grid(row=1, column=1, padx=5, pady=5)

    to_label = ttk.Label(root, text="To:")
    to_label.grid(row=2, column=0, padx=5, pady=5)
    to_box = ttk.Combobox(root, values=list(converter.currencies.keys()))
    to_box.current(0)
    to_box.grid(row=2, column=1, padx=5, pady=5)

    result_label = ttk.Label(root, text="Result:")
    result_label.grid(row=3, column=0, padx=5, pady=5)
    result_entry = ttk.Entry(root, state="readonly")
    result_entry.grid(row=3, column=1, padx=5, pady=5)

    # Define the function that will handle the conversion and update the result
    def convert_currency():
        from_curr = from_box.get()
        to_curr = to_box.get()
        amount = float(amount_entry.get())
        converted_amount = converter.convert(from_curr, to_curr, amount)
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, converted_amount)
        result_entry.config(state="readonly")

    # Define the "Convert" button and bind it to the conversion function
    convert_button = ttk.Button(root, text="Convert", command=convert_currency)
    convert_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()