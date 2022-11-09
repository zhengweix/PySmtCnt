'''
Decentralized Application for developing Smart Contract using Python, Flask, & Solidity
'''
from flask import Flask
from hexbytes import HexBytes
from web3.auto import w3
from deploy import asset_register

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DemoSecretKey'
@app.route('/registered', methods=['POST'])
def registered():
    '''
    Calling a contract function and interact with it using the data from the provided previously.
    '''
    response = w3.eth.getTransaction(
        asset_register.functions.setRegistration(
            'Decentralized Application for developing Smart Contract by Wei',
            w3.eth.accounts[0]
        ).transact()
    )
    return 'ethaddress: %s \n txhash: %s \n txdata: %s \n contractaddress: %s' % (w3.eth.accounts[0], HexBytes.hex(response['hash']), HexBytes(response['input']), asset_register.address)

if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=5000)
    w3.isConnected()