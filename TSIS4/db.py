import psycopg2
import config


def get_conn():
    return psycopg2.connect(
        dbname=config.DB_NAME,
        user=config.DB_USER,
        host=config.DB_HOST
    )


import psycopg2
from psycopg2 import sql
import config


def ensure_database():
    conn = psycopg2.connect(
        dbname="postgres",
        user=config.DB_USER,
        host=config.DB_HOST
    )
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (config.DB_NAME,))
    exists = cur.fetchone()

    if not exists:
        cur.execute(sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(config.DB_NAME)
        ))
        print(f"Database {config.DB_NAME} created")

    cur.close()
    conn.close()

def create_tables():
    conn = get_conn()
    cur  = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS game_sessions (
            id SERIAL PRIMARY KEY,
            player_id INTEGER REFERENCES players(id),
            score INTEGER NOT NULL,
            level_reached INTEGER NOT NULL,
            played_at TIMESTAMP DEFAULT NOW()
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


def get_or_create_player(username):
    conn = get_conn()
    cur  = conn.cursor()
    cur.execute("SELECT id FROM players WHERE username = %s;", (username,))
    row = cur.fetchone()
    if row:
        player_id = row[0]
    else:
        cur.execute("INSERT INTO players (username) VALUES (%s) RETURNING id;", (username,))
        player_id = cur.fetchone()[0]
        conn.commit()
    cur.close()
    conn.close()
    return player_id


def save_session(player_id, score, level_reached):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s);",
        (player_id, score, level_reached)
    )
    conn.commit()
    cur.close()
    conn.close()


def get_leaderboard():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.username, gs.score, gs.level_reached, gs.played_at
        FROM game_sessions gs
        JOIN players p ON p.id = gs.player_id
        ORDER BY gs.score DESC
        LIMIT 10;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def get_personal_best(username):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT MAX(gs.score)
        FROM game_sessions gs
        JOIN players p ON p.id = gs.player_id
        WHERE p.username = %s;
    """, (username,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row and row[0] is not None:
        return row[0]
    return 0
