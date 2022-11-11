'''
Deploy Solidity Contract to Ganache-CLI
'''
from solcx import compile_standard
from web3 import Web3, HTTPProvider
from json import loads
w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
BUYER = w3.eth.accounts[3]
DEALER = w3.eth.accounts[0]
w3.eth.defaultAccount = DEALER
BUYER_KEY = '0xf17d112f0d8d408be0c6afdb0592530bef72fe08953a8cc072e7de1b05b4c479'
response = compile_standard(
    {
        "language": "Solidity",
        "sources": {
            "alpha": {
                "urls": [
                    "Vehicle.sol"
                ]
            }
        },
        "settings": {
            "optimizer": {
               "enabled": True
            },
            "outputSelection": {
                "*": {
                    "*": [
                        "metadata", "evm.bytecode", "abi"
                    ]
                }
            }
        }
    },
    allow_paths=['.']
)
contract = w3.eth.contract(
    abi=response['contracts']['alpha']['Vehicle']['abi'],
    bytecode=response['contracts']['alpha']['Vehicle']['evm']['bytecode']['object']
)
amount = w3.toWei(5, 'ether')
txn_receipt = w3.eth.waitForTransactionReceipt(contract.constructor('Blue', 'V1', amount).transact())
print(loads(w3.toJSON(txn_receipt)))
asset = w3.eth.contract(
    address=txn_receipt.contractAddress,
    abi=response['contracts']['alpha']['Vehicle']['abi']
)
print(asset.functions.getVin().call())
print(asset.functions.getOwner().call())

buyer_txn_receipt = w3.eth.waitForTransactionReceipt(asset.functions.buyVehicle(amount).transact({'from': BUYER, 'value': amount, 'gas': 1000000}))
print(buyer_txn_receipt)

print(asset.functions.getOwner().call())
print(w3.fromWei(w3.eth.getBalance(DEALER), 'ether'))
print(w3.fromWei(w3.eth.getBalance(BUYER), 'ether'))
