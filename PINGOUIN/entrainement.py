import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib

# 1. Charger et nettoyer
df = sns.load_dataset('penguins').dropna()
# 2. Encodage du sexe
sexe_code = LabelEncoder()
df['sex'] = sexe_code.fit_transform(df['sex'])

# 3. Sélection des colonnes choisies
X = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'sex']]
y = df['species']

# 4. Normalisation
echelle = StandardScaler()
X_scaled = echelle.fit_transform(X)

# 5. Entraînement
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
carte_geographique = KNeighborsClassifier(n_neighbors=5)
carte_geographique.fit(X_train, y_train)

# 6. Sauvegarde des fichiers finaux
joblib.dump(carte_geographique, 'carte_geographique.pkl')
joblib.dump(echelle, 'echelle_convertie.pkl')
joblib.dump(sexe_code, 'traduction_sexe.pkl') #male = 1; femelle = 0

print("Fichiers sauvegardés : carte_geographique.pkl, echelle_convertie.pkl, traduction_sexe.pkl")