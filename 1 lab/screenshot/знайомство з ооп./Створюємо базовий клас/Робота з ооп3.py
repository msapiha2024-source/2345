class Dog:
    kind = 'canine'         # змінна класу (спільна для всіх)

    def __init__(self, name):
        self.name = name    # змінна екземпляру (унікальна для кожного)

d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)  # canine
print(e.kind)  # canine
print(d.name)  # Fido
print(e.name)  # Buddy