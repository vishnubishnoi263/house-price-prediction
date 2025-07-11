# 🏠 House Price Prediction with Decision Tree and Random Forest

This project predicts house sale prices using supervised regression models on the **Ames Housing Dataset**. It uses **Decision Tree** and **Random Forest** models, evaluates them using **Mean Absolute Error (MAE)**, and produces a submission file similar to a Kaggle competition.

---

## 📂 Project Structure

| File                     | Description                                      |
|--------------------------|--------------------------------------------------|
| `house_price_prediction.py` | Main script for training and predicting prices |
| `submission.csv`         | Final predicted prices (output file, optional)  |
| `train.csv` & `test.csv` | Dataset files (downloaded from Kaggle manually) |
| `.gitignore`             | Prevents large or unnecessary files from uploading |

---

## 🧠 Project Objectives

- 📌 Predict housing prices using selected features
- 🧪 Train and evaluate multiple models
- 📉 Compare performance using MAE
- 🧾 Generate predictions for unseen test data
- 📝 Save results in CSV format for submission

---

## 📊 Dataset Description

The data comes from the Kaggle competition:  
🔗 [Home Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/home-data-for-ml-course)

### Features Used:
- `LotArea`: Lot size in square feet
- `YearBuilt`: Original construction year
- `1stFlrSF`: First floor square footage
- `2ndFlrSF`: Second floor square footage
- `FullBath`: Number of full bathrooms
- `BedroomAbvGr`: Bedrooms above ground level
- `TotRmsAbvGrd`: Total rooms above ground

### Target:
- `SalePrice`: House sale price in USD

---

## 🚀 Workflow Summary

### 📦 1. Import Required Libraries
Libraries like `pandas`, `sklearn` are used for data handling, model building, and evaluation.

### 📥 2. Load & Explore Data
The training data is loaded and summarized using `.describe()` and `.head()`.

### 🎯 3. Select Features and Target
Key numerical features are selected for modeling. The target is `SalePrice`.

### 🌳 4. Train Basic Decision Tree
A simple `DecisionTreeRegressor` is trained on the full dataset.

### ✂️ 5. Split Data for Validation
The dataset is split into training and validation subsets.

### 🔍 6. Tune Tree with Best Leaf Nodes
MAE is computed for various `max_leaf_nodes` values to find the best-performing tree size.

### 🌲 7. Train Random Forest Regressor
A `RandomForestRegressor` is trained and evaluated on the same data.

### 🧪 8. Predict on Test Data
Test set predictions are generated using the trained Decision Tree model.

### 📤 9. Export Final Predictions
Predictions are saved to `submission.csv`, formatted for Kaggle-style evaluation.

---

## 📉 Model Performance (Example)

| Model              | MAE (on Validation Set) |
|--------------------|-------------------------|
| Decision Tree      | ~28,000+ (varies)       |
| Random Forest      | ✅ Lower MAE (~18,000–22,000) |

---

## 🛠 Tech Stack

- **Language**: Python 3.x
- **Libraries**:  
  - `pandas` – data manipulation  
  - `scikit-learn` – models & evaluation  
- **Editor**: Jupyter  
- **Environment**: Local 

---

## 📦 Future Improvements

- ✅ Add missing value handling
- ✅ Use pipelines for clean preprocessing
- ✅ Add categorical feature encoding
- ✅ Visualize feature importances
- ✅ Improve final model (RandomForest instead of DecisionTree)

---

## 🙋 About the Author

**👨 Vishnu Bishnoi**  
📍 Aspiring Data Scientist | Python, ML, SQL  
📫 [LinkedIn](https://www.linkedin.com/in/vishnu-bishnoi-261832230/)  
📁 [GitHub](https://github.com/vishnubishnoi263)

---

## ⭐ Support This Project

If you find this useful:
- ⭐ Star this repo
- 🔁 Fork it
- 🧠 Connect with me for feedback or collaboration



