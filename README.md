# 🏠 House Price Prediction Using Machine Learning

This project aims to predict housing prices using supervised learning techniques like **Decision Tree** and **Random Forest** from the popular Ames Housing Dataset. It's inspired by the [Kaggle competition](https://www.kaggle.com/competitions/home-data-for-ml-course).

---

## 📁 Files Included

| File                         | Description                                        |
|------------------------------|----------------------------------------------------|
| `house_price_prediction.py`  | Python script containing the DecisionTreeRegressor |
                               |  & RandomForestRegressor                           |
| `.gitignore`                 | Ignores datasets and virtual environment           |
| `README.md`                  | Project explanation and documentation              |
| `submission.csv`             | Final predictions (not uploaded by default)        |

---

## 📊 Dataset

We use the `train.csv` and `test.csv` from the Ames Housing Dataset (from Kaggle).  
Note: These are **not included** in the repo. Download from:  
🔗 [https://www.kaggle.com/competitions/home-data-for-ml-course](https://www.kaggle.com/competitions/home-data-for-ml-course)

### ✅ Features Used:

- `LotArea`: Lot size in square feet  
- `YearBuilt`: Year of original construction  
- `1stFlrSF`: First floor square feet  
- `2ndFlrSF`: Second floor square feet  
- `FullBath`: Full bathrooms above grade  
- `BedroomAbvGr`: Bedrooms above grade  
- `TotRmsAbvGrd`: Total rooms above grade  

### 🎯 Target:
- `SalePrice`: The property's sale price in USD

---

## 🚀 Project Workflow

### 1️⃣ Import Libraries  
Includes `pandas`, `sklearn` modules for modeling and evaluation.

### 2️⃣ Load and Explore Data  
Reads training data, prints `.describe()` and `.head()`.

### 3️⃣ Feature Selection  
Picks relevant numerical features for initial modeling.

### 4️⃣ Train a Basic Decision Tree  
Fits a `DecisionTreeRegressor` and evaluates performance.

### 5️⃣ Train-Validation Split  
Uses `train_test_split` to simulate unseen data evaluation.

### 6️⃣ MAE Evaluation  
Calculates **Mean Absolute Error (MAE)** on validation set.

### 7️⃣ Hyperparameter Tuning  
Finds the best `max_leaf_nodes` to reduce overfitting.

### 8️⃣ Random Forest Model  
Trains `RandomForestRegressor` for improved performance.

### 9️⃣ Load Test Data & Predict  
Predicts prices for test data using the final model.

### 🔟 Save Submission File  
Writes predictions to `submission.csv` for Kaggle or further use.

---

## 📉 Model Evaluation

- **Metric Used:** Mean Absolute Error (MAE)
- **Models Compared:**  
  - `DecisionTreeRegressor`  
  - `RandomForestRegressor`

---

## 🧰 Tools & Technologies

- Python 3.10+
-  VS Code
- Libraries:
  - pandas
  - scikit-learn (sklearn)
  - matplotlib (optional for visualization)

---

## 💡 Future Improvements

- Handle missing values properly (e.g., using SimpleImputer)
- Add categorical features using OneHotEncoding
- Visualize feature importance
- Create a scikit-learn Pipeline
- Use GridSearchCV for hyperparameter tuning
- Deploy with Flask or Streamlit (for web app)

---

## 🙋 Author

**👨 Vishnu Bishnoi**  
📫 [LinkedIn](https://www.linkedin.com/in/vishnu-bishnoi-261832230/)  
📁 [GitHub](https://github.com/vishnubishnoi263)  


---

## ⭐ Support

If you found this project helpful:
- ⭐ Star this repo
- 🔁 Fork it
- 🧑‍💼 Connect on LinkedIn
- 🧠 Reach out for collaboration or feedback

