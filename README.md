![Descrição da Imagem](https://repository-images.githubusercontent.com/120371205/b6740400-92d4-11ea-8a13-d5f6e0558e9b)

# 🎯 RICK AND MORTY API

Este projeto tem como objetivo coletar, processar e analisar os dados da [Rick and Morty API](https://rickandmortyapi.com/documentation/#rest)

## **📊 Bases de dados**

[Character](https://rickandmortyapi.com/documentation/#character): usado para obter todos os personagens
[Location](https://rickandmortyapi.com/documentation/#location): usado para obter todos os locais
[Episode](https://rickandmortyapi.com/documentation/#episode)"usado para obter todos os episódios

## **🛠️ Ferramentas e bibliotecas utilizadas**

- **`Python`**: Linguagem de programação usada no projeto.
- **`Jupyter`**: Usado para análises e experimentação.
- **`plyer`**: Para criar notificações no sistema operacional;
- **`datetime`**: Usado para manipular e formatar datas e horários;
- **`pandas`**: Manipulação e análise de dados em tabelas;
- **`requests`**: Para fazer solicitações HTTP e consumir a API;
- **`sqlite3`**: Utilizado para armazenar e recuperar os dados.
- **`matplotlib`**: Para criar visualizações e gráficos.

## 📁 **Estrutura do Projeto**

- **`/pycache/`**: Pasta automática do Python para arquivos compilados.
- **`.venv/`** e **`myenv/`**: Ambientes virtuais do projeto.
- **`.gitignore`**: Para especificar quais arquivos devem ser ignorados pelo Git.
- **`functions.py`**: Contém as funções principais utilizadas.
- **`README.md`**: Documentação do projeto.
- **`requirements.txt`**: Lista das dependências necessárias para rodar o projeto.
- **`rick-and-morty.ipynb`**: Arquivo principal.

## 🚀 **Etapa de Instalação**

Siga os passos abaixo para configurar e executar o projeto localmente:

#### 1. Clone o projeto

```bash
# Clone o projeto para o seu ambiente local:
git clone git@github.com:LarissaAllves/coder-house-projeto-final.git
```

#### 2. Instale as Dependências

```bash
# Instale todas as dependências do projeto listadas no `requirements.txt`
  pip install -r requirements.txt
```

### 3. Verifique a Instalação

```bash
#Para verificar se todas as dependências foram instaladas corretamente, você pode executar

pip freeze

## Abra o arquivo rick_and_morty.ipynb e explore
```

## 🧵 Tratamento e Análise dos Dados

### 📊 **Exemplo do DataFrame `Characters`**

<table border="1" cellspacing="0" cellpadding="5">
    <tr>
        <th>id</th>
        <th>name</th>
        <th>status</th>
        <th>species</th>
        <th>type</th>
        <th>gender</th>
        <th>origin</th>
        <th>location</th>
        <th>image</th>
        <th>episode</th>
        <th>url</th>
        <th>created</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Rick Sanchez</td>
        <td>Alive</td>
        <td>Human</td>
        <td></td>
        <td>Male</td>
        <td>{'name': 'Earth (C-137)', 'url': 'https://rick...'}</td>
        <td>{'name': 'Citadel of Ricks', 'url': 'https://r...'}</td>
        <td>{"https://rickandmortyapi.com/api/character/avatar}</td>
        <td>{https://rickandmortyapi.com/api/episode/1}</td>
        <td>{https://rickandmortyapi.com/api/character/1}</td>
        <td>2017-11-04T18:48:46.250Z</td>
    </tr>
</table>

### 🔍 **Principais Transformações**

1. **Substituição de Valores Vazios**

   - Valores vazios na coluna `type` foram substituídos por `"unknown"`.

2. **Separação das Informações de `origin` e `location` em Colunas Distintas**

   - Foram criadas colunas adicionais:
     - `name_origin` e `url_origin` para os detalhes do `origin`.
     - `location_name` e `url_location` para os detalhes do `location`.

3. **Criação de uma Nova Coluna com o Total de Episódios**

   - Adição da coluna `total_episodes` que contém a quantidade total de episódios em que cada personagem aparece.

4. **Renomeação da Coluna `url`**

   - A coluna `url` foi renomeada para `character_url` para melhorar a clareza e especificidade das informações.

5. **Exclusão das Colunas Desnecessárias**
   - As colunas `origin`, `location`, `created` e `episode` foram removidas

### 📊 **Exemplo do DataFrame `Locations`**

<table border="1" cellspacing="0" cellpadding="5">
    <tr>
        <th>id</th>
        <th>name</th>
        <th>type</th>
        <th>dimension</th>
        <th>residents</th>
        <th>url</th>
        <th>created</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Earth (C-137)</td>
        <td>Planet</td>
        <td>Dimension C-137</td>
        <td>
            <{"https://rickandmortyapi.com/api/character/38"}>
        </td>
        <td><{"https://rickandmortyapi.com/api/location/1"}</td>
        <td>2017-11-10T12:42:04.162Z</td>
    </tr>
</table>

### 🔍 **Principais Transformações**

1. **Renomeação da Coluna `residents` e `url`**

   - A coluna `residents` foi renomeada para `residents_name` e `url` para `url_locations` para melhorar a clareza das informações.

2. **Substituição das URLs na coluna `residents` por Nomes dos Characters**

   - Os links em `residents_name` foram substituídos pelos nomes dos personagens correspondentes.

3. **Criação da Coluna `total_residents`**

   - Adição da coluna `total_residents` que contém o número total de residentes de cada localização.

4. **Exclusão da Coluna `created`**
   - A coluna `created` foi removida, pois não é necessária para as análises.

### 📊 **Exemplo do DataFrame `Episodes`**

  <table border="1" cellspacing="0" cellpadding="5">
    <tr>
        <th>id</th>
        <th>name</th>
        <th>air_date</th>
        <th>episode</th>
        <th>characters</th>
        <th>url</th>
        <th>created</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Pilot</td>
        <td>December 2, 2013</td>
        <td>S01E01</td>
        <td>
            <{"https://rickandmortyapi.com/api/character/1"}>
        </td>
        <td>{"https://rickandmortyapi.com/api/episode/1"}</td>
        <td>2017-11-10T12:56:33.798Z</td>
    </tr>
</table>

### 🔍 **Principais Transformações**

1. **Renomeação das Colunas**

   - A coluna `characters` foi renomeada para `characters_name`.
   - A coluna `url` foi renomeada para `episode_url`.

2. **Formatação das Datas**

   - A data na coluna `air_date` foi transformada para o formato **dd/mm/yyyy**.

3. **Substituição das URLs pelos Nomes dos Characters**

   - Na coluna `characters_name`, as URLs foram substituídas pelos nomes dos personagens.

4. **Criação da Coluna `total_characters_in_the_episode`**
   - Criação da coluna `total_characters_in_the_episode`, contendo o número total de personagens presentes em cada episódio.

## 🚀 **Conclusão**

A estrutura dos dados foi organizada para facilitar as análises e a geração de insights relevantes sobre personagens, locais e episódios.

---
