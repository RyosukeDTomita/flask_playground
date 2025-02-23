# coding:utf-8
from flask import Flask
from flask_iniconfig import INIConfig
import os
from .database import db
from .database import init_db



def _create_app():
    """_summary_

    Returns:
        _type_: _description_
    以下エラーをapp.app_context().push()で回避する
    RuntimeError(unbound_message) from None
    flask-container  | RuntimeError: Working outside of application context.
    """
    app = Flask(__name__)

    # config.iniを読み込む
    INIConfig(app)
    current_dir = os.path.dirname(__file__)
    config_ini_path = os.path.join(current_dir, "../config.ini")
    if not os.path.exists(config_ini_path):
        raise FileNotFoundError("Not Found config.ini.")
    app.config.from_inifile(config_ini_path, encoding="utf-8")
    # config.iniの内容をapp.configに追加
    app.config = {**app.config}

    # データベースの初期化
    init_db(app)

    # RuntimeErrorを回避
    app.app_context().push()
    return app


app = _create_app()  # run.pyにてimportされる。
