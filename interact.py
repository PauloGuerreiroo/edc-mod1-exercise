import boto3
import pandas as pd 

#Criar cliente para interagir com a aws s3
s3_client = boto3.client('s3')
s3_client.download_file("datalake-guerreirodev",
                        "raw-data/aluno.csv",
                        "CURSOIGTI/aluno.csv")

df = pd.read_csv("./aluno.csv",sep=";")
print(df)
