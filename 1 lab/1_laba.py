a = "змінна з текстом"
b = 1 # числова Змінна
b1 = 1.1 
c = ["a", 1, 1.25, "Слово", a] # List
d = {"a": "Слово", "b": 1, a: b} # Dict
e = ("a", a) # Tuple
f = {"ss", str(a) + str(b)} # Set


print("Перша константа: ", True)
print(f"Як можна так робити вивід? {True}")
print(abs(-12.5), f"є рівним {abs(12.5)}", "і якщо порівняти то: ", abs(-12.5) == abs(12.5))
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")
else:
    print("Ця конструкція безглузда!")
from random import randint
A = randint(0, 1)
print(f"Значить А={A}" if A else f"Але може бути що А={A}")
A = 0
try:
    print("Що буде якщо", 10/A, "?")
except Exception as e:
    print("Невже це помилка > ", e)
finally:
    print("О це так на тобі!")
with open("README.md", "r") as f:
    for _, line in enumerate(f):
        print(f"{_})> {line}", end="")
def a_b_func(a, b):
    return a, b

this_is_lambda = lambda first, age: f'Цей код написав: {first}, Мені {age:10d} років'
print("Це просто функція:", a_b_func, "\nА це лямбда:", this_is_lambda)
print("Це її виклик:", this_is_lambda('Богдан', 1_00_000))
print(this_is_lambda(*a_b_func("a", 1)))
