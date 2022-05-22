#!/usr/bin/env python3

import json, sys
from eth_account import account
from web3 import Web3
from web3.types import SignedTx
#import getEthBalance.py

ganache_url_local = "http://127.0.0.1:7545"
ganache_url_remote = "http://192.168.2.30:7545"
kovan_url = "https://kovan.infura.io/v3/70a5f17851164f4890fd114ba74a18f2"
ropsten_url = "https://ropsten.infura.io/v3/70a5f17851164f4890fd114ba74a18f2"
mainnet_url = "https://mainnet.infura.io/v3/70a5f17851164f4890fd114ba74a18f2"
#ganache_url = "http://192.168.0.156:7545"
# web3 = Web3(Web3.HTTPProvider(ganache_url))
global address, address_2

address = {
"addresss" : "private key"
}

address_2 = {
"addresss" : "private key"
}

meta_address = {
"addresss" : "private key"
}

def connectToBlockchain():
    chooseWeb3Provider()
    connected = web3.isConnected()
    if connected == True:
        print('Connected!')
        print('Current block number: ', web3.eth.blockNumber)
        getVariables()
        #print(web3.eth.blockNumber)
    elif connected != True:
        print('Failed to connect..')
        sys.exit()

def chooseWeb3Provider():
    global web3, working_address
    print('Would you like to connect the \'mainnet\', \'testnet\' or \'ganache\'?')
    choice = input()
    if choice == 'mainnet':
        web3 = Web3(Web3.HTTPProvider(mainnet_url))
    elif choice == 'testnet':
        print('Are you running \'ropsten\' or \'kovan\' testnet?')
        working_address = meta_address
        choice = input()
        if choice == 'ropsten':
            web3 = Web3(Web3.HTTPProvider(ropsten_url))
        elif choice == 'kovan':
            web3 = Web3(Web3.HTTPProvider(kovan_url))
    elif choice == 'ganache':
        print('Are you running ganache \'local\' or \'remote\'?')
        choice = input()
        if choice == 'local':
            web3 = Web3(Web3.HTTPProvider(ganache_url_local))
            working_address = address
        elif choice == 'remote':
            web3 = Web3(Web3.HTTPProvider(ganache_url_remote))
            working_address = address_2

    # print('Are you running ganache \'local\' or \'remote\'?')
    # choice = input()
    # if choice == 'local':
    #     web3 = Web3(Web3.HTTPProvider(ganache_url_local))
    # elif choice == 'remote':
    #     web3 = Web3(Web3.HTTPProvider(ganache_url_remote))

def getVariables():
    global send_acct, receive_acct, signing_key, value
    print('Enter the wallet address from which you want to send ether')
    send_acct = input()
    print("Enter the wallet address to which you want to send ether")
    receive_acct = input()
    if receive_acct == 'all':
        #send_acct = send_acct
        for addy in working_address.keys():
            if addy == send_acct:
                print('Same acct!')
            else:
                receive_acct = addy
                signing_key = working_address[send_acct]
                value = web3.eth.getBalance(send_acct) / 10
                value = web3.fromWei(value, "ether") #/ 10
                executeOperation(value, send_acct, receive_acct, signing_key)

    elif send_acct in working_address:
         #send_acct = send_acct
         signing_key = working_address[send_acct]
         print('How much ether would you like to send:')
         value = input()
         executeOperation(value, send_acct, receive_acct, signing_key)
         # print("Enter the wallet address to which you want to send ether")
         # receive_acct = input()

    elif send_acct == 'all':
        for addy in working_address.keys():
            if addy == receive_acct:
                print('Same acct!')
            else:
                send_acct = addy
                signing_key = working_address[addy]
                value = web3.eth.getBalance(addy)
                value = web3.fromWei(value, "ether") - 1
                executeOperation(value, send_acct, receive_acct, signing_key)

    # elif send_acct in meta_address:
    #      #send_acct = send_acct
    #      signing_key = meta_address[send_acct]
    #      print('How much ether would you like to send:')
    #      value = input()
    #      executeOperation(value, send_acct, receive_acct, signing_key)
    #      # print("Enter the wallet address to which you want to send ether")
    #      # receive_acct = input()
    # elif send_acct in address_2:
    #      #send_acct = send_acct
    #      signing_key = address_2[send_acct]
    #      print('How much ether would you like to send:')
    #      value = input()
    #      executeOperation(value, send_acct, receive_acct, signing_key)
    #      # print("Enter the wallet address to which you want to send ether")
    #      # receive_acct = input()

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
    #print('remaining balance : ', web3.fromWei(balance, "ether"), 'ether')


connectToBlockchain()
# print('How much ether would you like to send:')
# value = input()
# getVariables()
#executeOperation(value, send_acct, receive_acct, signing_key)
