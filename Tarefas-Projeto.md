## 🧩 Responsabilidades por Grupo — Preparação da Base para Análises

Para garantir que todas as visualizações do Power BI possam ser construídas corretamente, cada grupo deverá executar as seguintes etapas no processamento da base de dados.

---

## 👥 Grupo 1 — Limpeza + Transformação (4 pessoas)

Responsáveis por preparar e organizar toda a base para que as métricas e análises possam ser calculadas corretamente.

### 🧼 1. Limpeza dos Dados
- Remover valores nulos e duplicados.
- Padronizar:
  - Nomes de artistas (`artist_name`)
  - Formatos de data (`release_date`, `year`)
  - Gêneros musicais
  - Sexo dos artistas (M/F/Outro)
- Corrigir inconsistências:
  - Artistas escritos com variações.
  - Gêneros repetidos com grafias diferentes.
- Ajustar tipos de dados:
  - Numéricos → int/float  
  - Datas → datetime  
  - Categorias → string padronizada  

---

### 🔄 2. Transformações Necessárias
Criar as colunas e métricas essenciais para o BI:

#### Criar/ajustar:
- Coluna **ano** (se não existir).
- Coluna **quantidade de músicas por álbum**.
- Coluna **tempo em minutos** (opcional).
- Tabelas derivadas, como:
  - Tabela de artistas
  - Tabela de álbuns
  - Tabela de faixas

#### Gerar estatísticas e indicadores:
- Média da duração das músicas.
- Média de músicas por álbum por ano.
- Top 3 gêneros por período.
- Crescimento do número de lançamentos.
- Popularidade média por ano/artista.

---

### 📊 3. Garantir que as análises obrigatórias do Power BI sejam possíveis
O grupo deve confirmar que as informações estão prontas para:

- Moda do artista  
- Seguidores × popularidade  
- Evolução da popularidade  
- Artistas mais populares de 2025  
- Distribuição por gênero  
- Top 3 gêneros (2009–2023)  
- Crescimento anual de lançamentos  
- Duração média das faixas  
- Média de músicas por álbum  

---

## 🗃️ Grupo 2 — SQL + BI (3 pessoas)

Responsáveis pela modelagem, carga no banco, criação de views e preparação do Power BI.

### 🗄️ 1. Modelagem de Banco de Dados
Criar estrutura relacional:

- `artists`  
- `albums`  
- `tracks`  
- tabelas auxiliares (se necessário)

Com chaves:
- **PK** (chave primária)  
- **FK** (chave estrangeira)  

---

### 🧳 2. Carga dos Dados (L)
- Inserir todos os dados tratados no banco (SQLite ou PostgreSQL).
- Criar views otimizadas para o Power BI:
  - Popularidade ao longo do tempo  
  - Lançamentos por ano  
  - Artistas mais populares de 2025  
  - Top gêneros  
  - Seguidores × popularidade  
  - Distribuição por gênero  

---

### 📊 3. Power BI — Conexão e Métricas
- Conectar Power BI ao banco.
- Criar relacionamentos entre as tabelas.
- Criar medidas DAX (se necessárias).
- Montar gráficos e dashboards para responder aos 10 pontos obrigatórios.

---

## 🎯 Resultado Final Esperado

Ao final, o pipeline completo (ETL + SQL + BI) deve entregar:

- Dados limpos  
- Estrutura relacional consistente  
- Views prontas para visualização  
- Dashboard completo com todas as análises solicitadas