import random

print( "\tДобро пожаловать в игру 'Отгадай число'!")
gest = int(input('Загадай натуральное число в диапазоне от 1 до 50. '))
print("Компютер постарается отгадать за  минимальне число попыток.\n")

num = random.randint(1, 50)
i = 1

while num != gest:
	if num > gest:
		print(num)
		print('меньше')
	else:
		print(num)
		print("больше")
	num = random.randint(1, 50)
	i += 1
print("Компютеру удалось отгадать число! Зто в самом деле",num)
print("Он затратили на отгадывание всего лишь ",i," попыток!")