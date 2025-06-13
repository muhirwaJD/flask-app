from flask import Flask, render_template
import pymysql

app = Flask(__name__)

def db_connect():
    return pymysql.connect(
        host='flaskdb.c7c22480exdf.eu-west-1.rds.amazonaws.com',
        user='admin',
        password='Muhirwa.!',
        database='testdb',
        connect_timeout=5
    )

@app.route('/')
def home():
    return "✅ Hello from Flask + EC2 + RDS!"

@app.route('/people')
def show_people():
    try:
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM visitors")
        rows = cursor.fetchall()
        conn.close()
        return render_template("people.html", people=[r[0] for r in rows])
    except Exception as e:
        return f"❌ Error: {str(e)}"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
