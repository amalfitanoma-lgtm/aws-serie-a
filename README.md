# ETL Pipeline Serie A — AWS S3

Pipeline ETL per l'analisi delle statistiche delle squadre di Serie A, con archiviazione su AWS S3.

## Descrizione

Questo progetto implementa una pipeline ETL che interagisce con AWS S3:
- **Extract** → legge il CSV direttamente da un bucket S3
- **Transform** → filtra la Serie A, pulisce i dati e aggiunge metriche calcolate
- **Load** → carica il risultato finale su S3

## Tecnologie utilizzate

- Python 3
- Pandas
- Boto3 (AWS SDK per Python)
- AWS S3

## Trasformazioni applicate

- Filtro per campionato (Serie A)
- Rimozione valori mancanti con `dropna()`
- Aggiunta colonna `cartellini_totali` (gialli + rossi)
- Ordinamento per gol decrescente

## Configurazione

Per eseguire il progetto sostituisci le credenziali nel file:

```python
s3 = boto3.client(
    's3',
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='YOUR_REGION'
)
```

## File

| File | Descrizione |
|------|-------------|
| `aws_serie_a.py` | Script principale ETL |
| `Football teams.csv` | Dataset originale |

## Requisiti

```bash
pip install boto3 pandas
```
