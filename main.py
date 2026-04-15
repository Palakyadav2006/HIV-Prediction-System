import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# STEP 1: Load Dataset
data = pd.read_csv("hiv_dataset.csv")

print("Columns:")
print(data.columns)

print("\nOriginal Data:")
print(data.head())

# STEP 2: Select correct columns (based on your file)
data = data[['Location', 'Period', 'FactValueNumeric']]

# Rename columns
data.columns = ['Country', 'Year', 'HIV_Prevalence']

# Remove missing values
data = data.dropna()

print("\nCleaned Data:")
print(data.head())

# STEP 3: Create ML Features
data['Age'] = np.random.randint(20, 60, size=len(data))
data['CD4_Count'] = np.random.randint(50, 600, size=len(data))
data['Viral_Load'] = np.random.randint(1000, 100000, size=len(data))

# Target variable
data['Health_Status'] = data['CD4_Count'].apply(lambda x: 1 if x < 200 else 0)

print("\nFinal Dataset:")
print(data.head())

# STEP 4: Train Model
X = data[['Age', 'CD4_Count', 'Viral_Load']]
y = data['Health_Status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("\nModel Accuracy:", accuracy)

# STEP 5: Graphs

from graphs.scatter_plot import plot_scatter
from graphs.bar_chart import plot_bar
from graphs.histogram import plot_histogram
from graphs.line_chart import plot_line
from graphs.box_plot import plot_box

plot_scatter(data)
plot_bar(data)
plot_histogram(data)
plot_line(data)
plot_box(data)

