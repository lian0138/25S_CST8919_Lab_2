from flask import Flask, request
import logging

app = Flask(__name__)

# Configure logging to output to stdout (Azure captures this)
logging.basicConfig(level=logging.INFO)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == 'password':
        logging.info('Successful login')
        return 'Login successful', 200
    else:
        logging.warning('Failed login attempt')
        return 'Login failed', 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
