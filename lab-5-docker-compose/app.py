from flask import Flask
import redis
import psycopg2  

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    r.incr('hits')
    count = r.get('hits')
    return f'Docker Compose app! Visits: {count}'

@app.route('/db')
def db_test():
    conn = psycopg2.connect(
        host='postgres',
        database='mydb',
        user='user',
        password='password'
    )
    cur = conn.cursor()
    cur.execute('SELECT version()')
    version = cur.fetchone()[0]
    cur.close()
    conn.close()
    return f'PostgreSQL: {version}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
