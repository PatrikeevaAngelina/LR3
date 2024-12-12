class ElementPatrikeeva:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

element = ElementPatrikeeva("Фосфор", "P", 15)

print("Имя элемента:", element.name)
print("Символ элемента:", element.symbol)
print("Номер элемента:", element.number)
