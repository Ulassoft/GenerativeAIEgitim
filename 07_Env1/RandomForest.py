import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error



file_path = "Prices.csv"
data = pd.read_csv(file_path)


# Özellikler ve hedef değişkeni ayırma
X = data[["alan", "odasayisi", "binayasi"]]
y = data["fiyat"]



# Eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# Random Forest modelini oluştur ve eğit
model = RandomForestRegressor(random_state=42, n_estimators=100)
model.fit(X_train, y_train)



# Test seti üzerinde tahmin yapma
y_pred = model.predict(X_test)



# Hata metriği hesaplama
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse}")


# Yeni bir veri tahmini
# Yeni veriyi buraya girin
new_data = pd.DataFrame({
    "alan": [300],  # Yeni evin alanı
    "odasayisi": [4],  # Yeni evin oda sayısı
    "binayasi": [5]  # Yeni evin bina yaşı
})

predicted_price = model.predict(new_data)
print(f"Yeni evin tahmini fiyatı: {predicted_price[0]:,.2f}")






