
# Develop and Deploying a Machine Learning Model using Titanic Data from Kaggle

## Project Structure

```
Internship Machine Learning Challenge/
├── dataset/
│   ├── train.csv
│   └── test.csv
├── models/
│   ├── random_forest_model.pkl
├── app.py
├── Preprocessing & Train Model.ipynb
├── README.md
└── requirements.txt
```

## Instructions

1. Download dataset from [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic/data)
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan file Jupyter Notebook `Preprocessing & Train Model.ipynb`
4. Jalankan API dengan:
   ```bash
   python app.py
   ```

## Model & Feature Summary

### Features Used:
1. `Pclass`: Kelas penumpang (1 = tertinggi, 3 = terendah)
2. `Sex`: Jenis kelamin (0 = wanita, 1 = pria)
3. `Age`: Usia
4. `Fare`: Harga tiket
5. `Embarked`: Pelabuhan keberangkatan (0 = C, 1 = Q, 2 = S)
6. `FamilySize`: Jumlah keluarga di kapal (`SibSp` + `Parch` + 1)

### Target:
- `Survived`: Selamat (0 = tidak selamat, 1 = selamat)

### Model Used:
- Random Forest Classifier
- Logistic Regression

---

## API Documentation

### 🔹 HEALTH — Health Check
- **Method**: `GET`
- **URL**: `http://127.0.0.1:5000`
- **Description**: Mengecek apakah API sedang berjalan
- **Response**:
```json
{
  "status": "API is running."
}
```

### 🔹 TRAIN — Retrain Model
- **Method**: `POST`
- **URL**: `http://127.0.0.1:5000/train`
- **Description**: Melatih ulang model dengan data baru
- **Input Example**:
```json
{
  "Pclass": 1,
  "Sex": 1,
  "Age": 22.0,
  "Fare": 7.25,
  "Embarked": 1,
  "FamilySize": 2,
  "Survived": 1
}
```
- **Response**:
```json
{
  "status": "Model retrained and saved."
}
```

### 🔹 PREDICT — Make Prediction
- **Method**: `POST`
- **URL**: `http://127.0.0.1:5000/predict`
- **Description**: Memprediksi apakah penumpang akan selamat atau tidak
- **Input Example**:
```json
{
  "Pclass": 1,
  "Sex": 1,
  "Age": 22.0,
  "Fare": 7.25,
  "Embarked": 1,
  "FamilySize": 2
}
```
- **Response**:
```json
{
  "prediction": 1
}
```
