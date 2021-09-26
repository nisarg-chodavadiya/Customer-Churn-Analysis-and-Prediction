# Read Data
import numpy as np
import pandas as pd

# Machine Learning
from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Save Model
import pickle

df = pd.read_csv('D:/Nisarg/Data Science/Datasets/telecom_churn.csv')

# Define Features and Target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Model
clfr = RandomForestClassifier(n_estimators=100, random_state=0)
clfr.fit(X_train, y_train)

pickle.dump(clfr, open('TCC-RF-clf.pkl', 'wb'))
print("---Done---")