
time = int(input("Введите время в секуднах: "))
h = time // 3600
h_1 = (time - h*3600)
min = h_1 // 60
sec = h_1 - min * 60
print(f'{h:>02}:{min:>02}:{sec:>02}')

