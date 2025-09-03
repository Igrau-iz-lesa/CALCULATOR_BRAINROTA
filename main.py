import tkinter as tk
from tkinter import messagebox

def calculate_brainrot(bags, kpm, time):
    try:
        result = (kpm ** 2) / (bags * time * 0.1 + 1)
        return result
    except ZeroDivisionError:
        return 10000

def calculate():
    try:
        bags = int(bags_entry.get())
        kpm = int(kpm_entry.get())
        time_val = float(time_entry.get())

        if bags == 0:
            bags = 1

        result = calculate_brainrot(bags, kpm, time_val)
        result_label.config(text=f"Ваша доза брейнрота: {result:.2f}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа во все поля")


# Создаем главное окно с тёмным фоном
root = tk.Tk()
root.title("Калькулятор брейнрота")
root.geometry("400x300")
root.configure(bg='#333333')  # Тёмно-серый фон
root.iconbitmap('alesso.ico')

# Стиль для всех элементов
label_style = {'bg': '#333333', 'fg': 'white', 'font': ('Arial', 10)}
entry_style = {'bg': '#555555', 'fg': 'white', 'insertbackground': 'white'}
button_style = {'bg': '#4CAF50', 'fg': 'white', 'activebackground': '#45a049'}

# Создаем элементы интерфейса
tk.Label(root, text="Калькулятор брейнрота", font=("Arial", 16), bg='#333333', fg='white').pack(pady=10)

tk.Label(root, text="Количество сумок на хайсте:", **label_style).pack()
bags_entry = tk.Entry(root, **entry_style)
bags_entry.pack()

tk.Label(root, text="Количество вашего KPM на хайсте:", **label_style).pack()
kpm_entry = tk.Entry(root, **entry_style)
kpm_entry.pack()

tk.Label(root, text="Время на хайсте:", **label_style).pack()
time_entry = tk.Entry(root, **entry_style)
time_entry.pack()

calculate_btn = tk.Button(root, text="Рассчитать", command=calculate, **button_style)
calculate_btn.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12), bg='#333333', fg='white')
result_label.pack()

root.mainloop()