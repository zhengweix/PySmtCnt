'''
Decentralized Application for developing Smart Contract using Python, Flask, & Solidity
'''
from flask import Flask, jsonify, request
from web3.auto import w3
from deploy import *
from json import *

app = Flask(__name__)
@app.route('/api/register', methods=["POST"])
def register():
    ''' Calling a contract function and interact with it using the data from the provided previously. '''
    data = loads(request.data)
    response = set_registration(data['sender'], data['receiver'], data['private_key'], data['amount'])
    if response['status'] == 200:
        return jsonify({'status': 'success', 'message': response['data']})
    else:
        if response['status'] == 502:
            return jsonify({'status': 'error', 'message': 'wrong private key'})
        else:
            return jsonify({'status': 'error', 'message': response['error']})


@app.route('/api/accounts')
def get_accounts():
    return jsonify(w3.eth.accounts)

if __name__ == '__main__':
    app.run(debug=True)
