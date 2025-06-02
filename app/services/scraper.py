import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
from app.config import Config

URLS = {
    'producao': 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02',
    'processamento': 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03',
    'comercializacao': 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04',
    'importacao': 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05',
    'exportacao': 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06',
}

def baixar_csvs(tipo):
    fallback_dir = os.path.join(Config.FALLBACK_DIR, tipo)
    os.makedirs(fallback_dir, exist_ok=True)

    url = URLS[tipo]
    print(f"[INFO] Tentando acessar Embrapa: {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)
        csv_links = [l['href'] for l in links if l['href'].endswith('.csv')]

        for link in csv_links:
            nome = link.split('/')[-1]
            path = os.path.join(fallback_dir, nome)

            if not os.path.exists(path):
                csv_url = f"http://vitibrasil.cnpuv.embrapa.br/{link}"
                print(f"[INFO] Baixando arquivo: {csv_url}")
                r = requests.get(csv_url, timeout=10)
                with open(path, 'wb') as f:
                    f.write(r.content)

    except Exception as e:
        print(f"[ERRO] Falha ao acessar Embrapa: {e}")
        print(f"[INFO] Usando fallback local em: {fallback_dir}")

    return fallback_dir

def parse_num(val):
    try:
        if isinstance(val, (int, float)):
            return float(val)
        raw = str(val).strip().replace(".", "").replace(",", "")
        return float(raw)
    except:
        return None

def get_data_all_sections(tipo):
    tipo = tipo.lower().strip()
    print(f"[DEBUG] Tipo recebido: '{tipo}'")
    print(f"[DEBUG] Tipos esperados: {list(URLS.keys())}")

    dir_path = baixar_csvs(tipo)
    dados = []
    total_lidos = 0

    for file in os.listdir(dir_path):
        if file.endswith('.csv'):
            path = os.path.join(dir_path, file)
            try:
                if tipo in ["exportacao", "importacao"]:
                    print(f"[DEBUG] Iniciando leitura de {tipo}: {file}")
                    df = pd.read_csv(path, sep="\t", encoding="utf-8", engine="python")
                    df.columns = [c.strip() for c in df.columns]

                    anos = sorted(set(c.split('.')[0] for c in df.columns if c[:4].isdigit()))

                    for _, row in df.iterrows():
                        row_dict = row.to_dict()

                        for ano in anos:
                            col_qtd = ano
                            col_val = ano + '.1'

                            qtd = parse_num(row_dict.get(col_qtd))
                            val = parse_num(row_dict.get(col_val))

                            if pd.isna(qtd) and pd.isna(val):
                                continue

                            registro = {
                                "ano": int(ano),
                                "quantidade": qtd if not pd.isna(qtd) else 0,
                                "valor": val if not pd.isna(val) else 0,
                                "arquivo": file
                            }

                            for campo in ['Id', 'País']:
                                if campo in row_dict:
                                    registro[campo.lower()] = row_dict[campo]

                            dados.append(registro)
                            total_lidos += 1

                    print(f"[DEBUG] Registros adicionados: {total_lidos}")

                else:
                    try:
                        df = pd.read_csv(path, sep=';', encoding='latin1')
                    except Exception:
                        df = pd.read_csv(path, sep='\t', encoding='utf-8', engine='python')

                    df.columns = [c.strip() for c in df.columns]

                    id_vars = [col for col in df.columns if not col.isdigit()]
                    value_vars = [col for col in df.columns if col.isdigit()]

                    df_melted = df.melt(
                        id_vars=id_vars,
                        value_vars=value_vars,
                        var_name='ano',
                        value_name='quantidade'
                    )

                    df_melted['ano'] = df_melted['ano'].astype(str).str.strip()
                    df_melted['quantidade'] = df_melted['quantidade'].fillna(0)
                    df_melted['arquivo'] = file

                    dados.extend(df_melted.to_dict(orient='records'))

            except Exception as e:
                print(f"[ERRO] Falha ao processar {file}: {e}")

    print(f"[DEBUG] Total final de registros retornados: {len(dados)}")
    return dados
