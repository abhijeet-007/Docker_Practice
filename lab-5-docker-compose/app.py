from flask import Flask
import redis
import psycopg2
import os

app = Flask(__name__)

r = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=6379, decode_responses=True)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>Docker Compose App</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: Arial, sans-serif; background: #1a1a2e; color: #eee; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
    .card {{ background: #16213e; border-radius: 16px; padding: 40px 60px; text-align: center; box-shadow: 0 8px 32px rgba(0,0,0,0.4); }}
    h1 {{ font-size: 2rem; color: #e94560; margin-bottom: 10px; }}
    p {{ color: #a8a8b3; margin-bottom: 30px; }}
    .counter {{ font-size: 5rem; font-weight: bold; color: #fff; background: #e94560; border-radius: 12px; padding: 20px 40px; display: inline-block; margin-bottom: 30px; }}
    .badge {{ background: #0f3460; color: #e94560; padding: 6px 16px; border-radius: 20px; font-size: 0.85rem; margin-bottom: 20px; display: inline-block; }}
    a {{ color: #e94560; text-decoration: none; font-size: 0.9rem; }}
    a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <div class="card">
    <span class="badge">🐳 Docker Compose</span>
    <h1>Live Visitor Counter</h1>
    <p>Powered by Flask + Redis</p>
    <div class="counter">{count}</div>
    <br>
  </div>
</body>
</html>
"""

@app.route('/')
def hello():
    r.incr('hits')
    count = r.get('hits')
    return HTML.format(count=count)

@app.route('/db')
def db_test():
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST', 'postgres'),
        database=os.getenv('POSTGRES_DB', 'mydb'),
        user=os.getenv('POSTGRES_USER', 'user'),
        password=os.getenv('POSTGRES_PASSWORD', 'password')
    )
    try:
        cur = conn.cursor()
        cur.execute('SELECT version()')
        version = cur.fetchone()[0]
        cur.close()
    finally:
        conn.close()
    return DB_HTML.format(version=version)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.getenv('FLASK_DEBUG', 'false').lower() == 'true')
