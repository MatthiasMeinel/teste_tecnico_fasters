# teste_tecnico_fasters

📊 Análise de Performance Comercial e Ligações – PySpark
📌 Visão Geral do Projeto

Este projeto realiza uma análise exploratória de dados (EDA) utilizando PySpark, com foco na avaliação de performance comercial e indicadores operacionais de uma base de telefonia.

O objetivo foi extrair KPIs de negócio, validar a qualidade dos dados e gerar insights sobre desempenho de vendedores e padrão de atendimento.

🗂 Bases Utilizadas

Foram analisadas três bases de dados:

base_avaliacoes.csv

base_pessoas.csv

base_telefonia.csv

Essas bases contêm informações sobre:

Vendas realizadas

Colaboradores

Registros de ligações (início e fim)

📈 Principais Resultados
🏆 Top 5 Vendedores por Volume Total

Foram identificados os cinco colaboradores com maior volume financeiro em vendas, permitindo visualizar a concentração de receita e os principais destaques comerciais.

💰 Ticket Médio por Vendedor

Foi calculado o ticket médio individual, possibilitando comparar:

Vendedores com maior volume total

Vendedores com maior valor médio por venda

Essa análise evidencia diferentes perfis de performance comercial.

📞 Análise de Duração das Ligações

Identificados 2 registros inconsistentes com duração negativa.

Após tratamento, foi calculado o tempo médio das ligações válidas:

Tempo médio: 9,92 minutos

Esse indicador pode servir como benchmark operacional.

🧹 Validação e Qualidade dos Dados

Durante a análise foram realizadas verificações como:

Conversão correta de timestamps

Identificação de registros inconsistentes

Filtragem de dados inválidos

Garantia de consistência para cálculo de KPIs

🛠 Tecnologias Utilizadas

Python

PySpark

Spark SQL

Jupyter Notebook
