import pandas as pd

path = "data/fallback/importacao/ImpVinhos.csv"
print(f"\n📄 Lendo arquivo: {path}\n")

# Lê o CSV
df = pd.read_csv(path, sep="\t", encoding="utf-8", engine="python")
df.columns = [c.strip() for c in df.columns]

anos = sorted(set(c.split('.')[0] for c in df.columns if c[:4].isdigit()))
print(f"🕐 Anos detectados: {anos[:5]}... (+{len(anos)} anos no total)\n")

total_registros = 0

# Itera sobre o DataFrame
for idx, row in df.iterrows():
    row_dict = row.to_dict()
    id_pais = f"{row_dict.get('Id')} - {row_dict.get('País')}"
    registros_validos = 0

    for ano in anos:
        col_qtd = ano
        col_val = ano + ".1"

        qtd = row_dict.get(col_qtd)
        val = row_dict.get(col_val)

        if (qtd is None and val is None):
            continue

        try:
            qtd = float(str(qtd).replace(".", "").replace(",", "").strip()) if qtd != '' else 0
            val = float(str(val).replace(".", "").replace(",", "").strip()) if val != '' else 0
        except:
            continue

        if qtd != 0 or val != 0:
            registros_validos += 1
            print(f"[{id_pais}] Ano {ano}: Quantidade={qtd}, Valor={val}")

    if registros_validos > 0:
        total_registros += registros_validos

print(f"\n✅ TOTAL de registros válidos encontrados: {total_registros}")
