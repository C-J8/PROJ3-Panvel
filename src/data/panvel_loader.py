import pandas as pd 
from pathlib import Path
import requests

class Dataloader:
    def __init__(self):
        self.base_url = "https://bkt-panvel-puc-projcd.s3.amazonaws.com/project-puc/"
        self.files = ["devolucoes.parquet", "filiais.parquet", "metas.parquet", "vendas.parquet", "filiais_dt_abertura.parquet"]
        
    def load_file(self, filename:str) -> pd.DataFrame:
        """It can be devolucoes.parquet, filiais.parquet, metas.parquet, vendas.parquet"""
        return pd.read_parquet(self.base_url+filename)
    
    def load_dataset(self):
        dataset = {}
        for file in self.files:
            name = file.split(".")[0]
            df = self.load_file(file)
            dataset[name] = df
        return dataset
    
    def download(self, dir):
        dir = Path(dir)
        dir.mkdir(parents=True, exist_ok=True)
        for file in self.files:
            target_path = dir / file
            if not target_path.exists():
                print(f"Downloading {file}")
                response = requests.get(self.base_url + file)
                response.raise_for_status()
                with open(target_path, "wb") as f:
                    f.write(response.content)
            else:
                print(f"Skipping {file} already exist")
                
        return True