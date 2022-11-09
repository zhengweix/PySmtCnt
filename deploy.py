'''
Deploy Solidity Contract to Ganache-CLI
'''
from solc import compile_source
from web3 import Web3, HTTPProvider
WEB3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
WEB3.eth.defaultAccount = WEB3.eth.accounts[0]
smt_cnt_interface = compile_source(
    '''
    pragma solidity ^0.8.17;
    contract StorageContract {
        string public serialnumber;
        address public assetowner;

        event Registration(
           string serialnumber,
           address assetowner
        );
        
        function setRegistration (string newSerialnumber, address newAssetowner) public {
            serialnumber = newSerialnumber;
            assetowner = newAssetowner;
            emit Registration(serialnumber, assetowner);
        }
    }
    '''
)['<stdin>:StorageContract']
contract = WEB3.eth.contract(
    abi=smt_cnt_interface['abi'],
    bytecode=smt_cnt_interface['bin']
)
tx_receipt = Web3.eth.waitForTransactionReceipt(contract.constructor().transact())
asset_register = Web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=smt_cnt_interface['abi']
)