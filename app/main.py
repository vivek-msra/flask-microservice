from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def live_output():
    current_time = time.strftime("%H:%M:%S")
    return f"""
    <html>
      <head>
        <meta http-equiv="refresh" content="1">
      </head>
      <body>
        <h1>Hello Bibek 👋</h1>
        <p>Current Time: {current_time}</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
