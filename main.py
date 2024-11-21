from ldap3 import Server, Connection, SIMPLE, SYNC
from getpass import getpass

def valida_ldap(srv: str, usr: str, pwd: str) -> bool:
    try:
        ldap_server = Server(srv, get_info=SYNC)
        with Connection(
            ldap_server,
            user=usr,
            password=pwd,
            authentication=SIMPLE,
            auto_bind=True,
        ) as conn:
            return conn.bound
    except Exception as e:
        # Exibe o erro para diagnóstico em ambientes de produção
        print(f"Erro ao autenticar no LDAP: {e}")
        return False

def main():
    dominio = "informar seu dominio\\"
    ip_server = "Ip do servidor"

    usuario = input("Digite o nome de usuário: ")
    senha = getpass("Digite a senha: ")

    usuario_ad = dominio + usuario

    if valida_ldap(ip_server, usuario_ad, senha):
        print("Autenticação bem-sucedida!")
    else:
        print("Falha na autenticação.")

if __name__ == "__main__":
    main()
