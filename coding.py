"""
Simple Python script for Git practice
Author: Sudhir
Purpose: Basic data analysis example
"""

import pandas as pd


def create_dataframe():
    data = {
        "Name": ["Amit", "Ravi", "Neha", "Pooja"],
        "Age": [25, 30, 28, 26],
        "Salary": [50000, 70000, 65000, 52000]
    }
    return pd.DataFrame(data)


def analyze_data(df):
    print("DataFrame:\n", df)
    print("\nAverage Age:", df["Age"].mean())
    print("Average Salary:", df["Salary"].mean())


if __name__ == "__main__":
    df = create_dataframe()
    analyze_data(df)
