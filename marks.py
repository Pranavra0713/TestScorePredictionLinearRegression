import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import tkinter as tk

# Load the data
data = pd.read_csv('data.csv')
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data[['Test 1', 'Test 2']], data['Test 3'], test_size=0.2)
# Create the GUI window
window = tk.Tk()
window.title("Test Score Predictor")

# Create labels and input boxes for the user to enter their test scores
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

# Function to update the training data with the user's input and retrain the model
def train_model():
    # Load data
    global data

    # Create X and y arrays
    X = data[['Test 1', 'Test 2']]
    y = data['Test 3']

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Get input from user
    test1 = float(test1_input.get())
    test2 = float(test2_input.get())

    # Predict fourth test result
    test3 = model.predict([[test1, test2]])
    if test3[0] > 50:
        test3[0] = 50
    else:
        test3[0]=round(test3[0],2)

    # Display result to user
    test3_prediction.config(text=str(test3[0]))

    # Add new data to the dataset
    new_data = pd.DataFrame({
        'Test 1': [test1],
        'Test 2': [test2],
        'Test 3': [test3[0]]
    })
    data = pd.concat([data, new_data], ignore_index=True)
    data.to_csv('data.csv', index=False)

# Create a button to train the model and display the predicted score
train_button = tk.Button(window, text="Train Model", command=train_model)
train_button.grid(row=3, column=1)
# Run the GUI window
window.mainloop()