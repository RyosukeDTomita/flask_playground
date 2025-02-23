# Flask playground

![un license](https://img.shields.io/github/license/RyosukeDTomita/flask_playground)

## INDEX

- [ABOUT](#about)
- [ENVIRONMENT](#environment)
- [PREPARING](#preparing)
- [HOW TO USE](#how-to-use)

---

## ABOUT

Try to use Flask's features.
Flaskの機能を試すためのリポジトリ

- [Flask REST API](#flask-rest-api)
- [Flask CLI](#flask-cli)
- [Flask Migrate](#flask-migrate)

---

## ENVIRONMENT

- Python: 3.12.4
  - Flask
  - rye

see [Dockerfile](./Dockerfile) and [pyproject.toml](./pyproject.toml) in detail.

---

## PREPARING

### Using Dev Container

open VSCode and use `Dev Containers: Rebuild Container without cache`

### Not Using Dev Container

```bash
cd flask_playground
docker compose up
```

---

## HOW TO USE

### Flask REST API

In [Dockerfile](./Dockerfile), `gunicorn` activates flask app.

```bash
/flask/.venv/bin/gunicorn app:run --chdir /flask/src
```

Go to [http://localhost:8000](http://localhost:8000) and you can see the Hello World message.

### Flask CLI

```shell
cd /flask/src
/flask/.venv/bin/flask hello say --name sigma
```

### Flask Migrate

#### `mydatabase` only

> [!WARNING]
> This repository uses multiple databases.

before `flask db upgrade`, you can see only `alembic_version` table.

```shell
cd /flask/src
/flask/.venv/bin/flask db init
/flask/.venv/bin/flask db migrate
```

```sql
mysql -h mysql_svr -u root -p
mysql> USE mydatabase;
Database changed
mysql> SHOW TABLES;
+----------------------+
| Tables_in_mydatabase |
+----------------------+
| alembic_version      |
+----------------------+
1 row in set (0.00 sec)
```

```shell
/flask/.venv/bin/flask db upgrade
```

```sql
mysql> SHOW TABLES;
+----------------------+
| Tables_in_mydatabase |
+----------------------+
| alembic_version      |
| users                |
+----------------------+
2 rows in set (0.00 sec)
```

#### multiple databases

[Multiple Database with bind](https://flask-sqlalchemy.readthedocs.io/en/stable/binds/)

```sql
mysql -h mysql_svr -u root -p
USE mydatabase;
DROP TABLE alembic_version;
drop table users;
CREATE DATABASE mydatabase_alt; -- flask db cannot create database
```

```shell
rm -rf migrations # if any
/flask/.venv/bin/flask db init --multidb
```

---

## memo

### rye

- `rye install`ではpyproject.tomlのdependenciesにライブラリが追加されない。これがしたいなら，`rye add`を使う。
- `rye run python run.py`のようにすると，venv内のpythonを使って.pyを実行できる。
- `rys sync`するとpyproject.tomlのdependenciesに記述されたライブラリがvenvにインストールされる。
