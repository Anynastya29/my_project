a = 40
b = 60
c = 20

print(f"Состав коктеля Апероль шприц, мл: ликер", a, "шампанское", b, "содовая", c)

liquor = int(input("Введите объем ликера: "))
if liquor != a:
    print("Неверно")

if liquor == a:
    print("Верно")

champagne = int(input("Введите объем шампанского: "))
if champagne != b:
    print("Неверно")

if champagne == b:
    print("Верно")

soda = int(input("Введите объем содовой: "))
if soda != c:
    print("Неверно")

if soda == c:
    print("Верно")

component_1 = input("Введите название первого компонента: ")

component_2 = input("Введите название второго компонента: ")

component_3 = input("Введите название третьего компонента: ")


print(f"Состав: {component_1} {liquor} {component_2} {champagne} {component_3} {soda}")











