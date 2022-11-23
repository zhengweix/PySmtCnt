'''
Decentralized Application for developing Smart Contract using Python, Flask, & Solidity
'''
from flask import Flask, jsonify
from hexbytes import HexBytes
from web3.auto import w3
from deploy import asset

app = Flask(__name__)
@app.route('/registered', methods=['POST'])
def registered():
    '''
    Calling a contract function and interact with it using the data from the provided previously.
    '''
    response = w3.eth.getTransaction(
        asset.functions.setRegistration(
            'Decentralized Application for developing Smart Contract by Wei',
            w3.eth.accounts[0]
        ).transact()
    )
    jsonify(response)
@app.route('/api/accounts')
def getAccounts():
    return jsonify(w3.eth.accounts)


if __name__ == '__main__':
    app.run(debug=True)
