def get_cats_info(path):
    """Fuction take info and Create List from file"""
    cats_dict = []
    total = 0
    counter = 0
    try:
        with open (path, "r", encoding="utf-8") as file: # открываем файл, указывая его кодировку
            for line in file:
                id, name, age = line.strip().split(",")  # присвоить значения id, name, age через разделитель (,)
                cats_dict.append({"id":id, "name":name, "age":age}) # обновил свой списов значениями 3х переменных
        return cats_dict
                                                             
    except FileNotFoundError:                            # проверка на правильный путь к файлу и его существование
        print ("Указанный файл не найден.")
        return 0, 0
    except ValueError:                                   # проврека на формат данных внутри фала
        print ("Ошибка в формате файла данных.")
        return 0, 0
    
cats_info = get_cats_info("homer_works_goit/cats_file.txt")
print(cats_info)