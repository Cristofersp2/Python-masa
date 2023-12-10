import tkinter as tk
import math

def kilos_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilos(lb):
    return lb / 2.20462

def convert():
    option = var.get()
    if option == 1:
        kg = float(entry.get())
        result = kilos_to_pounds(kg)
        resultado.set(f"{kg} kilograms is equal to {result:.2f} pounds")
    elif option == 2:
        lb = float(entry.get())
        result = pounds_to_kilos(lb)
        resultado.set(f"{lb} pounds is equal to {result:.2f} kilograms")

window = tk.Tk()
window.title("Mass Converter")

label = tk.Label(window, text="Select an option:")
label.grid(row=0, column=0, padx=10, pady=10)

var = tk.IntVar()
radio_kg_to_lb = tk.Radiobutton(window, text="Kilos to Pounds", variable=var, value=1)
radio_lb_to_kg = tk.Radiobutton(window, text="Pounds to Kilos", variable=var, value=2)
radio_kg_to_lb.grid(row=1, column=0, padx=10, pady=5, sticky="w")
radio_lb_to_kg.grid(row=2, column=0, padx=10, pady=5, sticky="w")

label2 = tk.Label(window, text="Enter the mass:")
label2.grid(row=3, column=0, padx=10, pady=10)

entry = tk.Entry(window)
entry.grid(row=4, column=0, padx=10, pady=5)

button = tk.Button(window, text="Convert", command=convert)
button.grid(row=5, column=0, padx=10, pady=10)

resultado = tk.StringVar()
label3 = tk.Label(window, textvariable=resultado, font=("Arial", 12, "bold"))
label3.grid(row=6, column=0, padx=10, pady=10)


window.mainloop()