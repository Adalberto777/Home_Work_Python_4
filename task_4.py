# Задана натуральная степень k. Сформировать случайным образом список коэффициентов многочлена и записать в файл многочлен степени k.
# Коэффициенты должны быть случайными числами в диапазоне от 1 до 100
# Пример:
# - k=2 => 6*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0
# Усложнение: Коэффициенты в полиноме могут быть нулевыми.
# Примечание Создать три функции:
# 1) Функция формирования полинома. аргумент: степень полинома; возвращает полином. Коэффициенты вычисляются случайными.
# Полином удобно представить как словарь или как список коэффициентов. (на ваш выбор)
# В словаре степени будут ключами, в списке - индексами.
# Например k=3 => 6*x^3 + 4*x + 5. Словарь будет такой: {3:6, 2:0, 1:4, 0:5}. А список такой [5,4,0,6]
# 2) Функция формирование строки-полинома. Аргумент: полином (в вид словаря или списка).
# Возвращает строку вида '6*x^3 + 4*x + 5'
# Примечание: Обратите внимание на запись первой и нулевой степени, а также учет нулевого коэффициента.
# Для формирования строки удобно использовать join
# 3) Функция записи строки-полинома в файл. Аргументы: имя файла и строка-полином.

from random import randint


def create_coeffs(k: int) ->list:
    return [randint(0, 100) for _ in range(k + 1)]


def create_str(list_coeffs: list) -> str:
    lenght = len(list_coeffs)
    rez =[]
    # lst_str = [f"{el}*x^{lenght - idx - 1}" for idx, el in enumerate(list_coeffs)]
    # return " + ".join(lst_str)
    for idx, el in enumerate(list_coeffs):
        if el == 0:
            rez +=[]
        elif lenght - idx - 1 == 0:
            rez += [f"{el} = 0"]
        elif lenght - idx - 1 == 1:
            rez += [f"{el}*x"]
        else:
            rez += [f"{el}*x^{lenght - idx - 1}"]
        
    return " + ".join(rez)


def write_to_file(polynoms_str: str, file_name: str) -> None:
    with open(file_name, mode="w", encoding="utf-8") as file:
        file.write(polynoms_str)



k = int(input('Enter k: '))
list_coeffs = create_coeffs(k)
polynoms_str = create_str(list_coeffs)

print(create_coeffs(k))
print(create_str(list_coeffs))

write_to_file(create_str(create_coeffs(k)), "test.txt")
