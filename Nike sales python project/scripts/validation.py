def validate_data(df):
    print("verification apres traitement\n")
    print("Valeurs manquantes restantes :")
    print(df.isnull().sum())
    print("\nTypes de donnees :")
    print(df.dtypes)
    # Vérifier les valeurs négatives uniquement dans les colonnes numériques
    numeric_cols=df.select_dtypes(include=['float64', 'int64']).columns
    print("\nValeurs negatives dans les colonnes numeriques")
    print((df[numeric_cols] < 0).sum())
