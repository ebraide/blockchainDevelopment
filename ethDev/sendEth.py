#!/usr/bin/env python3

import json,sys
from eth_account import account
from web3 import Web3
from web3.types import SignedTx
#import getEthBalance.py

#ganache_url = "http://127.0.0.1:7545"
ganache_url = "http://192.168.2.30:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))



account_1 = ""
account_1_key = ""
account_2 = "="
account_2_key = ""
account_3 = ""
account_3_key = ""
account_4 = ""
account_4_key = ""
account_5 = ""
account_5_key = ""


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
