
## Como criar meu ambiente em MySQL


docker network create some-network

$ docker run --name teste-mysql --network some-network -p 3306:3306 -e MYSQL_ROOT_PASSWORD=thiago -d mysql:latest

docker run -it --network some-network --rm mysql mysql -hteste-mysql -u root -p
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'thiago';
FLUSH PRIVILEGES;

CREATE USER 'root'@'%' IDENTIFIED BY 'thiago';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

docker exec -it teste-mysql mysql -u root -p -e "SHOW VARIABLES LIKE 'bind_address';"


docker exec -it teste-mysql sh -c "echo '[mysqld]\nbind-address = 0.0.0.0' > /etc/mysql/my.cnf"


Claro! Aqui está um `README.md` bem explicativo para a pasta `docker/`, detalhando o processo de instalação e configuração do MySQL usando Docker, com base nos comandos que você forneceu:


# 🐳 Instalação do MySQL via Docker

Este guia mostra como subir rapidamente uma instância do MySQL utilizando Docker, permitindo acesso externo e com permissões configuradas para o usuário `root`.

## ✅ Pré-requisitos

Antes de seguir qualquer uma das abordagens, verifique se você possui:

- Acesso como administrador na máquina
- [Docker instalado](https://www.docker.com/get-started) (para a instalação via Docker)
- Acesso à internet para download dos pacotes

## 📦 Passo a Passo da Instalação

### 1. Crie uma rede Docker personalizada

Isso facilita a comunicação entre contêineres no mesmo ambiente isolado.

```bash
docker network create some-network
```

### 2. Suba o container do MySQL

Neste exemplo, o nome do container será `teste-mysql`, a senha do root será `thiago`, e a porta local 3306 será exposta.

```bash
docker run --name teste-mysql \
  --network some-network \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=<CRIE-UMA-SENHA-PARA-ROOT> \
  -d mysql:latest
```

### 3. Acesse o MySQL pela linha de comando

Você pode usar outro container temporário para se conectar ao MySQL:

```bash
docker run -it --network some-network --rm mysql mysql -h teste-mysql -u root -p
```

Digite a senha: `<CRIE-UMA-SENHA-PARA-ROOT>`


### 4. Configure o usuário `root` para permitir conexões externas

Execute os comandos SQL abaixo no prompt do MySQL:

```sql
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '<CRIE-UMA-SENHA-PARA-ROOT>';
FLUSH PRIVILEGES;

-- Caso o comando acima não funcione, crie o usuário manualmente:
CREATE USER 'root'@'%' IDENTIFIED BY '<CRIE-UMA-SENHA-PARA-ROOT>';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

### 5. Verifique o endereço de bind do MySQL

Esse passo é para confirmar se o MySQL está escutando em todas as interfaces:

```bash
docker exec -it teste-mysql mysql -u root -p -e "SHOW VARIABLES LIKE 'bind_address';"
```

### 6. Altere o bind address para permitir acesso externo

Esse comando sobrescreve o arquivo de configuração principal do MySQL dentro do container, permitindo conexões externas:

```bash
docker exec -it teste-mysql sh -c "echo '[mysqld]\nbind-address = 0.0.0.0' > /etc/mysql/my.cnf"
```

## 🧹 Remover o ambiente

```bash
docker stop teste-mysql
docker rm teste-mysql
docker network rm some-network
```

