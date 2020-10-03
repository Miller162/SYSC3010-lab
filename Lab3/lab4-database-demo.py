import sqlite3

id = 4;
temperature = 0.0;
date = '2014-01-05';

dbconnect = sqlite3.connect("my.db");

dbconnect.row_factory = sqlite3.Row;

cursor = dbconnect.cursor();

for i in range(10):
    id+= 1;
    temperature += 1.1
    cursor.execute('''insert into temperature values (?, ?, ?)''', (id, temperature, date));
    
#cursor.execute('''insert into temperature values (4, 2.1, '2020-04-24')''');

dbconnect.commit();

cursor.execute('SELECT * FROM temperature');

for row in cursor:
    print(row['id'], row['tempfloat'], row['datetext']);


#exercise 4
cursor.execute('''CREATE TABLE IF NOT EXISTS sensors (sensorID INTEGER, type TEXT, zone TEXT)''');
cursor.execute('''INSERT INTO sensors values (1, "door", "kitchen")''');
cursor.execute('''INSERT INTO sensors values (2, "temperature", "kitchen")''');
cursor.execute('''INSERT INTO sensors values (3, "door", "garage")''');
cursor.execute('''INSERT INTO sensors values (4, "motion", "garage")''');
cursor.execute('''INSERT INTO sensors values (5, "temperature", "garage")''');

dbconnect.commit();
    
cursor.execute('SELECT * FROM sensors WHERE zone="kitchen"');
for row in cursor:
    print(row['sensorID'], row['type'], row['zone']);
    
print("\n")

cursor.execute('SELECT * FROM sensors WHERE type="door"');
for row in cursor:
    print(row['sensorID'], row['type'], row['zone']);

dbconnect.close();