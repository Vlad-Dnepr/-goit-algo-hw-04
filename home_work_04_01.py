def total_salary(path):
    """Fuction take SUM-number from file (str)"""
    total = 0
    counter = 0
    try:
        with open (path, "r", encoding="utf-8") as file: # открываем файл, указывая его кодировку
            for line in file:
                name, salary = line.strip().split(",")   # присвоить значения в name и salary через разделитель (,)
                total +=  int(salary)                    # суммируем все цифры, делаем их целыми (int)
                counter += 1                             # добавляем счетчик на +1, чтобы найти среднее значение
        average = total / counter if counter > 0 else 0  # вычисляем среднее значение если данные не равны 0 (ноль)
        return total, average                            # чтобы не было ошибки ZeroDivisionError
    except FileNotFoundError:                            # проверка на правильный путь к файлу и его существование
        print ("Указанный файл не найден.")
        return 0, 0
    except ValueError:                                   # проврека на формат данных внутри фала
        print ("Ошибка в формате файла данных.")
        return 0, 0

total, average = total_salary("homer_works_goit\working_people.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")