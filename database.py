import sqlite3
from datetime import datetime, timezone

# =========================
# CONEXÃO
# =========================
def conectar():
    return sqlite3.connect("ssw.db")

# =========================
# CRIA TABELAS (CORRIGIDO)
# =========================
def criar_tabelas():
    conn = conectar()
    cur = conn.cursor()

    # =========================
    # TOKENS
    # =========================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS tokens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        domain TEXT,
        username TEXT,
        cnpj TEXT,
        token TEXT,
        resposta TEXT,
        data TEXT NOT NULL
    )
    """)

    # =========================
    # OCORRÊNCIAS (CORRIGIDO)
    # =========================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS ocorrencias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        token TEXT,
        cte TEXT,
        nfe TEXT,
        codigo TEXT,
        descricao TEXT,
        resposta TEXT,
        status TEXT DEFAULT 'OK',
        data TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

# =========================
# UTIL: GERAR DATA PADRÃO (ISO SEM FALHA)
# =========================
def agora():
    return datetime.now(timezone.utc).isoformat()

# =========================
# EXEMPLO DE USO NO FLASK
# =========================
def salvar_ocorrencia(conn, token, cte, nfe, codigo, descricao, payload):
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO ocorrencias (token, cte, nfe, codigo, descricao, resposta, data)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        token,
        cte,
        nfe,
        codigo,
        descricao,
        str(payload),
        agora()
    ))

    conn.commit()