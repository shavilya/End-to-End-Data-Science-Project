import streamlit as st
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

def predict_datapoint():
    st.header("Predict Data Point")
    st.write("Enter the following details to predict the result:")

    gender = st.selectbox("Gender", ['male', 'female'])
    race_ethnicity = st.selectbox("Race_ethnicity", ['group A', 'group B', 'group C', 'group D', 'group E'])
    parental_level_of_education = st.selectbox("Parental Level of Education", ['some high school', 'high school', 'some college', "associate's degree", "bachelor's degree", "master's degree"])
    lunch = st.selectbox("Lunch", ['standard', 'free/reduced'])
    test_preparation_course = st.selectbox("Test Preparation Course", ['none', 'completed'])
    reading_score = st.number_input("Reading Score", min_value=0, max_value=100, step=1)
    writing_score = st.number_input("Writing Score", min_value=0, max_value=100, step=1)

    if st.button("Predict"):
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )
        pred_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        st.subheader("Prediction Result")
        st.write("The predicted result is:", results[0])

def main():
    st.title("Math Score Predictor")
    predict_datapoint()

if __name__ == "__main__":
    main()

