import sys
import os
import io

# Проверка наличия аргумента командной строки. Если количество аргументов не равно 2, выводим сообщение об ошибке и завершаем программу.
if len(sys.argv) != 2:
    sys.stderr.write("Ошибка аргументов. Использование:\n")
    sys.stderr.write("\tpython3 fill_na.py файл-данных\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage2", "train.csv")
os.makedirs(os.path.join("data", "stage2"), exist_ok=True)

# Функция для обработки данных из файла.
def process_data(fd_in, fd_out):
    arr_experience_level = []  # Список для уровня опыта.
    arr_job_title = []  # Список для названий должностей.
    arr_salary_in_usd = []  # Список для заработных плат в USD.
    arr_company_size = []  # Список для размеров компаний.

    # Чтение строк из входного файла и разделение их на элементы.
    for line in fd_in:
        line = line.rstrip('\n').split(',')
        arr_experience_level.append(line[0])  # Добавляем уровень опыта в соответствующий список.
        arr_job_title.append(line[1])  # Добавляем название должности в соответствующий список.
        arr_company_size.append(line[3])  # Добавляем размер компании в соответствующий список.

        # Проверка и добавление заработной платы в USD, если значение является числом и меньше 300000. В противном случае, добавляем 0.
        if line[2].isdigit() and int(line[2]) < 300000:
            arr_salary_in_usd.append(int(line[2]))
        else:
            arr_salary_in_usd.append(0)
            
    s = sum(arr_salary_in_usd)  # Вычисляем сумму всех зарплат в массиве arr_salary_in_usd
    salary_count = len(arr_salary_in_usd)  # Получаем количество элементов в массиве arr_salary_in_usd

    # Проходим по всем элементам массива arr_salary_in_usd
    for i in range(salary_count):
        # Если текущая зарплата равна 0, заменяем ее на среднее значение всех зарплат в массиве
        if arr_salary_in_usd[i] == 0:
            arr_salary_in_usd[i] = round(s / salary_count, 3)

    # Проходим по соответствующим массивам и записываем данные в выходной файл
    for p_experience_level, p_job_title, p_salary_in_usd, p_company_size in zip(arr_experience_level, arr_job_title, arr_salary_in_usd, arr_company_size):
        fd_out.write("{},{},{},{}\n".format(p_experience_level, p_job_title, p_salary_in_usd, p_company_size))

# Открываем входной файл для чтения и выходной файл для записи
with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        # Вызываем функцию process_data для обработки данных из входного файла и записи их в выходной файл
        process_data(fd_in, fd_out)
