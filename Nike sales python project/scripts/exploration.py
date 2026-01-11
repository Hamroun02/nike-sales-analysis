import matplotlib.pyplot as plt
import seaborn as sns

def explore_data(df):
    print("informations generales sur le dataset")
    print(df.info())
    print("\n Statistiques descriptives")
    print(df.describe(include='all'))
    print("\n Valeurs manquantes par colonne")
    print(df.isnull().sum())

    
    plt.figure(figsize=(6,4))
    sns.histplot(df['Units_Sold'], kde=True)  #hist+densite
    plt.title("distribution des unites vendues")
    plt.show()
