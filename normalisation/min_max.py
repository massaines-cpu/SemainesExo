#min-max
from sklearn.preprocessing import MinMaxScaler
import numpy as np
salaires = np.array([[25000], [35000], [45000], [100000]])
scaler = MinMaxScaler()
salaires_normalises = scaler.fit_transform(salaires)
print(salaires_normalises)

scaler = MinMaxScaler()
X_train_norm = scaler.fit_transform(X_train)