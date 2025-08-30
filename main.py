import tkinter as tk
from tkinter import messagebox


cont_persona = 0
cont_g1 = 0
cont_g2 = 0
cont_n = 0
suma_imc = 0

def calcular_imc():
    global cont_persona, cont_g1, cont_g2, cont_n, suma_imc

    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        if altura <= 0:
            messagebox.showerror("Error", "La altura debe ser mayor que 0")
            return

        imc = peso / (altura ** 2)
        cont_persona += 1
        suma_imc += imc

        if imc < 17:
            categoria = "Infrapeso"
        elif 17 <= imc < 18:
            categoria = "Bajo peso"
        elif 18 <= imc < 25:
            categoria = "Peso normal"
            cont_n += 1
        elif 25 <= imc < 30:
            categoria = "Obesidad grado I"
            cont_g1 += 1
        elif 30 <= imc < 35:
            categoria = "Obesidad grado II"
            cont_g2 += 1
        else:
            categoria = "Obesidad grado III"

        messagebox.showinfo("Resultado", f"Tu IMC es {imc:.2f}\nCategoría: {categoria}")
        actualizar_estadisticas()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

def actualizar_estadisticas():
    if cont_persona > 0:
        promedio_imc = suma_imc / cont_persona
        porcentaje_n = (cont_n * 100) / cont_persona
        lbl_stats.config(text=f"""
        Personas ingresadas: {cont_persona}
        Peso normal: {cont_n} ({porcentaje_n:.2f}%)
        Obesidad Grado I: {cont_g1}
        Obesidad Grado II: {cont_g2}
        Promedio IMC: {promedio_imc:.2f}
        """)
    else:
        lbl_stats.config(text="Sin datos aún.")


root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("400x400")
root.config(bg="#f4f4f9")


tk.Label(root, text="Peso (kg):", bg="#f4f4f9", font=("Arial", 12)).pack(pady=5)
entry_peso = tk.Entry(root, font=("Arial", 12))
entry_peso.pack(pady=5)

tk.Label(root, text="Altura (m):", bg="#f4f4f9", font=("Arial", 12)).pack(pady=5)
entry_altura = tk.Entry(root, font=("Arial", 12))
entry_altura.pack(pady=5)

btn_calcular = tk.Button(root, text="Calcular IMC", command=calcular_imc, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
btn_calcular.pack(pady=20)


lbl_stats = tk.Label(root, text="Sin datos aún.", bg="#f4f4f9", justify="left", font=("Arial", 10))
lbl_stats.pack(pady=10)

root.mainloop()
