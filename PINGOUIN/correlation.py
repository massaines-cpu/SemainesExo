import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib

# charger les données
df = sns.load_dataset('penguins').dropna()

traduction = {
    'bill_length_mm': 'longueur bec',
    'bill_depth_mm': 'épaisseur bec',
    'flipper_length_mm': 'nageoire',
    'body_mass_g': 'poids',
    'island': 'ile',
    'sex': 'sexe'
}
df = df.rename(columns=traduction)

# matrice correlation
le_sexe = LabelEncoder()
df['sex'] = le_sexe.fit_transform(df['sexe'])

l_ile = LabelEncoder()
df['ile'] = l_ile.fit_transform(df['ile'])

matrice = df.select_dtypes(include=['float64', 'int64']).corr()
print(matrice)

# pour l'afficher joliment
sns.heatmap(matrice, annot=True, cmap='coolwarm')
plt.title("Matrice de corrélation des attributs des pingou")
plt.show()

# prépa pour KNN
colonnes_finales = ['longueur_bec', 'épaisseur_bec', 'nageoire', 'poids', 'sexe', 'ile']
X = df[colonnes_finales]
y = df['species']

# KNN a besoin que les données soient à la même échelle (StandardScaler)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# ENTRAÎNEMENT KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# SAUVEGARDE
joblib.dump(knn, 'model_knn_pingouin.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(le_sexe, 'le_sexe.pkl')
joblib.dump(l_ile, 'le_ile.pkl')