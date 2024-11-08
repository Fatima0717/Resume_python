#!/usr/bin/env python
"""Djangoの管理タスク用コマンドラインユーティリティ"""
import os
import sys


def main():
    """管理タスクの実行"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'didcoding.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Djangoをインポートできません。インストールされているか、 "
            "PYTHONPATHに設定されているか確認してください。"
            "仮想環境をアクティベートし忘れていませんか？"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
