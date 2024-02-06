# registration.py
import random

def сгенерироватьКод():
    код = random.randint(1000, 9999)
    print(f"Ваш одноразовый код: {код}")
    print("Пожалуйста, сохраните его.")
    return код
