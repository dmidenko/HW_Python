# Задание №2
input_values = int(input("Введите число"))
h = input_values // 3600
min = (input_values % 3600)//60
sec = input_values - ( h*3600 + min*60)

print("часы: {2}, минуты {1}, секунды {0}".format(sec,min,h))