import os
import sys
import pickle
import json

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

if len(sys.argv) != 3:
    sys.stderr.write("Ошибка аргументов. Использование:\n")
    sys.stderr.write("\tpython dt.py data-file model \n")
    sys.exit(1)

# Определение имени входного файла и пути к выходному файлу модели

df = pd.read_csv(sys.argv[1])

X = df.iloc[:, [0, 1, 3]]
y = df.iloc[:, 2]

with open(sys.argv[2], "rb") as fd:
    clf = pickle.load(fd)

y_pred = clf.predict(X)
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = mean_squared_error(y, y_pred, squared=False)

metrics_file = os.path.join("evaluate", "metrics.json")

with open(metrics_file, "w") as fd:
    json.dump({"MAE": mae, "MSE": mse, "RMSE": rmse}, fd)
