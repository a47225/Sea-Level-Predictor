import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x="Year",y="CSIRO Adjusted Sea Level",data=df)

    # Create first line of best fit
    slope = linregress(x=df["Year"],y=df["CSIRO Adjusted Sea Level"]).slope
    intercept = linregress(x=df["Year"],y=df["CSIRO Adjusted Sea Level"]).intercept
    list_predict = []
    for i in range(df["Year"].values[-1] + 1,2051):
        list_predict.append(i)
    df_predict=pd.Series(list_predict)
    df_predict = pd.concat([df["Year"],df_predict],ignore_index=True)
    plt.plot(df_predict,intercept + slope*df_predict,'g')

    # Create second line of best fit
    df_after2000=df.loc[df["Year"]>=2000]
    df_after2000 = df_after2000.reset_index()
    df_after2000.drop("index",axis=1)

    slope2000 = linregress(x=df_after2000["Year"],y=df_after2000["CSIRO Adjusted Sea Level"]).slope
    intercept2000 = linregress(x=df_after2000["Year"],y=df_after2000["CSIRO Adjusted Sea Level"]).intercept

    list_predict2000 = []
    for i in range(df_after2000["Year"].values[-1] + 1,2051):
        list_predict2000.append(i)
    df_predict2000 = pd.Series(list_predict2000)
    df_predict2000 = pd.concat([df_after2000["Year"],df_predict2000],ignore_index=True)

    plt.plot(df_predict2000,intercept2000 + slope2000*df_predict2000,'r')
    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")


    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()