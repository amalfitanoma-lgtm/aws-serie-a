import boto3
import pandas as pd
from io import StringIO

# CREDENZIALI AWS
s3 = boto3.client(
    's3',
    aws_access_key_id='Key',
    aws_secret_access_key='Key',
    region_name='eu-north-1'
)

print("Connessione AWS riuscita")

# EXTRACT - legge il CSV da S3
bucket_name = 'serie-a-matteo'
file_name = 'Football teams.csv'

response = s3.get_object(Bucket=bucket_name, Key=file_name)
csv_content = response['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(csv_content))

print('File letto da S3')
# print(df.head())

# TRASFORM
serie_a = df[df ['Tournament'] == 'Serie A']
serie_a = serie_a.dropna()
serie_a['cartellini_totali'] = serie_a['yellow_cards'] + serie_a['red_cards']
serie_a = serie_a.sort_values('Goals', ascending=False).reset_index(drop=True)

print(f'\nSquadre Serie A: {len(serie_a)}')
print(serie_a[['Team', 'Goals', 'cartellini_totali']].head())

# LOAD
csv_buffer = StringIO()
serie_a.to_csv(csv_buffer, index=False)

s3.put_object(
    Bucket = bucket_name,
    Key = 'serie_a_pulita.csv',
    Body = csv_buffer.getvalue()
)

print('\nFile salvato su S3')