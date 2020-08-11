from constants import *
import os
import subprocess
import json
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account

mnemonic = os.getenv('ETH_MNEMONIC')

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

def derive_wallets(coin, numderive=3, mnem=mnemonic):
    derive_results = subprocess.run(
        ['./derive',
         '-g',
         f'--coin={coin}',
         f'--mnemonic={mnem}',
         f'--numderive={numderive}',
         '--format=json'],
        capture_output=True
    )
    derived_json = json.loads(derive_results.stdout)
    return derived_json

def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

def create_tx(coin, account, to, amount, chainId):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": to, "value": amount})
        tx = {
            'to': to,
            'from': account.address,
            'value': amount,
            'gasPrice': w3.eth.gasPrice,
            'gas': gasEstimate,
            'nonce': w3.eth.getTransactionCount(account.address),
            'chainId': chainId
        }
    elif coin == BTCTEST:
        tx = PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])
    return tx

def send_tx(coin, account, to, amount, chainId):
    tx = create_tx(coin, account, to, amount, chainId)
    signed_tx = account.sign_transaction(tx)
    if coin == ETH:
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return result
    elif coin == BTCTEST:
        result = NetworkAPI.broadcast_tx_testnet(signed_tx)
    return result