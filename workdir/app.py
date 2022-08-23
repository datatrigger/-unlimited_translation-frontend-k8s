from flask import Flask, render_template, request
import mysql.connector
import requests
import pandas as pd
import os

# # Fetch credentials for the MySQL database
# def get_secret(key):
#     '''Retrieve Docker secrets'''
#     path= os.environ[key]
#     with open(path) as file:
#             value = file.read()
#     return value

# db_user = get_secret('FLASK_DB_USER_FILE')
# db_password = get_secret('FLASK_DB_PASSWORD_FILE')

# Init Flask app
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        text_de = request.form['text']
        headers = {'accept': 'application/json'}
        json_data = {'text_de': text_de}
        text_en = requests.post('http://backend-fastapi-pod/translate', headers=headers, json=json_data).json()['text_en']

        # if text_de:
        #     try:
        #         cnx = mysql.connector.connect(user=db_user, password=db_password, host='database', database='translation')
        #         cursor = cnx.cursor()
        #         text_de_sql = text_de.replace("\'", "\\\'")
        #         text_en_sql = text_en.replace("\'", "\\\'")
        #         cursor.execute(f"""INSERT INTO translations (text_de, text_en) VALUES ('{text_de_sql}', '{text_en_sql}');""")
        #         cnx.commit()
        #     except mysql.connector.Error as error:
        #         text_de = f'The input and its translation could not be written into the database! The following MySQL error was raised: {str(error)}\n\n{text_de}'
        #     finally:
        #         cursor.close()
        #         cnx.close()

        return render_template('index.html', input = text_de, translation = text_en)
    else:
        return render_template('index.html', input = None, translation = None)

@app.route('/query_db', methods=['POST', 'GET'])
def query_db():

    return render_template('query_db.html', result = None)


    # if request.method == 'POST':
    #     query = request.form['query']

    #     try:
    #         cnx = mysql.connector.connect(user=db_user, password=db_password, host='database', database='translation')
    #         cursor = cnx.cursor()
    #         cursor.execute(query)
    #         result = pd.DataFrame(data = cursor.fetchall(), columns = cursor.column_names).to_html(index=False)
    #     except mysql.connector.Error as error:
    #         result = f'Something went wrong! The following MySQL error was raised: {str(error)}'
    #     finally:
    #         cursor.close()
    #         cnx.close()

    #     return render_template('query_db.html', result = result )
    # else:
    #     return render_template('query_db.html', result = None)

# Run Flask app. Host and port are specified in the Dockerfile
if __name__ == "__main__":
    app.run()