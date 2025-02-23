#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""_summary_
gunicornのrun()から呼ばれる。
"""
from app import app

if __name__ == '__main__':
    # すべてのネットワークインターフェースからのリクエストを8000で待ち受け
    app.run(host='0.0.0.0', port=8000) # app/__init__.py内でimportされているapp/application.pyのappインスタンスを起動する。

