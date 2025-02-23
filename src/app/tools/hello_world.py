import click
from .services import HelloWorldService


# NOTE: click_command()にはhelloのサブコマンドに使いたい名前をつける
@click.command("say", help="/flask/.venv/bin/flask hello say --name <name>")
@click.option("--name", default="World", help="name to say hello")
def run_hello(name: str):
    HelloWorldService().print_hello(name)
