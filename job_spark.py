from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession
spark=(
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)
#leitura dos dados
enem = (
        spark
        .read
        .format("csv")
        .option("header", True)
        .option("inferSchema",True)
        .option("delimiter",";")
        .load("s3://datalake-guerreirodev/raw-data/")
)
(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save("s3://datalake-guerreirodev/staging/enem")
)