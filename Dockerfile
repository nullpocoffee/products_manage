# Pythonの公式イメージ（軽量版）を使用
FROM python:3.11-slim

# 環境変数の設定
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 作業ディレクトリの設定
WORKDIR /app

# ライブラリのインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# コード全体をコピー
COPY . /app/

# App Runnerが使用するポート8000を開放
EXPOSE 8000

# ★ ここが重要：起動時に migrate を実行してから gunicorn を起動
CMD ["sh", "-c", "python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]
