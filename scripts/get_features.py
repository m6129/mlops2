import sys
import os
import io

# Проверка наличия правильного количества аргументов командной строки.
if len(sys.argv) != 2:
    sys.stderr.write("Ошибка аргументов. Использование:\n")
    sys.stderr.write("\tpython3 get_features.py файл-данных\n")
    sys.exit(1)

# Определение входного и выходного файлов.
f_input = sys.argv[1]
f_output = os.path.join("data", "stage1", "train.csv")
os.makedirs(os.path.join("data", "stage1"), exist_ok=True)

# Функция для обработки данных.
def process_data(fd_in, fd_out):
    # Считываем первую строку файла, предположительно это заголовок, и пропускаем его.
    fd_in.readline()
    for line in fd_in:
        # Разбиваем строку на отдельные элементы, используя запятую как разделитель.
        line = line.rstrip('\n').split(',')
        
        # Извлекаем необходимые данные из строки.
        p_experience_level = line[1]  # Уровень опыта
        p_job_title = line[3]  # Название должности
        p_salary_in_usd = line[4]  # Зарплата в USD
        p_company_size = line[10]  # Размер компании
        
        # Записываем извлеченные данные в выходной файл, разделяя их запятыми.
        fd_out.write("{},{},{},{}\n".format(p_experience_level, p_job_title, p_salary_in_usd, p_company_size))

# Открываем входной файл для чтения с учетом кодировки utf-8.
with io.open(f_input, encoding="utf8") as fd_in:
    # Открываем выходной файл для записи с учетом кодировки utf-8.
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        # Вызываем функцию для обработки данных.
        process_data(fd_in, fd_out)