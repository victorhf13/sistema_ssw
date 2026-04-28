import requests
from datetime import datetime

# =========================
# 1. GERAR TOKEN
# =========================
def gerar_token():
    url = "https://ssw.inf.br/api/generateToken"

    payload = {
        "domain": "TES",
        "username": "user",
        "password": "pass",
        "cnpj_edi": "26087292000135"
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        r = requests.post(url, json=payload, headers=headers)
        data = r.json()

        if data.get("sucess"):
            return data.get("token")

        print("❌ Erro ao gerar token:", data)
        return None

    except Exception as e:
        print("❌ Erro de requisição token:", str(e))
        return None


# =========================
# 2. ENVIAR OCORRÊNCIA
# =========================
def enviar_ocorrencia(token):
    url = "https://ssw.inf.br/api/ocorrenciaParceiro"

    payload = {
        "cnpjRemetente": "51914620000177",
        "nf": {
            "serieNFe": "2",
            "numeroNFe": 32236,
            "chaveNFe": "35191151914620000177550020000322361001919140",
            "pedido": "",
            "codigoNR": "12345678912345"
        },
        "cte": {
            "chaveCTe": "35191151914620000177550020000322361001919140"
        },
        "ocorrencia": {
            "dataHoraEvento": datetime.now().strftime("%Y-%m-%dT%H:%M:%S-03:00"),
            "codigo": 82,
            "descricao": "SAIDA DE UNIDADE",
            "complemento": "Enviado via script Python",
            "dataHoraAgendamento": "",
            "unidade": "SPO",
            "imagem": "",
            "latitude": "",
            "longitude": "",
            "placaAgregado": "",
            "nomeRec": "",
            "documentoRec": "",
            "parentescoRec": ""
        }
    }

    headers = {
        "authorization": token,
        "content-type": "application/json"
    }

    try:
        r = requests.post(url, json=payload, headers=headers)

        print("\n📡 Status HTTP:", r.status_code)

        try:
            resposta = r.json()
            print("📩 Resposta JSON:", resposta)
        except:
            print("📩 Resposta (texto):", r.text)

    except Exception as e:
        print("❌ Erro ao enviar ocorrência:", str(e))


# =========================
# 3. EXECUÇÃO
# =========================
if __name__ == "__main__":
    print("🔐 Gerando token...")

    token = gerar_token()

    if token:
        print("✔ Token gerado com sucesso\n")
        enviar_ocorrencia(token)
    else:
        print("❌ Falha ao gerar token")