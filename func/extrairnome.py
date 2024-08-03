import pandas as pd
import os

def find_partition(formatocpf: str) -> str:
    directory = "D:/Ferramentas/DB FULL/partitions"
    for file_name in os.listdir(directory):
        if file_name.endswith(".csv"):
            start, end = file_name.replace(".csv", "").split("-")
            if start <= formatocpf <= end:
                return os.path.join(directory, file_name)
    raise FileNotFoundError("Partition not found")

def extrair_nome(formatocpf: str) -> str:
    partition_file = find_partition(formatocpf)
    df = pd.read_csv(partition_file, dtype={"CPF": str})
    result = df[df["CPF"] == formatocpf]
    if not result.empty:
        nome = result.iloc[0]["Nome Completo"]
        return nome
    else:
        raise ValueError("CPF not found")
