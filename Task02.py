time = int(input("Введите время, сек: "))

hours = time//3600

minutes = (time - hours * 3600)//60

seconds = time - (hours * 3600 + minutes * 60)

print(f"Время (чч:мм:сс)    {hours}:{minutes}:{seconds}")

