"""
Download do dataset Olist via Kaggle API.

Setup:
    1. pip install kaggle
    2. Acesse kaggle.com/settings > API > Create New Token
    3. Salve o access_token em ~/.kaggle/access_token
    4. Execute: python src/download_data.py
"""
import os
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

DATASET = "olistbr/brazilian-ecommerce"


def download():
    kaggle_json  = Path.home() / ".kaggle" / "kaggle.json"
    kaggle_token = Path.home() / ".kaggle" / "access_token"

    if not kaggle_json.exists() and not kaggle_token.exists():
        print("Credenciais não encontradas em ~/.kaggle/")
        print("Acesse kaggle.com/settings > API > Create New Token")
        return

    if kaggle_token.exists() and not kaggle_json.exists():
        os.environ["KAGGLE_TOKEN"] = kaggle_token.read_text().strip()

    os.system(f'kaggle datasets download -d {DATASET} -p "{RAW_DIR}" --unzip')

    csvs = sorted(RAW_DIR.glob("*.csv"))
    print(f"\n{len(csvs)} arquivos em {RAW_DIR}:")
    for f in csvs:
        print(f"  {f.name:55s} {f.stat().st_size / 1_048_576:.1f} MB")


if __name__ == "__main__":
    download()
