import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_data(df):
    numeric_df=df.select_dtypes(include=['int64', 'float64'])

    # Heatmap des correlations
    corr=numeric_df.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Matrice de corrélation des colonnes numériques")
    plt.show()

    # Histogramme revenue
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Revenue'], bins=30, kde=True, color='blue')
    plt.title("Distribution de Revenue")
    plt.show()

    # Barplot revenue par produit
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Produit', y='Revenue', data=df, estimator=sum, ci=None, palette='viridis')
    plt.title("Revenue total par Produit")
    plt.ylabel("Revenue")
    plt.xlabel("Produit")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(6,4))
    sns.histplot(df['Units_Sold'], kde=True)  #hist+densite
    plt.title("Distribution des unites vendues")
    plt.show()
    
    print("Visualisation terminee")

