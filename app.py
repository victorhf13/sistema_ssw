from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# =========================
# BANCO DE DADOS
# =========================
def conectar():
    return sqlite3.connect("ssw.db")

def criar_tabelas():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tokens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        domain TEXT,
        username TEXT,
        cnpj TEXT,
        token TEXT,
        resposta TEXT,
        data TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS ocorrencias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        token TEXT,
        cte TEXT,
        nfe TEXT,
        codigo TEXT,
        descricao TEXT,
        resposta TEXT,
        data TEXT
    )
    """)

    conn.commit()
    conn.close()

criar_tabelas()

# =========================
# TOKEN
# =========================
@app.route("/token", methods=["POST"])
def token():

    data = request.json

    fake_token = "TOKEN_" + str(data.get("cnpj_edi", ""))

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO tokens (domain, username, cnpj, token, resposta, data)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data.get("domain"),
        data.get("username"),
        data.get("cnpj_edi"),
        fake_token,
        str(data),
        datetime.now(timezone.utc).isoformat()
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "ok": True,
        "token": fake_token
    })

# =========================
# OCORRÊNCIA
# =========================
@app.route("/ocorrencia", methods=["POST", "OPTIONS"])
def ocorrencia():

    if request.method == "OPTIONS":
        return jsonify({"ok": True}), 200

    data = request.json

    token = data.get("token", "")
    payload = data.get("payload", {})

    cte = payload.get("cte", {}).get("chaveCTe", "")
    nfe = payload.get("nf", {}).get("numeroNFe", "")
    codigo = payload.get("ocorrencia", {}).get("codigo", "")
    descricao = payload.get("ocorrencia", {}).get("descricao", "")

    data_hora = datetime.now(timezone.utc).isoformat()

    conn = conectar()
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
        str(data),
        data_hora
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "ok": True,
        "msg": "Recebido e salvo no banco",
        "dataHora": data_hora,
        "dados": data
    })

# =========================
# 🔥 HISTÓRICO CORRIGIDO (AQUI ESTÁ O FIX)
# =========================
@app.route("/historico", methods=["GET"])
def historico():

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, token, cte, nfe, codigo, descricao, resposta, data
        FROM ocorrencias
        ORDER BY id DESC
    """)

    rows = cur.fetchall()
    conn.close()

    dados = []

    for r in rows:
        dados.append({
            "id": r[0],
            "token": r[1],
            "cte": r[2],
            "nfe": r[3],
            "codigo": r[4],
            "descricao": r[5],
            "resposta": r[6],
            "data": r[7]
        })

    return jsonify(dados)

# =========================
# START
# =========================
if __name__ == "__main__":
    app.run(port=5000, debug=True)