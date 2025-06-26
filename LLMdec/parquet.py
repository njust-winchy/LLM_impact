import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

df = pd.DataFrame({'inference_sentence': ['These', 'settings', 'should', 'provide', 'a', 'good', 'balance', 'of', 'structure', 'and', 'flexibility.']})
table = pa.Table.from_pandas(df)

pq.write_table(table, 'output.parquet')
