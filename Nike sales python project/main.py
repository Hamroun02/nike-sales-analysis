from scripts.load_data import load_dataset
from scripts.exploration import explore_data
from scripts.preprocessing import preprocess_data
from scripts.validation import validate_data
from scripts.visualization import visualize_data
from scripts.export_data import export_clean_data  

DATA_PATH = r"C:\Users\lenovo\Desktop\Les projets\Nike sales python project\Nike sales python project\data\raw\nike_sales_uncleaned.csv"
EXPORT_PATH = r"C:\Users\lenovo\Desktop\Les projets\Nike sales python project\Nike sales python project\data\processed\nike_sales_cleaned.csv"

def main():
    df = load_dataset(DATA_PATH)
    explore_data(df)
    df_cleaned = preprocess_data(df)
    validate_data(df_cleaned)
    visualize_data(df_cleaned)
    export_clean_data(df_cleaned, EXPORT_PATH)




main()
