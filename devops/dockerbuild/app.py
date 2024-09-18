from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/') # Home page
def serve_html():
    return '''
    <!DECOTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Static image</title>
    </head>
    <body>
    <h1>Welcome to our Website!<\h1>
    <img src="/static/Shrekpic.jpg" alt="Picture">
    </body>
    </html>
    '''

@app.route('/static/<path:path>') # Static files
def serve_statich(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

