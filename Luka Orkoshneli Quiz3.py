import requests
import json
import sqlite3
from plyer import notification

#davukavshirdi bazas
conn = sqlite3.connect('mydatabase.db')

#shevqmeni kursor obieqti
cursor = conn.cursor()

# shevqmeni table romelsac aqvs id , title da body
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mytable (
        id INTEGER PRIMARY KEY,
        title TEXT,
        body TEXT
    )
''')

# davacommite
conn.commit()

url = 'https://jsonplaceholder.typicode.com/posts/'

#wamoviget api
response = requests.get(url)

#tu dagvibrunda sworad
if response.status_code == 200:
    #jsonshi gavparset
    json_data = response.json()

    #shevqmeni faili json is da chavwere es data
    with open("api_data.json", 'w') as file:
        json.dump(json_data, file, indent=4)

    #aq ubralod vprintav infomacias da aseve vamateb bazashi id s sataurs da agweras
    for i in json_data:
        print(i['title'])
        print(i['body'])
        print(i['userId'])
        print(i['id'])
        print()

        id = i['id']
        title = i['title']
        body = i['body']
        cursor.execute('INSERT INTO mytable (id, title, body) VALUES (?, ?, ?)', (id, title, body))

else:
    print("Error: API request failed.")

#davacommite
conn.commit()

notification.notify(
    title="Data Inserted",
    message="JSON data inserted into the database successfully.",
    timeout=10
)

#ubralod viyeneb requestis methodebs
print(response.status_code, response.headers)

#vwyvet bazastan kavshirs
conn.close()

