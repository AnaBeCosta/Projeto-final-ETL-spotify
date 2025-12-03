# 🎵 Projeto ETL Spotify

## 📝 O que ele faz

Este projeto implementa um processo de **ETL (Extração, Transformação e Carga)** para dados do Spotify. O script principal lê dados de um arquivo CSV, realiza uma série de tratamentos e limpezas, e carrega o resultado em um banco de dados SQLite. O objetivo final é preparar os dados para análise e visualização em ferramentas de Business Intelligence como o Power BI.

- Link de acesso Power BI: https://escolatrabalhador4-my.sharepoint.com/:u:/r/personal/anabecosta_escoladotrabalhador40_com_br/Documents/projeto_final_spotify.pbix?csf=1&web=1&e=dht7oV

| Introdução | Visão Geral |
|---------|----------|
| <img src="https://github.com/user-attachments/assets/97682bc6-b1a4-4f6a-aeea-851203015705" width="400" /> | <img src="https://github.com/user-attachments/assets/da742e91-b9f9-48c1-8284-91349413e151" width="400" /> |

| Artistas | Popularidade |
|---------|----------|
| <img src="https://github.com/user-attachments/assets/1f1feb0b-00e4-42c3-a91a-33c15eafdac0" width="400" /> | <img src="https://github.com/user-attachments/assets/13c08180-5fc2-40b4-8264-2b63d1256eb0" width="400" /> |


## ✨ Funcionalidades

O processo ETL é dividido nas seguintes etapas:

1.  **Extração**: Os dados são lidos a partir de um arquivo CSV para um DataFrame do pandas.
2.  **Transformação**:
    *   Remove linhas duplicadas para garantir a consistência.
    *   Trata valores ausentes, removendo linhas ou preenchendo com "Não informado".
    *   Converte a coluna de data de lançamento do álbum (`album_release_date`) para o formato `DD/MM/YYYY`.
    *   Padroniza colunas de texto para letras minúsculas e remove espaços extras.
    *   Limpa caracteres especiais da coluna de gêneros (`artist_genres`), mantendo a estrutura de lista.
3.  **Carga**:
    *   Cria um banco de dados SQLite (`spotify.db`).
    *   Salva o DataFrame tratado em uma tabela chamada `spotify_data_clean` dentro do banco de dados.

## ⚙️ Dependências

Para executar o script de ETL, você precisará das seguintes bibliotecas Python:

*   `pandas`
*   `numpy`
*   `sqlite3`

## 📂 Arquivos Usados

*   `main.py`: O script principal que executa todo o processo de ETL.
*   `spotify_data_clean.csv`: O arquivo de entrada contendo os dados brutos do Spotify.
*   `spotify.db`: O banco de dados SQLite gerado como saída do processo, contendo os dados limpos e prontos para análise.

*   `README.md`: Este arquivo de documentação.

