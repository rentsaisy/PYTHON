from sklearn.tree import DecisionTreeRegressor 
import numpy as np

# Data latih contoh: [deadline_days, weight_pct, difficulty] -> skor_prioritas
X = np.array([
    [1,  10, 5],   # sangat mepet → tinggi
    [3,  50, 4],   # bobot besar & cukup dekat → tinggi
    [5,  40, 2],   # bobot besar tapi tidak terlalu sulit → sedang
    [6,  20, 3],   # bobot kecil, masih dekat → sedang
    [10, 20, 3],   # jauh & bobot kecil → rendah
    [2,  70, 2],   # mepet → tinggi
])
y = np.array([92, 88, 72, 60, 42, 90])  # skor target (contoh)

model = DecisionTreeRegressor(max_depth=3, random_state=42).fit(X, y)

# Prediksi contoh B: deadline=5, weight=40, difficulty=2
sample = np.array([[5, 40, 2]])
score = model.predict(sample)[0]

# Konversi skor ke label 
def to_label(score):
    if score >= 80: return "Tinggi"
    if score >= 55: return "Sedang"
    return "Rendah"

print("Skor:", round(float(score), 1), "| Label:", to_label(score))
