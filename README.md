Data Cleaning & Exploratory Data Analysis (EDA)
📌 Overview
This project performs data cleaning and exploratory data analysis (EDA) on the famous Titanic dataset from Kaggle.
The goal is to explore relationships between different features and identify patterns & trends that may have influenced passenger survival.

Key steps include:

Handling missing values

Converting categorical variables to appropriate data types

Removing irrelevant features

Creating insightful visualizations

📂 Files in This Project
train.csv → Titanic dataset (from Kaggle)

titanic_eda.py → Python script containing the data cleaning & EDA code

survival_count.png → Bar chart of survival count

survival_by_gender.png → Survival comparison between genders

age_distribution.png → Age distribution of passengers

survival_by_class.png → Survival comparison between passenger classes

correlation_heatmap.png → Correlation heatmap of numeric features

📜 Requirements
Install dependencies before running:

bash
Copy
Edit
pip install pandas seaborn matplotlib

🖥️ How to Run
Clone this repository:

bash
Copy
Edit
git clone https://github.com/<your-username>/<your-repo-name>.git
Navigate to the project folder:

bash
Copy
Edit
cd <your-repo-name>
Place train.csv in the same folder as titanic_eda.py.

Run the script:

bash
Copy
Edit
python titanic_eda.py
All generated plots will be saved in the same folder as the script.

🔍 Code Workflow
1️⃣ Data Loading & Inspection
Load dataset with Pandas

View dataset info & missing values

2️⃣ Data Cleaning
Fill missing Age with median

Fill missing Embarked with mode

Drop Cabin column due to too many missing values

Convert categorical variables (Sex, Embarked)

3️⃣ Exploratory Data Analysis (EDA)
Generated visualizations include:

Survival Count


Survival by Gender


Age Distribution


Survival by Passenger Class


Correlation Heatmap


✨ Insights from EDA
Women had a much higher survival rate than men.

First-class passengers had the highest survival rate.

Younger passengers had slightly higher chances of survival.

Passenger class and gender are strongly related to survival.

👨‍💻 Author
Tanmay Gupta
Data Science Intern
