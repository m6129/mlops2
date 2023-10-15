import sys
import os
import yaml
import pickle

import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Проверка корректности аргументов командной строки
if len(sys.argv) != 3:
    sys.stderr.write("Ошибка аргументов. Использование:\n")
    sys.stderr.write("\tpython dt.py data-file model \n")
    sys.exit(1)

# Определение имени входного файла и пути к выходному файлу модели
f_input = sys.argv[1]
f_output = os.path.join("models", sys.argv[2])
os.makedirs(os.path.join("models"), exist_ok=True)

# Загрузка параметров для обучения из файла params.yaml
params = yaml.safe_load(open("params.yaml"))["train"]
p_seed = params["seed"]
p_max_depth = params["max_depth"]
p_splitter = params["splitter"]
p_min_samples_split = params["min_samples_split"]

# Загрузка данных из входного файла в виде DataFrame
df = pd.read_csv(f_input)

# Определение матрицы признаков (X) и вектора целевых значений (y)
X = df.iloc[:,[0, 1, 3]]
y = df.iloc[:, 2]

# Создание и обучение модели регрессии на основе решающего дерева
clf = DecisionTreeRegressor(max_depth=p_max_depth, random_state=p_seed, splitter=p_splitter, min_samples_split=p_min_samples_split)
clf.fit(X, y)

# Сохранение обученной модели в файл с использованием Pickle
with open(f_output, "wb") as fd:
    pickle.dump(clf, fd)
