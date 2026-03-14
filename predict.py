from pathlib import Path
import mlflow.sklearn
from sklearn.datasets import load_iris

# ustawienie lokalnej ścieżki oraz tracking URI dla MLflow
mlruns_path = Path("mlruns").resolve()
mlflow.set_tracking_uri(mlruns_path.as_uri())

# wczytanie modelu
loaded_model = mlflow.sklearn.load_model(f"runs:/e0780cc3263b4b369466180342ac463a/model")

# wczytanie danych
iris = load_iris()
X = iris.data
y = iris.target

# próbka do testu
sample = [X[0]]

# przewidywanie
prediction = loaded_model.predict(sample)
# wyznaczenie prawdopodobieństw
probabilities = loaded_model.predict_proba(sample)

# wyświetlenie wynikóws
print("Prawdziwa klasa:", y[0])
print("Przewidziana klasa:", prediction[0])
print("Prawdopodobieństwa klas:", probabilities[0])