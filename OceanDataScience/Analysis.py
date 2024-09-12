from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import time

chromedriver_path = "C:\Documents\chromedriver-win64\chromedriver-win64\chromedriver.exe"
chrome_options = Options()
service = Service(chromedriver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://climatereanalyzer.org/clim/sst_daily/")

time.sleep(5)

sst_data_url = "https://climatereanalyzer.org/clim/sst_daily/json/oisst2.1_world2_sst_day.json"

response_sst = requests.get(sst_data_url)

if response_sst.status_code == 200:
    sst_data = response_sst.json()
    sst_df = pd.DataFrame(sst_data)

    sst_df["average_temperature"] = sst_df["data"].apply(
        lambda x: pd.Series(x).mean())

    sst_df["year"] = pd.to_numeric(sst_df["name"], errors="coerce")

    sst_df.dropna(subset=["year"], inplace=True)

    sst_df["year"] = sst_df["name"].astype(int)

    print("\nSea Surface Temperature Data (first few rows):")
    print(sst_df[["name", "average_temperature"]].head())

    plt.figure(figsize=(10, 6))
    sns.lineplot(
        x=sst_df["name"], y=sst_df["average_temperature"], marker="o", label="Avg SST")
    plt.title("Average Sea Surface Temperature Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Average SST (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    X = sst_df[["year"]]
    y = sst_df["average_temperature"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"\nModel Evaluation:\nMean Squared Error: {mse}\nR-squared: {r2}")

    plt.figure(figsize=(10, 6))
    plt.scatter(X_test, y_test, color="blue", label="Actual")
    plt.plot(X_test, y_pred, color="red", linewidth=2, label="Predicted")
    plt.title("Average vs Predicted Sea Surface Temperature")
    plt.xlabel("Year")
    plt.ylabel("Average SST (°C)")
    plt.legend()
    plt.show()

else:
    print(f"Failed to fetch data. Status code: {response_sst.status_code}")

driver.quit()
