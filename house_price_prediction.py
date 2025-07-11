# ----------------------------------
# 📚 1. Import Required Libraries
# ----------------------------------
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# ----------------------------------
# 📊 2. Load & Explore Training Data
# ----------------------------------
data = pd.read_csv("train.csv")

print("📈 Data Overview:")
print(data.describe())
print("\n👀 Data Preview:")
print(data.head())

# ----------------------------------
# 🎯 3. Define Target and Features
# ----------------------------------
y = data["SalePrice"]
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF',
            'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = data[features]

# ----------------------------------
# 🌳 4. Train a Basic Decision Tree
# ----------------------------------
basic_tree = DecisionTreeRegressor(random_state=1)
basic_tree.fit(X, y)

# ----------------------------------
# ✂️ 5. Split Data for Validation
# ----------------------------------
X_train, X_val, y_train, y_val = train_test_split(X, y, random_state=1)

# ----------------------------------
# 🌳 6. Train and Evaluate Decision Tree on Validation
# ----------------------------------
tree_model = DecisionTreeRegressor()
tree_model.fit(X_train, y_train)
val_preds = tree_model.predict(X_val)
tree_mae = mean_absolute_error(y_val, val_preds)
print("\n🌳 Decision Tree MAE:", round(tree_mae, 2))

# ----------------------------------
# 🔍 7. Find Best Leaf Size for Tree
# ----------------------------------
def get_mae(max_leaf_nodes, X_train, X_val, y_train, y_val):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=1)
    model.fit(X_train, y_train)
    preds = model.predict(X_val)
    return mean_absolute_error(y_val, preds)

leaf_scores = {size: get_mae(size, X_train, X_val, y_train, y_val)
               for size in [5, 25, 50, 100, 250, 500]}

print("\n📐 MAE for Different max_leaf_nodes:")
for size in leaf_scores:
    print(f"  Leaf size {size}: MAE = {round(leaf_scores[size], 2)}")

best_leaf = min(leaf_scores, key=leaf_scores.get)
print(f"\n✅ Best leaf size: {best_leaf} (Lowest MAE: {round(leaf_scores[best_leaf], 2)})")

# ----------------------------------
# 🌲 8. Random Forest Model
# ----------------------------------
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_val)
rf_mae = mean_absolute_error(y_val, rf_preds)
print("\n🌲 Random Forest MAE:", round(rf_mae, 2))

# ----------------------------------
# 🧪 9. Load Test Data and Predict
# ----------------------------------
test_data = pd.read_csv("test.csv")
test_X = test_data[features]

# Final model (can be improved to use RandomForest instead)
final_model = DecisionTreeRegressor(random_state=1)
final_model.fit(X, y)
final_preds = final_model.predict(test_X)

# ----------------------------------
# 📤 10. Save Submission File
# ----------------------------------
output = pd.DataFrame({
    'Id': test_data['Id'],
    'SalePrice': final_preds
})
output.to_csv('submission.csv', index=False)
print("\n✅ Submission file 'submission.csv' created successfully.")


