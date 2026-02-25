from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, to_date

def main():
    spark = SparkSession.builder \
        .appName("VendasDiarias") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    # Ler arquivos (mesma pasta do script)
    telefonia = spark.read.csv(
        "base_telefonia.csv",
        header=True,
        inferSchema=True
    )

    pessoas = spark.read.csv(
        "base_pessoas.csv",
        header=True,
        inferSchema=True
    )

    # Ajustar nomes de colunas problemáticas
    telefonia = telefonia.withColumnRenamed("Valor venda", "valor_venda")
    pessoas = pessoas.withColumnRenamed("Líder da Equipe", "lider_equipe")

    # Filtrar apenas vendas válidas
    vendas = telefonia \
        .filter(col("Motivo") == "Venda") \
        .filter(col("valor_venda").isNotNull()) \
        .withColumn("data", to_date("inicio_ligacao"))

    # Join para pegar liderança
    vendas_join = vendas.join(pessoas, "Username", "left")

    # Agregação
    resultado = vendas_join.groupBy("data", "lider_equipe") \
        .agg(sum("valor_venda").alias("total_vendas"))

    # Salvar parquet particionado
    resultado \
        .repartition("lider_equipe") \
        .write \
        .partitionBy("lider_equipe") \
        .mode("overwrite") \
        .parquet("output_vendas_diarias")

    print("Arquivo gerado com sucesso!")

    spark.stop()


if __name__ == "__main__":
    main()