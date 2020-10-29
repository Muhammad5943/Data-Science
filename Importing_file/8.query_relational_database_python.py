from pandas.io.sql import DatabaseError
from sqlalchemy import create_engine
import pandas as pd

# cara biasa (cara 1)
""" 
1. import package dan function
2. membuat database engine
3. koneksikan ke engine
4. mengisi query DatabaseError
5. menyimpan hasil query ke dataframe
6. menutup koneksi 
"""

""" engine = create_engine('sqlite:///Northwind_Small.sqlite')
con = engine.connect()
rs = con.execute("SELECT * FROM Customer")
dataFrame = pd.DataFrame(rs.fetchall())
dataFrame.columns = rs.keys()
con.close() """

# print(dataFrame)

# konteks manager (cara 2)
""" 
1. import package dan function
2. membuat database engine
3. koneksikan ke engine
4. mengisi query DatabaseError
5. menyimpan hasil query ke dataframe
"""

""" engine = create_engine('sqlite:///Northwind_Small.sqlite')
with engine.connect() as con:
    rs = con.execute("SELECT CompanyName, Phone FROM Customer")
    df = pd.DataFrame(rs.fetchmany(size = 3))
    df.columns =rs.keys()

print(df) """

# cara lama (menggunakan context manager)
""" engine = create_engine('sqlite:///Northwind_Small.sqlite')
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Customer")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

print(df) """

# cara cepat
engine = create_engine("sqlite:///Northwind_Small.sqlite")
df = pd.read_sql_query("SELECT * FROM Customer", engine)
print(df)