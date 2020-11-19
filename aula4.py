from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://quant-ibmec.group/site.html'
resp = urlopen(url)
pag = resp.read()
print(pag)
html = BeautifulSoup(pag,'html.parser')
html

html.h1.get_text()
html.find('div',class_='banana').get_text()
----
import pandas as pd

tabela = html.find('table')
df=pd.read_html(str(tabela))[0]
df.columns = df.iloc[0,:]
df.drop([0],inplace=True)
==============


!pip install pymysql

-------
from sqlalchemy import create_engine
import pymysql
import pandas as pd

conn_str = 'mysql+pymysql://quanti43_user:Ibmec@2017@162.241.203.36/quanti43_camara'
conn = create_engine(conn_str)

df=pd.read_sql('select * from camara', con=conn)
df.drop('level_0',axis=1,inplace=True)
df.head()
----
linha ={
#'level_0':['100'],
'txNomeParlamentar':['Maria'],
'ideCadastro':[''],
'nuCarteiraParlamentar':[''],
'nuLegislatura':[''],
'sgUF':['RJ'],
'sgPartido':['PPZ'],
'codLegis