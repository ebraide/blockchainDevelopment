#!/usr/bin/env python3

import json,sys
from web3 import Web3

ganache_url_local = "http://127.0.0.1:7545"
ganache_url_remote = "http://192.168.2.30:7545"
mainnet_url = "https://mainnet.infura.io/v3/70a5f17851164f4890fd114ba74a18f2"
kovan_url = "https://kovan.infura.io/v3/70a5f17851164f4890fd114ba74a18f2"
ropsten_url = "https://ropsten.infura.io/v3/70a5f17851164f4890fd114ba74a18f2"
bsc= "https://bsc-dataseed.binance.org/"
#web3 = Web3(Web3.HTTPProvider(infura_mainnet_url))
# web3 = Web3(Web3.HTTPProvider(ganache_url))

def chooseWeb3Provider():
    global web3
    print('Would you like to connect the \'mainnet\', \'testnet\' or \'ganache\' or \'Binance\'?')
    choice = input()
    if choice == 'mainnet':
        web3 = Web3(Web3.HTTPProvider(mainnet_url))
    elif choice.lower() == 'binance':
        web3 = Web3(Web3.HTTPProvider(bsc))
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

def connectToBlockchain():
    chooseWeb3Provider()
    #print(web3.isConnected())
    connected = web3.isConnected()
    if connected == True:
        print('Connected!')
        print('Current block number: ', web3.eth.blockNumber)
        executeOperation()
    elif connected != True:
        print('Not connected..')
        sys.exit()

def executeOperation():
    print("Enter the wallet address for which you want to check balance:")
    balance = web3.eth.getBalance(input())
    print(web3.fromWei(balance, "ether"), 'ether')

connectToBlockchain()
# executeOperation()
