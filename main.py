"""import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
data = pd.read_csv('train.csv')
print(data.head())
X = data[['temperature', 'humidity']]
y = data['weather_condition']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")"""



from joblib import load
try:
    model = load('./savedmodels/model.joblib')
except Exception as e:
    print(f"Error loading the model: {e}")