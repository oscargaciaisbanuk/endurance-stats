import pandas as pd
import numpy as np
import re
import sys

result=pd.DataFrame()

for f in sys.argv[3:]:
    df = pd.read_csv(f, sep=';')
    m=re.search("([a-zA-Z_0-9]+)",f)
    df['TRACK']=m.group(1)
    if result.empty:
        result=df
    else:
        result=result.append(df, ignore_index=True)

sec=result[' LAP_TIME'].str.extract("(?:([0-9]+).)?([0-9]+):([0-9]+).([0-9]+)",expand=False)
sec.fillna(0,inplace=True)
sec['SEG']=pd.to_numeric(sec[1])*60 + pd.to_numeric(sec[2]) + pd.to_numeric(sec[3])/1000 + pd.to_numeric(sec[0]) * 3600
result['SEG']=sec['SEG']

a=result[['TRACK','CLASS','MANUFACTURER','TEAM','NUMBER','DRIVER_NAME','SEG']].groupby(['TRACK','CLASS','MANUFACTURER','TEAM','NUMBER','DRIVER_NAME']).agg({np.size,np.mean, np.median, np.min,lambda x: np.percentile(x, q = 15)})

a.to_csv(sys.argv[1]+'-'+sys.argv[2]+'-DRIVER.CSV',tupleize_cols=True,float_format='%.2f',decimal=',')

a=result[['TRACK','CLASS','MANUFACTURER','TEAM','NUMBER','SEG']].groupby(['TRACK','CLASS','MANUFACTURER','TEAM','NUMBER']).agg({np.size,np.mean, np.median, np.min,lambda x: np.percentile(x, q = 15)})

a.to_csv(sys.argv[1]+'-'+sys.argv[2]+'-TEAM.CSV',tupleize_cols=True,float_format='%.2f',decimal=',')
