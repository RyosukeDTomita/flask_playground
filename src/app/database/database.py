from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def init_db(app):
    """_summary_
    データベースの初期化を行う
    NOTE: database自体の作成はflask dbコマンドではできないので事前にデータベースを用意しておく必要がある。
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = _create_mysql_url(app.config.get("mysql"))

    # 別のデータベースを使えるようにするための検証
    app.config["SQLALCHEMY_BINDS"] = {
        "mydatabase_alt": _create_bind_mysql_url(app.config.get("mysql"))
    }

    db.init_app(app)
    migrate = Migrate(app, db)


def _create_mysql_url(mysql_config):
    """_summary_
    MySQLのエンドポイントを返す
    """
    host = mysql_config.get("host")
    user = mysql_config.get("user")
    password = mysql_config.get("password")
    port = mysql_config.get("port")
    database = mysql_config.get("database")
    # NOTE: mysqlclinetがうまくインストールできなかったのでpymysqlを代わりに使用している。
    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8"


def _create_bind_mysql_url(mysql_config):
    """_summary_
    別のデータベースを使えるようにするための検証
    """
    host = mysql_config.get("host")
    user = mysql_config.get("user")
    password = mysql_config.get("password")
    port = mysql_config.get("port")
    database = "mydatabase_alt"
    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8"
