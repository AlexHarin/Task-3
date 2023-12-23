def оценить_сложность_пароля(пароль):
    баллы = 0
    if len(пароль) >= 8:
        баллы += 1
    if any(символ.isupper() for символ in пароль):
        баллы += 1
    if any(символ.islower() for символ in пароль):
        баллы += 1
    if any(символ.isdigit() for символ in пароль):
        баллы += 1

    if any(символ in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for символ in пароль):
        баллы += 1

    return баллы

пароль1 = "StrongPassword123!"
пароль2 = "WeakPass"

результат1 = оценить_сложность_пароля(пароль1)
результат2 = оценить_сложность_пароля(пароль2)

print(f"Сложность пароля '{пароль1}': {результат1} баллов")
print(f"Сложность пароля '{пароль2}': {результат2} баллов")