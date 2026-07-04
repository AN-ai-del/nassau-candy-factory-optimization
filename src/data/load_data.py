from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "factory_sales_feature_engineered.csv"


def load_processed_data() -> pd.DataFrame:
    """
    Load the feature-engineered factory sales dataset.
    """
    return pd.read_csv(PROCESSED_DATA_PATH)