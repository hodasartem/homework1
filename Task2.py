N = int(input('Введите количество секунд: \n'))

hour = N // 3600 
min = (N - (hour * 3600)) // 60 
sec = N - (hour * 3600) - (min * 60)

print(hour)
print(type(hour))

print(min)
print(type(min))

print(sec)
print(type(sec))

check 