
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="📚",
    layout="centered"
)

# Load dataset
data = pd.read_csv("student_data.csv")

# Page title
st.title("📚 Student Performance Prediction System")
st.write(
    "Enter student details to estimate a final score "
    "using a machine learning model."
)

st.divider()

# Prepare features and target
X = data[["Study_Hours", "Attendance", "Previous_Score"]]
y = data["Final_Score"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Student inputs
st.subheader("Enter Student Details")

study_hours = st.slider(
    "Daily Study Hours",
    min_value=0,
    max_value=12,
    value=5
)

attendance = st.slider(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=80
)

previous_score = st.slider(
    "Previous Score",
    min_value=0,
    max_value=100,
    value=70
)

# Prediction button
if st.button("Predict Final Score"):
    new_student = pd.DataFrame({
        "Study_Hours": [study_hours],
        "Attendance": [attendance],
        "Previous_Score": [previous_score]
    })

    prediction = model.predict(new_student)[0]

    st.success(
        f"Estimated Final Score: {prediction:.2f}"
    )

    st.caption(
        "This is an educational estimate based on a "
        "small sample dataset, not a guaranteed result."
    )

# Model information
st.divider()
st.subheader("Dataset Overview")

st.write("Number of sample records:", len(data))
st.dataframe(data)

st.subheader("Model Evaluation")

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

st.write(f"Mean Absolute Error: {mae:.2f}")
# Study Hours vs Final Scores Chart
st.divider()
st.subheader("Study Hours vs Final Scores")

st.scatter_chart(
    data,
    x="Study_Hours",
    y="Final_Score"
)