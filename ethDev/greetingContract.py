#!/usr/bin/env python3

import json, sys
from eth_account import account
from eth_utils import address
from web3 import Web3, contract
from web3.types import SignedTx
#import getEthBalance.py

ganache_url_local = "http://127.0.0.1:7545"
ganache_url_remote = "http://192.168.2.30:7545"
kovan_url = "https://kovan.infura.io/v3/70a5f17851164f4890fd114ba74a18f2"
ropsten_url = "https://ropsten.infura.io/v3/70a5f17851164f4890fd114ba74a18f2"
mainnet_url = "https://mainnet.infura.io/v3/70a5f17851164f4890fd114ba74a18f2"
#ganache_url = "http://192.168.0.156:7545"
# web3 = Web3(Web3.HTTPProvider(ganache_url))

def chooseWeb3Provider():
    global web3
    print('Would you like to connect the \'mainnet\', \'testnet\' or \'ganache\'?')
    choice = input()
    if choice == 'mainnet':
        web3 = Web3(Web3.HTTPProvider(mainnet_url))
    elif choice == 'testnet':
        print('Are you running \'ropsten\' or \'kovan\' testnet?')
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
        elif choice == 'remote':
            web3 = Web3(Web3.HTTPProvider(ganache_url_remote))

def initVariables():
    global contract, address
    web3.eth.default_account = web3.eth.accounts[0]
    abi= json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
    address = web3.toChecksumAddress("0xDeA5C04c52445d4f2b4A95330A84B96F96be284a")
    contract = web3.eth.contract(address=address, abi= abi)

def connectToBlockchain():
    chooseWeb3Provider()
    initVariables()
    #print(web3.isConnected())
    connected = web3.isConnected()
    if connected == True:
        print('Connected!')
        print('Current block number: ', web3.eth.blockNumber)
        menu()
        #print(web3.eth.blockNumber)
    elif connected != True:
        print('Failed to connect..')
        sys.exit()

def menu():
    print('Select your option')
    print('1. Print current Greeting \n2. Set new greeting')
    # accepted_choice= {1,2}
    choice = input()
    # if choice in accepted_choice:
        # choice = str(choice)
    if choice == '1':
        printCurrentGreeting()
    if choice == '2':
        setNewGreeting()

def printCurrentGreeting():
    print(contract.functions.greet().call())

def setNewGreeting():
    print('Enter new greeting')
    newGreeting = input()
    tx_hash = contract.functions.setGreeting(newGreeting).transact()
    #tx_hash = contract.functions.setGreeting('Newnew World!').transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    print('Successfully set greeting: {}'.format(
    contract.functions.greet().call()
    ))
    print('Txid: ',web3.toHex(tx_hash))

connectToBlockchain()
# menu()
