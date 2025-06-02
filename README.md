# Vitibrasil API

> API REST para acesso estruturado aos dados da vitivinicultura brasileira coletados da Embrapa.

## Problema que resolve

Os dados da vitivinicultura no Brasil estão dispersos em arquivos CSV escondidos em páginas HTML da Embrapa, dificultando sua utilização para análises, visualizações ou aplicações de Machine Learning. Esta API centraliza e estrutura essas informações para facilitar o consumo automatizado.

## Stack utilizada

* Python 3.13+
* Flask
* Flasgger (Swagger UI)
* requests + BeautifulSoup + pandas
* dotenv

## Estrutura do projeto

```
vitibrasil_api/
├── app/
│   ├── routes/            # Endpoints da API REST
│   ├── services/          # Web scraping + fallback
│   ├── config.py          # Configuração da API e paths
│   └── __init__.py        # Criação do app Flask
├── data/fallback/         # Arquivos CSV de fallback por tipo
├── requirements.txt       # Dependências do projeto
├── debug_scraper.py       # Script para depuração
└── README.md
```

## Endpoints principais

* `/producao`
* `/processamento`
* `/comercializacao`
* `/importacao`
* `/exportacao`

Todos aceitam:

```
?limit=10&offset=0&ano=2021&produto=Vinho&pais=Chile
```

(Opcional, conforme o tipo de dado)

## Como rodar localmente

```bash
# 1. Clone o repositório
$ git clone https://github.com/seunome/vitibrasil_api.git
$ cd vitibrasil_api

# 2. Crie o ambiente virtual
$ python -m venv venv
$ source venv/bin/activate     # Linux/macOS
$ .\venv\Scripts\activate      # Windows

# 3. Instale as dependências
$ pip install -r requirements.txt

# 4. Inicie a API
$ flask run

# 5. Acesse a documentação
http://localhost:5000/apidocs
```

## Variáveis de ambiente (.env)

```
FLASK_APP=app
FALLBACK_DIR=data/fallback
```

## Fallback garantido

Se o site da Embrapa estiver offline, a API automaticamente usa os CSVs cacheados em `data/fallback/<tipo>`.

## Como testar

```bash
$ python debug_scraper.py
```

Esse script testa leitura real + fallback de todos os tipos de dados.

## Deploy sugerido (Render)

* Suba o projeto para o GitHub
* Crie um novo web service no [Render](https://render.com/)
* Configure a build command:

```
pip install -r requirements.txt
```

* Start command:

```
flask run --host=0.0.0.0 --port=10000
```

* Configure env vars (.env)

## Diagrama da arquitetura

**Fonte** (site da Embrapa)
↳ **Web Scraper** (`requests`, `BeautifulSoup`, `pandas`)
↳ **Fallback local** (CSVs salvos)
↳ **API Flask REST** (`/producao`, `/exportacao`...)
↳ **Swagger UI** (`/apidocs`)
↳ **Usuário** ou **aplicativo externo**
↳ **Futura pipeline de ML / dashboard**

---

**Vitibrasil API** - Desenvolvido para a disciplina de Machine Learning Engineering (FIAP)
