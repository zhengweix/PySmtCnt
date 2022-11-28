'''
Deploy Solidity Contract to Ganache-CLI
'''
from json import *
from web3 import Web3, HTTPProvider
from hexbytes import HexBytes

def set_registration(sender: str, receiver: str, private_key: str, amount: int = 1) -> object:
    '''
    parses array of smart contract data
    :param sender:
    :param receiver:
    :param proivat_key:
    :param amount:
    :return: array {status, data}
    https://www.polarsparc.com/xhtml/GanacheSolidityPython.html
    '''
    w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
    if sender == receiver:
        return {'status': 500, 'error': 'can\' be same account'}
    if not w3.isAddress(sender) or not w3.isChecksumAddress(receiver):
        return {'status': 501, 'error': ''}
    try:
        signed_txn = w3.eth.account.signTransaction(
            {'from': sender, 'to': receiver, 'value': w3.toWei(amount, 'ether'), 'gas': 90000, 'gasPrice': w3.eth.gas_price, 'nonce': w3.eth.getTransactionCount(sender)}, private_key)
        signed_hash = signed_txn['hash']
    except (ValueError, TypeError) as e:
        return {'status': 502, 'error': str(e)}
    try:
        txn = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        if HexBytes(loads(w3.toJSON(w3.eth.getTransaction(txn)))['hash']) == signed_hash:
            return {'status': 200, 'data': w3.fromWei(w3.eth.getBalance(sender), 'ether')}
    except (ValueError, TypeError) as e:
        return {'status': 503, 'error': str(e)}

