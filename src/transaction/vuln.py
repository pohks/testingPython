import requests
import sqlite3

# Função para consultar um site externo (vulnerabilidade SSRF)
def consultar_site(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Falha ao consultar o site"

# Função para realizar uma consulta SQL (vulnerabilidade SQL Injection)
def consultar_usuarios(nome):
    conn = sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE nome = '" + nome + "'"
    cursor.execute(query)
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def main():
    # Vulnerabilidade SSRF - Consulta a uma URL interna
    url_interna = "http://localhost:8080/rota_interna"
    resposta_ssrf = consultar_site(url_interna)
    print("Resposta da consulta SSRF:")
    print(resposta_ssrf)

    # Vulnerabilidade SQL Injection - Consulta de usuários
    nome_usuario = input("Digite o nome do usuário para consultar: ")
    resultados_sqli = consultar_usuarios(nome_usuario)
    print("Resultados da consulta SQL Injection:")
    print(resultados_sqli)

if __name__ == "__main__":
    main()
