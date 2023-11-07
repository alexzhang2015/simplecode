from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

import time

def get_message():
    '''This function blocks until data is ready'''
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

@app.route("/stream")
def stream():
    def generate():
        while True:
            # wait for source data to be available, then push it
            yield 'data: {}\n\n'.format(get_message())
    return app.response_class(generate(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(debug=True)