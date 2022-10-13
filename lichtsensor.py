from gpiozero import LightSensor
from time import sleep
import pymssql

varSensor = LightSensor(18)

while True:
    
    
    conn = pymssql.connect(host='jasonvanhamondserver.database.windows.net', port=1433, database='Thema10', user='jasonvanhamond', password='P@ssword')

    cursor = conn.cursor()
    
    while True:
        # doe iets met deze rowss
        lightValue = varSensor.value * 100
        print(lightValue)        
        cursor.execute("INSERT INTO Oefening21(sensorValue, sensorDevice, createDateTime) VALUES(%s, 'lichtsensor', GETDATE())" %(lightValue)) # meer value (%s, %s) %(value1, value2)
        conn.commit()
        sleep(10)
        
        
        
    conn.close()
    
    
