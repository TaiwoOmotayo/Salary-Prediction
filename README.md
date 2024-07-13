# Salary Prediction Project

## Overview
This repository contains code and data for predicting salaries based on various features related to data professions. The goal of this project is to develop and deploy a salary prediction model that can assist in estimating salaries for data professionals.

## Project Structure
- **data/**: Contains datasets used for training and testing the model.
- **notebooks/**: Jupyter notebooks for data exploration, preprocessing, model training, and evaluation.
- **scripts/**: Python scripts for data cleaning, feature engineering, and model deployment.
- **models/**: Saved model artifacts after training.
- **README.md**: Overview of the project, installation instructions, and usage guidelines.

## Setup
To set up the environment:
1. Clone this repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run Jupyter notebooks in the `notebooks/` directory for detailed exploration.

## Data
The primary dataset used is named 'Salary Prediction of Data Professions', containing features such as 'SEX,' 'DESIGNATION,' 'UNIT,' 'LEAVES REMAINING,' 'LEAVES USED,' 'RATINGS,' 'year joined,' 'month joined,' 'day joined,' 'dayofweek joined,' and 'quarter joined.'

## Notebooks
- **01_Data_Exploration.ipynb**: Explore the dataset, visualize distributions, and analyze correlations.
- **02_Data_Preprocessing.ipynb**: Clean data, handle missing values, encode categorical variables, and prepare features for modeling.
- **03_Model_Training.ipynb**: Train machine learning models to predict salaries.
- **04_Model_Evaluation.ipynb**: Evaluate model performance using metrics like Mean Squared Error (MSE) and R-squared.

## Scripts
- **data_cleaning.py**: Functions for cleaning and preprocessing data.
- **feature_engineering.py**: Functions for feature selection and engineering.
- **modeling.py**: Functions for training and saving machine learning models.
- **deployment.py**: Script for deploying the trained model for predictions.

## Models
- **saved_model.pkl**: Pickled file containing the trained model.

## Usage
- Follow the notebooks sequentially to understand the data processing and modeling steps.
- Use scripts for automating data preprocessing and model training.
- Deploy the model using `deployment.py` for making salary predictions.

## License
This is solely a project of my internship at Mentorness.
