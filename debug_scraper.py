# debug_scraper.py
from app.services.scraper import get_data_all_sections
import pandas as pd

print("🧪 TESTE 1: Caminho real do scraper usado")
print(get_data_all_sections.__code__.co_filename)

print("\n🔍 TESTE 2: Executando get_data_all_sections('importacao')...")
dados = get_data_all_sections("importacao")
print(f"✅ Registros carregados: {len(dados)}")
if dados:
    print("📦 Exemplo:")
    print(dados[0])
else:
    print("⚠️ Nenhum dado retornado.")

print("\n🔎 TESTE 3: Lendo CSV diretamente com pandas")
path = "data/fallback/importacao/ImpVinhos.csv"
df = pd.read_csv(path, sep="\t", encoding="utf-8", engine="python")
print(f"✅ Linhas no CSV: {len(df)}")
print("📌 Colunas detectadas:")
print(list(df.columns[:10]))
print("📌 Primeira linha:")
print(df.head(1))
