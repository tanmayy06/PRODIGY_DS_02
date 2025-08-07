import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load the Titanic dataset (make sure the CSV is in the same folder as this .py file)
csv_path = os.path.join(script_dir, r'T:\task 2\train.csv')
df = pd.read_csv(csv_path)

# Display basic info
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Data Cleaning
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)  # Drop Cabin due to many missing values

# Convert categorical variables
df['Sex'] = df['Sex'].astype('category')
df['Embarked'] = df['Embarked'].astype('category')

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Helper function to save plots in script folder
def save_plot(fig_name):
    full_path = os.path.join(script_dir, fig_name)
    plt.savefig(full_path)
    print(f"Saved: {full_path}")
    plt.clf()

# Plot 1: Survival count
sns.countplot(x='Survived', data=df)
plt.title('Survival Count')
save_plot('survival_count.png')

# Plot 2: Survival by gender
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title('Survival by Gender')
save_plot('survival_by_gender.png')

# Plot 3: Age distribution
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')
save_plot('age_distribution.png')

# Plot 4: Survival by class
sns.countplot(x='Survived', hue='Pclass', data=df)
plt.title('Survival by Passenger Class')
save_plot('survival_by_class.png')

# Plot 5: Correlation heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
save_plot('correlation_heatmap.png')

print("\n✅ EDA completed. All plots saved in the same folder as this script.")
