# Credit Risk Prediction Project

## Overview
This project is focused on understanding, predicting, and classifying credit risk using machine learning models. The goal is to build a system that can predict whether a user is a high or low credit risk based on their transaction data. The project encompasses various stages such as data exploration, feature engineering, model training, and deployment.

## Table of Contents
- [Task 1 - Understanding Credit Risk](#task-1-understanding-credit-risk)
- [Task 2 - Exploratory Data Analysis (EDA)](#task-2-exploratory-data-analysis-eda)
- [Task 3 - Feature Engineering](#task-3-feature-engineering)
- [Task 4 - Default Estimator and WoE Binning](#task-4-default-estimator-and-woe-binning)
- [Task 5 - Modelling](#task-5-modelling)
- [Task 6 - Model Serving API Call](#task-6-model-serving-api-call)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Task 1 - Understanding Credit Risk
Credit risk refers to the likelihood that a borrower may default on a loan or credit obligation. This task aims to understand the core concepts of credit risk, including the evaluation of default likelihood and risk management strategies used in the financial industry. Key references are provided for further reading.

### Key References:
- [Credit Risk Overview](https://www3.stat.sinica.edu.tw/statistica/oldpdf/A28n535.pdf)
- [Alternative Credit Scoring](https://www.hkma.gov.hk/media/eng/doc/key-functions/financial-infrastructure/alternative_credit_scoring.pdf)
- [World Bank Credit Scoring Guidelines](https://thedocs.worldbank.org/en/doc/935891585869698451-0130022020/original/CREDITSCORINGAPPROACHESGUIDELINESFINALWEB.pdf)
- [How to Develop a Credit Risk Model](https://towardsdatascience.com/how-to-develop-a-credit-risk-model-and-scorecard-91335fc01f03)
- [Credit Risk Overview by CFI](https://corporatefinanceinstitute.com/resources/commercial-lending/credit-risk/)
- [Credit Risk Definition](https://www.risk-officer.com/Credit_Risk.htm)

---

## Task 2 - Exploratory Data Analysis (EDA)
In this phase, we explore the dataset to understand its structure and key characteristics. The objective is to perform an in-depth analysis that includes identifying patterns, distributions, outliers, and missing values.

### Steps:
- **Overview of the Data**: Review the dataset’s rows, columns, and data types.
- **Summary Statistics**: Generate statistics for central tendency and distribution.
- **Distribution of Numerical Features**: Visualize the distribution to detect skewness or outliers.
- **Distribution of Categorical Features**: Analyze frequency and variability of categorical variables.
- **Correlation Analysis**: Examine relationships between numerical variables.
- **Missing Values**: Identify and address missing data.
- **Outlier Detection**: Use boxplots to detect and handle outliers.

---

## Task 3 - Feature Engineering
Feature engineering is crucial for improving model performance. This phase involves creating new features, encoding categorical variables, handling missing values, and normalizing or standardizing numerical features.

### Steps:
1. **Create Aggregate Features**:
   - Total Transaction Amount
   - Average Transaction Amount
   - Transaction Count
   - Standard Deviation of Transaction Amounts
2. **Extract Features**:
   - Transaction Hour
   - Transaction Day
   - Transaction Month
   - Transaction Year
3. **Encode Categorical Variables**:
   - One-Hot Encoding
   - Label Encoding
4. **Handle Missing Values**:
   - Imputation (mean, median, mode) or Removal
5. **Normalize/Standardize Numerical Features**:
   - Scaling numerical features to a consistent range.

### Tools:
- [xverse](https://pypi.org/project/xverse/)
- [woe](https://pypi.org/project/woe/)

---

## Task 4 - Default Estimator and WoE Binning
Here, we classify users based on their likelihood of default using RFMS formalism. We create a default estimator and apply Weight of Evidence (WoE) binning to improve the quality of the features used for modeling.

### Steps:
1. **Construct a Default Estimator**: Establish boundaries to classify users into high or low-risk categories.
2. **WoE Binning**: Apply Weight of Evidence (WoE) and Information Value (IV) to transform features into more predictive forms.

---

## Task 5 - Modelling
This task involves training machine learning models to predict credit risk, followed by model evaluation to assess performance.

### Steps:
1. **Split the Data**: Partition the data into training and testing sets.
2. **Choose Models**: Train at least two models from the following:
   - Logistic Regression
   - Decision Trees
   - Random Forest
   - Gradient Boosting Machines (GBM)
3. **Train the Models**: Train the models on the training data.
4. **Hyperparameter Tuning**: Use techniques like Grid Search or Random Search to fine-tune the models.
5. **Model Evaluation**: Evaluate model performance using metrics such as Accuracy, Precision, Recall, F1 Score, and ROC-AUC.

---

## Task 6 - Model Serving API Call
After training the models, we deploy them via a REST API for real-time predictions. The goal is to create an API that can accept new data and return predictions on credit risk.

### Steps:
1. **Choose Framework**: Use a framework such as Flask, FastAPI, or Django REST for API development.
2. **Load the Model**: Load the trained machine learning model for inference.
3. **Define API Endpoints**: Implement endpoints to accept input and return predictions.
4. **Handle Requests**: Process incoming requests, make predictions using the model, and return the results.
5. **Deploy the API**: Deploy the API on a web server or cloud platform like AWS or Heroku.

---

## Installation

To get started with the project, clone the repository and install the required dependencies.

### Clone the repository:
```bash
git clone https://github.com/yourusername/credit-risk-prediction.git
cd credit-risk-prediction
