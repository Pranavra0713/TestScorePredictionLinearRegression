import pandas as pd, tkinter as tk
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
data = pd.read_csv('data.csv')

window = tk.Tk()
window.title("Test Score Predictor")
tk.Label(window, text="Test 1 Score:").grid(row=0)
test1_input = tk.Entry(window)
test1_input.grid(row=0, column=1)
tk.Label(window, text="Test 2 Score:").grid(row=1)
test2_input = tk.Entry(window)
test2_input.grid(row=1, column=1)
tk.Label(window, text="Test 3 Prediction:").grid(row=2)
test3_prediction = tk.Label(window, text="")
test3_prediction.grid(row=2, column=1)

def clear_fields():
    test1_input.delete(0, tk.END)
    test2_input.delete(0, tk.END)
    test3_prediction.config(text="")

clear_button = tk.Button(window, text="Clear", command=clear_fields)
clear_button.grid(row=3, column=0)

def train_model():
    global data
    X = data[['Test 1', 'Test 2']]
    y = data['Test 3']
    linear_regression = LinearRegression()
    svr = SVR()
    rf_model = RandomForestRegressor(n_estimators=500)
    gb_model = GradientBoostingRegressor(n_estimators=500)
    voting_regressor = VotingRegressor([('lr', linear_regression), ('svr', svr),('random_forest', rf_model), ('gradient_boosting', gb_model)])
    voting_regressor.fit(X, y)
    test1 = float(test1_input.get())
    test2 = float(test2_input.get())
    test3 = voting_regressor.predict([[test1, test2]])
    if test3[0] > 50:
        test3[0] = 50
    else:
        test3[0] = round(test3[0], 2)
    test3_prediction.config(text=str(test3[0]))
    new_data = pd.DataFrame({
        'Test 1': [test1],
        'Test 2': [test2],
        'Test 3': [test3[0]]
    })
    data = pd.concat([data, new_data], ignore_index=True)
    data.to_csv('data.csv', index=False)
train_button = tk.Button(window, text="Predict", command=train_model)
train_button.grid(row=3, column=1)
window.mainloop()
