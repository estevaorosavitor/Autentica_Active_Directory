## Autenticar usuário no Active Directory

Código implementado para facilitar a autenticação de usuários através do Active Directory (Famoso AD), de forma simples e rápida.

São apenas duas variáveis que devem ser informadas no código-fonte:
- `dominio` : que é o nome do domínio do seu AD;
- `ip_server` : que é o IP do servidor local de seu Ad.

Será necessário instalar a biblioteca ldap3:
`pip install ldap3`