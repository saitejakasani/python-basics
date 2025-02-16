# -*- coding: utf-8 -*-
"""Pickle File.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10YHWZ7F_WdT5_SkMKsNGhk1nKzS7RqzC
"""

import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle
california = fetch_california_housing()

california

california.data.shape

california.data[:5]

california.feature_names

california.target_names

df = pd.DataFrame(california.data)

df.columns = california.feature_names

df['MedHouseVal'] = california.target

df

X = pd.DataFrame(california.data, columns=california.feature_names)
y = pd.DataFrame(california.target, columns=["Median_House_Value"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train.values.ravel())

RandomForestRegressor(random_state=42)

y_train.values.shape

y_pred_rf = rf_model.predict(X_test_scaled)

print("Random Forest Regression Metrics:")
print(f"MAE: {mean_absolute_error(y_test, y_pred_rf)}")
print(f"MSE: {mean_squared_error(y_test, y_pred_rf)}")
print(f"R2 Score: {r2_score(y_test, y_pred_rf)}")

with open("random_forest_model.pkl", "wb") as f:
    pickle.dump(rf_model, f)

import tensorflow as tf
from tensorflow import keras
dl_model = keras.Sequential([
    keras.layers.Dense(64, activation="relu", input_shape=(X_train_scaled.shape[1],)),
    keras.layers.Dense(32, activation="relu"),
    keras.layers.Dense(16, activation="relu"),
    keras.layers.Dense(1)
])

dl_model.compile(optimizer="adam", loss="mse", metrics=["mae"])

dl_model.fit(X_train_scaled, y_train, validation_data=(X_test_scaled, y_test), epochs=50, batch_size=32)

dl_model.save("deep_learning_model.h5")

with open("random_forest_model.pkl", "rb") as f:
    loaded_rf_model = pickle.load(f)
y_pred_loaded_rf = loaded_rf_model.predict(X_test_scaled)
print(f"Loaded RF Model R2 Score: {r2_score(y_test, y_pred_loaded_rf)}")

import tensorflow as tf
from tensorflow import keras
loaded_dl_model = keras.models.load_model("deep_learning_model.h5", custom_objects={'mse': tf.keras.losses.MeanSquaredError})
y_pred_loaded_dl = loaded_dl_model.predict(X_test_scaled)
print(f"Loaded DL Model MSE: {r2_score(y_test, y_pred_loaded_dl)}")

