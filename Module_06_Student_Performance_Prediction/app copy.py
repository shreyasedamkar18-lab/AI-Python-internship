
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


# Load the student dataset
data = pd.read_csv("student_data.csv")

# Display the dataset
print("Student Performance Dataset:")
print(data)

# Display basic information
print("\nDataset Information:")
print(data.info())

# Display statistical summary
print("\nStatistical Summary:")
print(data.describe())


# Separate input features and target
X = data[["Study_Hours", "Attendance", "Previous_Score"]]

y = data["Final_Score"]

# Display the input features and target
print("\nInput Features:")
print(X.head())

print("\nTarget Values:")
print(y.head())

print("\nDataset Shape:")
print("Input Features:", X.shape)
print("Target Values:", y.shape)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Display the shapes of the datasets
print("\nTraining and Testing Data:")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

# Create the Linear Regression model
model = LinearRegression()

# Train the model using training data
model.fit(X_train, y_train)

print("\nModel Training Completed Successfully!")

# Predict scores using the testing data
y_pred = model.predict(X_test)

# Calculate the Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)

# Display actual and predicted scores
print("\nModel Testing Results:")
print("Actual Scores:", list(y_test))
print("Predicted Scores:", y_pred.round(2))

print("\nMean Absolute Error:", round(mae, 2))

# Predict the final score for a new student
new_student = pd.DataFrame({
    "Study_Hours": [5],
    "Attendance": [80],
    "Previous_Score": [70]
})

# Generate prediction
prediction = model.predict(new_student)

# Display the result
print("\nNew Student Prediction:")
print("Study Hours: 5")
print("Attendance: 80%")
print("Previous Score: 70")
print("Estimated Final Score:", round(prediction[0], 2))

# Visualize actual vs predicted scores
plt.figure(figsize=(8, 5))

plt.plot(
    range(len(y_test)),
    list(y_test),
    marker="o",
    label="Actual Scores"
)

plt.plot(
    range(len(y_pred)),
    y_pred,
    marker="s",
    label="Predicted Scores"
)

plt.title("Actual vs Predicted Student Scores")
plt.xlabel("Test Student")
plt.ylabel("Final Score")
plt.legend()
plt.grid(True)

plt.show()