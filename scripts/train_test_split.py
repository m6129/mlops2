import yaml
import sys
import os

import pandas as pd
from sklearn.model_selection import train_test_split

# Загрузка параметров из файла params.yaml для разделения данных
params = yaml.safe_load(open("params.yaml"))["split"]

# Проверка корректности аргументов командной строки
if len(sys.argv) != 2:
    sys.stderr.write("Ошибка аргументов. Использование:\n")
    sys.stderr.write("\tpython3 train_test_split.py data-file\n")
    sys.exit(1)

# Определение имен файлов
f_input = sys.argv[1]
f_output_train = os.path.join("data", "stage4", "train.csv")
os.makedirs(os.path.join("data", "stage4"), exist_ok=True)
f_output_test = os.path.join("data", "stage4", "test.csv")
os.makedirs(os.path.join("data", "stage4"), exist_ok=True)

# Определение соотношения разделения (train:test) из параметров
p_split_ratio = params["split_ratio"]

# Загрузка данных из входного файла
df = pd.read_csv(f_input)

# Определение матрицы признаков (X) и вектора целевых значений (y)
X = df.iloc[:, [1, 2, 3]]
y = df.iloc[:, 0]

# Разделение данных на обучающий и тестовый наборы с сохранением стратификации
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=p_split_ratio, stratify=y)

# Сохранение обучающего и тестового наборов данных в CSV-файлы
pd.concat([y_train, X_train], axis=1).to_csv(f_output_train, header=None, index=None)
pd.concat([y_test, X_test], axis=1).to_csv(f_output_test, header=None, index=None)
