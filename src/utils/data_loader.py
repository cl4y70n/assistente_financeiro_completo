import pandas as pd

def load_data(path: str):
    try:
        return pd.read_csv(path)
    except Exception as e:
        raise ValueError(f"Erro ao carregar dados: {e}")
