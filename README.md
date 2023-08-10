## Maths Score Predictor

Maths Score Predictor is a machine learning project that aims to predict math scores based on various features using a Kaggle dataset. This repository contains all the necessary files and code to take you through the entire process, from data collection and preprocessing to model training and deployment.


### Introduction
Maths Score Predictor is a comprehensive project that demonstrates the end-to-end process of developing a machine learning model for predicting math scores. The project includes data collection, data preprocessing, model selection, training, evaluation, and deployment. Whether you're new to machine learning or looking to expand your skills, this repository can serve as a valuable resource.

#### Dataset
The dataset used for this project is sourced from kaggle : https://www.kaggle.com/datasets/spscientist/students-performance-in-exams <br>
It contains information about various factors that may influence math scores. The dataset includes features like student demographics, study time, parental education level, and more.

#### Installation
Clone the repository:
```bash
git clone https://github.com/your-username/Maths-Score-Predictor.git
cd Maths-Score-Predictor
```
Install the required dependencies:
```bash
python setup.py 
```
Run the application : 
```bash
streamlit run app.py
```

#### Usage
This project is organized into different stages, each implemented in a separate Jupyter Notebook.

#### Data Preprocessing
In src/components/ <br>
There are python files such as data_ingestion.py , data_transformation.py .In This files the complete data preprocessing steps are taken care of from data cleaning to data transformation. 

#### Model Training
In src/components/ <br>
There is a python file named model_trainer.py , It involves the model training part. Various algorithms are explored, and their performance is evaluated using appropriate metrics.

#### Model Evaluation
The src/utils.py notebook focuses on evaluating the trained models in detail. It includes analysis of the model's performance on the test dataset.

#### Deployment
The trained model is deployed using streamlit.<br> 
You can run : 
```bash
streamlit run app.py
```
or <br> 
You can go to : https://mathscorepredictor.streamlit.app/ to use the deployed application.  <br> 

Contributions to this repository are welcome. If you find any issues or want to add new features, please feel free to submit a pull request. <br>

For detailed information, refer to the individual notebooks and files within the repository. If you have any questions or feedback, feel free to contact me at shavilyarajput50@gmail.com 
Happy predicting!
