#!/usr/bin/env python3
# all2One version 2.0
import json, sys, os, re
from eth_account import account
from eth_account import Account
from web3 import Web3
from web3.types import SignedTx
#import getEthBalance.py

def connectToBlockchain():
    chooseWeb3Provider()
    connected = web3.isConnected()
    if connected == True:
        print('Connected!')
        print(f'Current block number: {web3.eth.blockNumber}')
        getVariables()
        #print(web3.eth.blockNumber)
    elif connected != True:
        print('Failed to connect..')
        sys.exit()

def chooseWeb3Provider():
    global web3, working_address, address
    address = {}
    ganache_url_local = "http://127.0.0.1:7545"
    ropsten_url = "https://ropsten.infura.io/v3/70a5f17851164f4890fd114ba74a18f2"
    mainnet_url = "https://mainnet.infura.io/v3/70a5f17851164f4890fd114ba74a18f2"
    print("Would you like to connect the 'mainnet' or 'testnet'?")
    choice = input()
    if choice.lower() == 'mainnet':
        web3 = Web3(Web3.HTTPProvider(mainnet_url))
        #inputMnemonic()
        #Mnemonic2PrivateKey(mnemonic)
        working_address = address
    elif choice.lower() == 'testnet':
        web3 = Web3(Web3.HTTPProvider(ropsten_url))
        working_address = address

def getVariables():
    global send_acct, receive_acct, signing_key, value, count
    inputMnemonic()
    #regex2Format(mnemonic)
    # print(address.values())
    #regex2Format(address.values())
    print("Enter the wallet address to which you want to send coins")
    receive_acct = input()
    print('Enter the wallet address from which you want to send coins')
    send_acct = input()

    # send from all wallets to one if send_acct option is set to all
    if send_acct == 'all':
        count= 0
        for addy in working_address.keys():
            count+=1
            if addy == receive_acct:
                print(f'Same account!')
            else:
                try:
                    send_acct = addy
                    signing_key = working_address[addy]
                    getBalances(addy)
                    # balance = web3.eth.getBalance(addy)
                    # value = float(web3.fromWei(balance, "ether")) - 0.1
                    balance = web3.fromWei(web3.eth.getBalance(addy), "ether")
                    # print(balance)
                    value = float(balance) - 0.2
                    # print(f'current value: {value}')
                    # executeOperation(value, send_acct, receive_acct, signing_key)
                except ValueError:
                    print(f"Balance too low to withdraw: {balance}")
                    print(f'current value: {value}')

    # share wallet balance to all wallets from one if receive_acct option is set to all
    elif receive_acct == 'all':
        count= 0
        for addy in working_address.keys():
            count+=1
            if addy == send_acct:
                print('Same acct!')
            else:
                try:
                    receive_acct = addy
                    signing_key = working_address[send_acct]
                    balance = web3.fromWei(web3.eth.getBalance(send_acct), "ether") #/ 10
                    value =  float(balance) / float(num_of_accts)
                    # print(f'current value: {value}')
                    # value = web3.eth.getBalance(send_acct) / 10
                    # value = web3.fromWei(value, "ether") #/ 10
                    executeOperation(value, send_acct, receive_acct, signing_key)
                except ValueError as e:
                    print(f"Value Error at wallet {count}")
                    print(f"Error: {e}")
                    # print(f"Balance too low to withdraw: {balance}")
                    print(f"Balance: {balance}")
                    print(f'current value: {value}')
    # send from one wallets to another if send_acct option is set to wallet address
    elif send_acct in working_address:
         #send_acct = send_acct
         signing_key = working_address[send_acct]
         print(f'How much ether would you like to send:')
         value = input()
         executeOperation(value, send_acct, receive_acct, signing_key)
         # print("Enter the wallet address to which you want to send ether")
         # receive_acct = input()"""

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
    print(f'Successfully sent {value} eth!')
    print(f'Txid: {web3.toHex(tx_hash)}')
    balance = web3.eth.getBalance(send_acct)
    print(f'remaining balance: {web3.fromWei(balance, "ether")}, eth')

def Mnemonic2PrivateKey(mnemonic):
    Account.enable_unaudited_hdwallet_features()
    try:
        acct = Account.from_mnemonic(mnemonic)
    except Exception as e:
        print(f"Error with seed phrase")
    acct = Account.from_mnemonic(mnemonic)
    #print(f'Wallet address: {acct.address}')
    #print(f'Wallet private key: {acct.key}')
    address[acct.address]= acct.key

def multipleMnemonic2PrivateKey(mnemonic):
    for single_mnemonic in mnemonic:
        # print(single_mnemonic)
        Mnemonic2PrivateKey(single_mnemonic)

def checkForWhitespace(mnemonic):
    while '' in mnemonic:
        try:
            mnemonic.remove('')
        except Exception as e:
            print(f"whitespace error")
    while '.' in mnemonic:
        try:
            mnemonic.remove('.')
        except Exception as e:
            print(f"dot error")
    print(f"Mnemonic has been formated.")

def inputMnemonic():
    global mnemonic, filename, num_of_accts
    mnemonic= []
    while True:
        print("Would you like to enter 'one' or 'more' seed phrase?")
        print("You can import your seed phrases by saving them in seed.txt, one per line")
        choice = input()
        counter = 0
        accepted_strings= {'list', 'more', 'import', 'one', 'multiple', 'multi'}
        import_strings= {'list', 'more', 'import', 'multiple', 'multi'}
        if choice in accepted_strings:
            if choice.lower() == 'one':
                print(f'Enter your 12 word seed phrase')
                mnemonic.append(input(r''))
                Mnemonic2PrivateKey(mnemonic)
                break
            elif choice.lower() in import_strings:
                # print('Enter filename:')
                # print('Ensure you have your seed phrases saved in seed.txt, one per line')
                print('Searching for seed.txt')
                try:
                    filename= r'seed.txt'
                    print('Importing seed phrases...')
                    readFile(filename)
                    print('Checking for whitespaces and formating errors')
                    checkForWhitespace(mnemonic)
                    multipleMnemonic2PrivateKey(mnemonic)
                    num_of_accts= len(address.keys())
                    print(f'{num_of_accts} seed phrases imported.')
                    break
                except ValueError:
                    print(f"seed.txt file not found. Confirm you have your seed phrases in seed.txt to proceed")
                    continue
            """elif choice.lower() == 'more':
                while '.' not in mnemonic:
                    print(f'Enter your 12 word seed phrase')
                    print("Enter '.' to continue")
                    mnemonic.append(input(r''))
                    counter= counter + 1
                checkForWhitespace(mnemonic)
                # mnemonic.remove('.')
                multipleMnemonic2PrivateKey(mnemonic)
                # for single_mnemonic in mnemonic:
                    # Mnemonic2PrivateKey(single_mnemonic)
                break"""

        else :
            print(f'Check your entry and try again.. \nAccepted options include {accepted_strings}\nYou entered {choice} ')
            continue

def readFile(filename):
    # global split_data
    f= open(os.path.join('./', filename), 'r')  # open for 'read mode'
    all_data= f.read()
    split_data= all_data.split('\n')
    #print(f'split data: \n{split_data}')
    for line in split_data:
        mnemonic.append(str(line))
    f.close()

def regex2Format(text):
    matches= []
    formatRegex = re.compile(r'''(
    ([HexBytes])        # numbers before comma
    (()             # opening brackets
    (')            # opening quotation mark
    (.{66})         # 66 character private key
    (')            # closing quotation mark
    ())             # closing brackets

    )''', re.VERBOSE)
    for key in text:
        print(key)
        count= 1
        for addy in working_address:
            print(working_address[count])
            count += 1
        formatRegex.findall(key)
        # for groups in formatRegex.findall(key):
            # matches.append(groups[3])
        #matches = '-'.join(numRegex.findall(text))
        #matches = str(matches)
    print('\n'.join(matches))

def getBalances(address):
    global balances
    balances= {}
    abi= json.loads( '[{"constant":true,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finishMinting","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_releaseTime","type":"uint256"}],"name":"mintTimelocked","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[],"name":"MintFinished","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')
    filename= r'contract_address.txt'
    readTokenList(filename)
    # print(f'{sys.max}')
    for token_address in tokens:
        # address= line
        try:
            contract = web3.eth.contract(address=token_address, abi= abi)
            #print(contract)
            #rich_address= '0x23735750a6ed0119e778d9bb969137df8cc8c3d1'
            # totalSupply = contract.functions.totalSupply().call()
            # name= contract.functions.name().call()
            symbol= contract.functions.symbol().call()
            # balance = contract.functions.balanceOf(address).call()
            balance = int(web3.fromWei(contract.functions.balanceOf(address).call(), "ether"))
            print(f'{symbol} balance of wallet {count}: {balance}')
            # print(f'{symbol} balance of {address}: {balance}')
            # print(f'Token name {name}')
            # print(f'Token symbol {symbol}')
        except OverflowError as of:
            print(f"OverflowError at {symbol}.")
        except ValueError:
            print(f"Value Error at {symbol}")

def readTokenList(filename):
    global tokens
    tokens= []
    f= open(os.path.join('./', filename), 'r')  # open for 'read mode'
    all_data= f.read()
    split_data= all_data.split('\n')
    #print(f'split data: \n{split_data}')
    for line in split_data:
        tokens.append(str(line))
    f.close()

connectToBlockchain()
