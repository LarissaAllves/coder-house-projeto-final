

from plyer import notification
from datetime import datetime
import pandas as pd
import requests
from datetime import datetime
import sqlite3

# alert


def alert(level, base, stage):

    if level == 1:
        title = "Alerta Baixo"
    elif level == 2:
        title = "Alerta Médio"
    else:
        title = "Alerta Alto"

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"Falha no carregamento da base {
        base} na fase de {stage}. Data: {current_date}"

    notification.notify(
        title=title,
        message=message,
        app_name="Rick and Morty API",
        timeout=10
    )

# cat api


def get_data_api(url, base, stage):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            alert(level=3, base=base, etapa=stage)

    except requests.RequestException as e:
        alert(level=3, base=base, stage=stage)
        print(f"Erro ao acessar a API: {e}")
        return None


def convert_date(date_str):
    return datetime.strptime(date_str, '%B %d, %Y').strftime('%d/%m/%Y')


def replace_urls_with_names(df, url_column, name_column, urls):

    url_to_name = dict(zip(df[url_column], df[name_column]))
    return [url_to_name.get(url, "Unknown") for url in urls]


# Função para listar as tabelas do banco de dados

def list_tables_bd(path_db, base, stage):
    try:
        with sqlite3.connect(path_db) as conn:
            query = "SELECT name FROM sqlite_master WHERE type='table';"
            tables = pd.read_sql(query, conn)
        return tables
    except sqlite3.Error as e:
        alert(level=3, base=base, stage=stage)
        print(f"Erro ao acessar a API: {e}")
        return None


# Função para salvar um dataframe no banco de dados

def bd_save(df, path_db, table_name, base, stage):

    try:
        with sqlite3.connect(path_db) as conn:
            df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Dados importados com sucesso na tabela '{
            table_name}' do banco '{path_db}'")
    except sqlite3.Error as e:
        alert(level=3, base=base, stage=stage)
        print(f"Erro ao acessar a API: {e}")
        return None

# carregar bd


def load_bd(table_name, path_db, base, stage):

    try:
        with sqlite3.connect(path_db) as conn:
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, conn)
        return df
    except sqlite3.Error as e:
        alert(level=3, base=base, stage=stage)
        print(f"Erro ao acessar a API: {e}")
        return None
