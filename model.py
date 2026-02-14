import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle


# 1. Load Dataset (Assuming you downloaded 'ENB2012_data.csv')
data = pd.read_csv('ENB2012_data.csv')

# Features: Relative Compactness, Surface Area, Wall Area, Roof Area, Overall Height, etc.
X = data.iloc[:, :-2] 
y = data.iloc[:, -2:] # Predicting both Heating and Cooling Load

# 2. Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train Model
model = LinearRegression()
model.fit(X_train, y_train)
# y_pred=model.predict(X_test)
# print(accuracy_score(y_test,y_pred))

# # 4. Save the Model
with open('energy_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as energy_model.pkl")