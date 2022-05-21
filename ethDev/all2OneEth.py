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
"0x6D18a16c6201E392985b6E5e529e7d3F7118D0ec" : "d1e0e2f2bd8268029e16b8627914ea64836d72d2c582f23a7e6086bcec5c6b83",
"0x4625555dD0666E3fa6bdCE1ba0786b9314C3e250" : "9abd3d46916918ac8f92a93739bca681fbfb5c1b1c96faf563f27e4bbb1a524f",
"0x5Ff3a4eF9E4F01709E350BFE75be053BA4623325" : "d1a1fd487a51c38173c7ad6450a6ef97dc254cd52c69bb87bde28c87bf08d5bd",
"0xc86456E1D33B185D35c7E6baF09230CAD639E779" : "ddd2b9a36c5bd2bbd649017b1b8f82a3c4f789a9b306a27e81797be537f666ff",
"0x3a4A22281eb06D0233E93AfF5f6b4FF134257C37" : "6f208ccd1e0b3f595710ec68db3f397088f8ab3e086becf67c39b62895bec641",
"0xa31B5C8A48F3255AB991cbeB264bBf3D1Ef1E0E4" : "5d2901d333443b3302780d581e894ec1694c7eeb8ba038095598d19b7daaab3a",
"0xC55d50d21483A5D60cEcf632fdD615469CEee76f" : "b9573f7cd14d5df3f91167cb7636d3140a089d7ed96224d4c839459387f6a241",
"0x9F61b0D13ca2Bd9279F0Fc533974aFF7F6C6C670" : "d576abe851303a0bc22eece14f6d7688d4aaa22832c9892197e221f95c25025e",
"0xA3E3c92cb29dE3e352eE53bd263BC67138187724" : "d406a9bd90a78c848202dea378752a82b2c5997996a4d494f98ef7ec598b2d5b",
"0xDC2b59568269d44588bD2a87252CB3042077ABB7" : "15d1edfe2cca97a9afb6aea2d9fd409f9324ed55cc5bbf250f8dbfa2c048e73a"
}

address_2 = {
"0x1BaA1D300Ee73f9D232BE778140bB9c0da997E66" : "43de7ba914dd499383581dfb740611b33d489fcd26ee2c1882fd6074962a6d13",
"0x2ea58F3402170884B2DA47c2c8246D9D84e64985" : "f87bf133b68e8a250e103cdff938e7e2d2bbe9b24d5ba4cc5d18093557eee5f0", "0x7Fb1108D7241e1d2835fdf798704F71252Fd4E75" : "3328fd3853c61e5386ff06137868cb2541d28691cfb77a36217451d7c0e1bc56", "0x3603Cbe68cfe3fc5facA6f3721AD7F44b4Df6F4b" : "fc1c1dfe9577cc3b9585b04928177901d1e36c660f3f4ad90d129daf6f232165", "0xEB4355E5D4220e4aEa30a4E87Bd8b4896f390141" : "3d181e5f9c73c2688a890c4c5b4ad453a3ac47a3b577a0d32ace8df32588f9f8",
"0x53C08D9C7C302beAC0124Cf6801F9102475948fb" : "03922d926997772d5b8a1c9ec5310737cf8a4bb25521bd958a09fb949c8faa34",
"0xBAF437A76186a6c656fF362526551B1d62a34bB9" : "97c31a099fcc33daae376d5e11ca0c238688278190f3a63fa2bca4c3fa56db3d",
"0x3aB40c7fBe391B4557b772ED172396FfF405828C" : "bf922281169ba5ea1abef968a9c64df13199402313fe39f815b7f2b679c97fa1",
"0xAf777477508052459Abc00d5931B3131d218c1b0" : "7833d400a8507649473c0a3575e901ec207fa9ecfb29abf39600b06c42cfb8d0",
"0x63f04D51715966d3E188516Cfa9D3a96f31FCEF2" : "40781be81cf474e85ec3b75048a1d3aa314b81e757c0c0557d265a49e397f11f"
}

meta_address = {
"0x6279e621e15BeaD5383FE988F6C3a84A2aEfE1ca" : "af68230b91ff8cbceac8d964f2c0cc7035bfb02209d8306bda152096e9fc4cf8",
"0x6c4b4a617981A59a4804A491AF81eE5ce1a318A1" : "1d23565f21a9fd5e4c618e9e3b19002de4ffbb151e9d1b9d7a91b611a6792f93",
"0xbE732eDF7C72d1a2cC5e7d677C583f83C8fDECE5" : "ca463944a1b8688f7b5e4337df7e8912c0a96331ffc4736aa45ae50df90adeed",
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
