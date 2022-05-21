#!/usr/bin/env python3

from web3 import Web3
import sys

ganache_url_local = "http://127.0.0.1:7545"
ganache_url_remote = "http://192.168.2.30:7545"
mainnet_url = "https://mainnet.infura.io/v3/70a5f17851164f4890fd114ba74a18f2"
#web3 = Web3(Web3.HTTPProvider(infura_mainnet_url))

def chooseWeb3Provider():
    global web3
    print('Would you like to connect the \'mainnet\' or \'ganache\'?')
    choice = input()
    if choice == 'mainnet':
        web3 = Web3(Web3.HTTPProvider(mainnet_url))
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
        global latest
        latest= web3.eth.blockNumber
        # print('Current block number: ', web3.eth.blockNumber)
        print('Current block number: ', latest)
        executeOperation()
    elif connected != True:
        print('Failed to connect..')
        sys.exit()

def executeOperation():
    # print(web3.eth.getBlock(latest))

    for i in range(0, 10):
        print(web3.eth.getBlock(latest - i))
        print(web3.eth.getTransactionByBlock(latest-i, i))

    # block_hash = '0x9d6a8d8cf7dc7f9d52b9c799cf3db1923f4bdf996efdf15764e497f8c9c2090b'

    # print(web3.eth.getTransactionByBlock(latest, 2))

connectToBlockchain()
