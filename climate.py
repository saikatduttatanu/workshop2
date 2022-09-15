import matplotlib.pyplot as plt
import sqlite3
        
years = []
co2 = []
temp = []


connection = sqlite3.connect("climate.db”)
cursor = connection.cursor()
cursor.execute("SELECT * FROM ClimateData") 
print("fetchall:")
result = cursor.fetchall() 


for r in result:
    years.append(r[0])
    co2.append(r[0])
    temp.append(r[0])
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 
plt.show()


