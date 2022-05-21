#!/usr/bin/env python3

import json,sys
from eth_account import account
from web3 import Web3
from web3.types import SignedTx
#import getEthBalance.py

#ganache_url = "http://127.0.0.1:7545"
ganache_url = "http://192.168.2.30:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# account_1 = "0xf9570e6cb35A2FBDDc267316D342b258aC17f1B6"
# account_1_key = "b6d9eb7637075bafddb291558a98f3cd1528dff13cb75ea487c4c7f8c53c9838"
# account_2 = "0xe370aeDB4CDA422dF8328210C3C52220946232D3"
# account_2_key = "885f8bc0e2e2b6c211d8d9732204966cf795270d9fdf7c2e3169036477f9807e"

account_1 = "0x1BaA1D300Ee73f9D232BE778140bB9c0da997E66"
account_1_key = "43de7ba914dd499383581dfb740611b33d489fcd26ee2c1882fd6074962a6d13"
account_2 = "0x2ea58F3402170884B2DA47c2c8246D9D84e64985"
account_2_key = "f87bf133b68e8a250e103cdff938e7e2d2bbe9b24d5ba4cc5d18093557eee5f0"
account_3 = "0x7Fb1108D7241e1d2835fdf798704F71252Fd4E75"
account_3_key = "3328fd3853c61e5386ff06137868cb2541d28691cfb77a36217451d7c0e1bc56"
account_4 = "0x3603Cbe68cfe3fc5facA6f3721AD7F44b4Df6F4b"
account_4_key = "fc1c1dfe9577cc3b9585b04928177901d1e36c660f3f4ad90d129daf6f232165"
account_5 = "0xEB4355E5D4220e4aEa30a4E87Bd8b4896f390141"
account_5_key = "3d181e5f9c73c2688a890c4c5b4ad453a3ac47a3b577a0d32ace8df32588f9f8"


def connectToBlockchain():

    #print(web3.isConnected())
    connected = web3.isConnected()
    if connected == True:
        print('Connected!')
        print('Current block number: ', web3.eth.blockNumber)
        #print(web3.eth.blockNumber)
    elif connected != True:
        print('Not connected..')
        sys.exit()

def getVariables():
    global send_acct, receive_acct, signing_key, value
    print("Enter the wallet address to which you want to send ether")
    receive_acct = input()
    print('1 2 3 4 5')
    choice = input()
    if choice == '1':
         send_acct = account_1
         # print("Enter the wallet address to which you want to send ether")
         # receive_acct = input()
         signing_key = account_1_key
    elif choice == '2':
         send_acct = account_2
         # print("Enter the wallet address to which you want to send ether")
         # receive_acct = input()
         signing_key = account_2_key
    elif choice == '3':
         send_acct = account_3
         # print("Enter the wallet address to which you want to send ether")
         # receive_acct = input()
         signing_key = account_3_key
    elif choice == '4':
         send_acct = account_4
         # print("Enter the wallet address to which you want to send ether")
         # receive_acct = input()
         signing_key = account_4_key
    elif choice == '5':
         send_acct = account_5
         # print("Enter the wallet address to which you want to send ether")
         # receive_acct = input()
         signing_key = account_5_key
    print('How much ether would you like to send:')
    value = input()

def executeOperation(value, send_acct, receive_acct, signing_key):
    # get the nonce
    nonce = web3.eth.getTransactionCount(send_acct)
    # build a trasnasction
    tx = {
        'nonce': nonce,
        'to': receive_acct,
        'value': web3.toWei(value, 'ether'),
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei')
    }

    # sign transaction
    signed_tx = web3.eth.account.signTransaction(tx, signing_key)

    # send transaction
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    # print txid
    print('Successfully sent ', value, ' ether!')
    print('Txid: ',web3.toHex(tx_hash))
    balance = web3.eth.getBalance(send_acct)
    print('remaining balance : ', web3.fromWei(balance, "ether"), 'ether')


connectToBlockchain()
# print('How much ether would you like to send:')
# value = input()
getVariables()
executeOperation(value, send_acct, receive_acct, signing_key)
