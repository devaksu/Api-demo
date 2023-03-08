from flask import Flask
from funcs import get_customer_info

app = Flask(__name__)

@app.route('/customer/<customer_id>')
def customer(customer_id):
    return get_customer_info(customer_id)


if __name__ == '__main__':
    app.run(debug=True)