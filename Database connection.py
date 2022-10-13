import pymssql

conn = pymssql.connect(host='{databaseServer}.database.windows.net', port=1433,
database='Thema10', user='{user}@{databaseServer}', password='{password}')
cursor = conn.cursor()
cursor.execute('{QUERY};')
row = cursor.fetchone()

while row:
 #Doe iets met deze rows
 print(str(row[0]) + str(row[1]) )
 row = cursor.fetchone()

conn.commit()
conn.close() 