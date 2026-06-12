from datetime import datetime
import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    app_name = os.environ.get("APP_NAME", "Dev Platform Demo")
    git_url = os.environ.get("GIT_SERVER_URL", "nicht konfiguriert")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
      <head><title>{app_name}</title></head>
      <body>
        <h1>{app_name}</h1>
        <p>Diese Anwendung laeuft in einem eigenen Runtime-Container.</p>
        <p>Gitea-Server: {git_url}</p>
        <p>Zeitpunkt: {now}</p>
      </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
