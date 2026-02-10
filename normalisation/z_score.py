from sklearn.preprocessing import StandardScaler
import numpy as np
salaires = np.array([[25000], [35000], [45000], [100000]])
scaler = StandardScaler()
salaires_standardises = scaler.fit_transform(salaires)
print(salaires_standardises)

