print("Введите имя студента")
name  = input()

print("Введите фамилию студента")
surname = input()

print("Введите год рождения студента")
year = int(input())



print(name + "_" + surname + "_" + str(year))



name, surname = surname, name
year += 60



print(name + "_" + surname + "_" + str(year))
