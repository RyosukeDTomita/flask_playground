from flask import current_app
from flask.cli import AppGroup

from .hello_world import run_hello


# helloコマンドを定義して追加
hello_tool = AppGroup("hello")
hello_tool.add_command(run_hello) # hello_world_serviceのrun_helloメソッドをflaskから使用可能にする。
current_app.cli.add_command(hello_tool)

