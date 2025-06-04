# Vitibrasil API

API REST construída em Flask para centralizar os dados públicos da vitivinicultura no Brasil, extraídos do site da Embrapa. Esta API organiza e entrega dados de produção, processamento, comercialização, exportação e importação de uvas e vinhos em formato estruturado e documentado via Swagger.

## Objetivo

Fornecer uma API pública confiável com dados históricos da vitivinicultura brasileira, permitindo futuras análises, visualizações e desenvolvimento de modelos preditivos de Machine Learning para:

- Prever produção e consumo;
- Identificar tendências de importação/exportação;
- Avaliar sazonalidade e comportamento de mercado.

---

## Principais Funcionalidades

- Coleta de dados via Web Scraping com fallback para arquivos CSV;
- API REST com rotas separadas para cada tipo de dado;
- Documentação completa em Swagger (Flasgger);
- Deploy público via Render;
- Suporte a filtros e paginação;
- Estrutura modular e pronta para expansão.

---

## Tecnologias Utilizadas

- **Linguagem**: Python 3
- **Framework**: Flask
- **Scraping**: requests, BeautifulSoup, pandas
- **Documentação**: Swagger (via Flasgger)
- **Deploy**: Render (produção pública)
- **Outros**: gunicorn, python-dotenv

---

## Endpoints Disponíveis

Cada endpoint retorna dados estruturados com filtros por ano, produto, país, cultivar, etc.

- `/producao`
- `/processamento`
- `/comercializacao`
- `/importacao`
- `/exportacao`

A documentação interativa está disponível em:
https://vitibrasil-api-rmzy.onrender.com/apidocs

---

## Como rodar localmente

```bash
1. Clone o projeto

git clone https://github.com/SEU_USUARIO/vitibrasil_api.git
cd vitibrasil_api

2. Crie e ative o ambiente virtual

python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

3. Instale as dependências

pip install -r requirements.txt

4. Execute o servidor local

python run.py

Acesse em: http://localhost:5000/apidocs

## Estrutura do projeto

vitibrasil_api/
│
├── app/
│   ├── routes/        # Rotas por seção (produção, importação, etc.)
│   ├── services/      # Scraper, helpers e lógica
│   ├── config.py      # Variáveis globais
│   └── __init__.py    # Criação do app Flask
│
├── data/              # Fallback local (.csv)
│
├── run.py             # Entry point da aplicação
├── requirements.txt   # Pacotes e dependências
└── README.md
```

## Link para o vídeo e diagrama

https://drive.google.com/drive/folders/13PDYRtId121lKwG8U4mbZ_akRmTkcpqg?usp=drive_link


## Autor

Projeto acadêmico desenvolvido por Alexandre Mazzini na pós-graduação de Machine Learning Engineering — FIAP.

Link para acesso à API em produção:
https://vitibrasil-api-rmzy.onrender.com/apidocs
