# Data_Analysis_Project
Financial data analysis: preprocess, visualize, calculate technical indicators.

----
Based on the code provided, I've created a README file outlining the analysis performed. Here it is:

---

# Data Analysis Project README

## Introduction
This repository contains Python code for analyzing financial market data. The analysis includes various steps such as data preprocessing, visualization, calculation of technical indicators, and segmentation using change point detection algorithms.

## Requirements
- Python 3.x
- Libraries: pandas, numpy, matplotlib, seaborn, talib, ruptures

## Data
The dataset used in this analysis is stored in an Excel file named `tumhisse.xlsx`. It contains historical market data including open, high, low, close prices, and other relevant information.

## Analysis Steps

1. **Data Preprocessing**: The code begins with importing necessary libraries and reading the dataset using pandas.

2. **Data Cleaning**: The initial step involves checking for missing values and handling them. Forward fill method is used to fill missing values in the dataset.

3. **Data Visualization**: Various visualizations are generated to explore the data distribution and relationships between different variables. Histograms and scatter plots are utilized for this purpose.

4. **Technical Indicators Calculation**: Several technical indicators are calculated using the `talib` library, including:
   - Moving Average (MA-7)
   - Williams %R (willr)
   - Average Directional Movement Index (adx)
   - Relative Strength Index (rsi)
   - Linear Regression (linreg)
   - Momentum (momentum)
   - Exponential Moving Average (ema)
   - Commodity Channel Index (cci)

5. **Correlation Analysis**: A heatmap is created to visualize the correlation between different technical indicators.

6. **Change Point Detection**: Change point detection algorithm (PELT) from the `ruptures` library is applied to identify significant changes or breakpoints in the time series data.

7. **Data Segmentation**: The detected change points are visualized on the time series plot to segment the data based on significant changes.

8. **Conclusion**: The README file concludes with a note indicating the completion of the data analysis process.

## Conclusion
This README provides an overview of the data analysis project. For detailed implementation and code, please refer to the Python script provided in this repository.

---

Feel free to adjust or expand the README file according to your specific requirements or additional details you want to include!
