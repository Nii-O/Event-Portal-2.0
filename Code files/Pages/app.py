import pyodbc
from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

# Replace the following with your actual database connection parameters
app.config['SQL_SERVER'] = 'tcp:ist615npandian.database.windows.net,1433;'
app.config['SQL_DATABASE'] = 'Event_management'
app.config['SQL_USERNAME'] = 'npandian'
app.config['SQL_PASSWORD'] = 'Nagul12*'

# Create a function to establish a database connection
def get_db_connection():
    conn = pyodbc.connect(
        'Driver={ODBC Driver 18 for SQL Server};'
        f'SERVER={app.config["SQL_SERVER"]};'
        f'DATABASE={app.config["SQL_DATABASE"]};'
        f'UID={app.config["SQL_USERNAME"]};'
        f'PWD={app.config["SQL_PASSWORD"]};'
       )
    return conn

@app.route('/get_data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM v_events')
    data = cursor.fetchall()

    conn.close()

    # Convert data to a JSON response
    response = jsonify(data)
    return response

@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM v_events')
    data = cursor.fetchall()

    conn.close()

    #print("Response Data: ", data)

    # Pass the data to the template
    return render_template('index.html', data=data)

#app.static_folder = 'static'

# @app.route('/linked_page')
# def linked_page():
#     return render_template('Available_events/index2.html')

if __name__ == '__main__':
    app.run(debug=True)


