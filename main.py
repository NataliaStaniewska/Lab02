import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


mlflow.set_experiment("Lab2")

# wczytanie danych
iris = load_iris()
X = iris.data
y = iris.target

# podział danych na trening i test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# hiperparametr
max_iter = 300

# run MLflow
with mlflow.start_run():
    # utworzenie modelu
    model = LogisticRegression(max_iter=max_iter)

    # trening
    model.fit(X_train, y_train)

    # predykcja
    y_pred = model.predict(X_test)

    # metryka
    accuracy = accuracy_score(y_test, y_pred)

    # zapis do MLflow
    mlflow.log_param("max_iter", max_iter)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(sk_model=model, name="model")

print("Trening zakończony")