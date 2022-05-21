#! /usr/bin/env python3

from datetime import datetime
#import all2One as script
def userResponses(text):
    accepted_strings= ['list', 'more', 'import', 'one', 'multiple', 'multi']
    import_strings= ['list', 'more', 'import', 'multiple', 'multi']
    user_message= str(input()).lower()

    if user_message in accepted_strings:
        inputMnemonic()
        # script.connectToBlockChain()
    else:
        return (f'Check your entry and try again. \nYou entered {user_message}')
    # return f"accepted responses include: {accepted_strings}")

    return 'Error in entry'

def inputMnemonic():
    global mnemonic, filename
    mnemonic= []
    while True:
        update.message.reply_text("Would you like to enter 'one' or 'more' seed phrase?")
        update.message.reply_text("You can import your seed phrases by saving them in seed.txt, one per line")
        choice = input()
        counter = 0
        accepted_strings= {'list', 'more', 'import', 'one', 'multiple', 'multi'}
        import_strings= {'list', 'more', 'import', 'multiple', 'multi'}
        if choice in accepted_strings:
            if choice.lower() == 'one':
                update.message.reply_text(f'Enter your 12 word seed phrase')
                mnemonic.append(input(r''))
                Mnemonic2PrivateKey(mnemonic)
                break
            elif choice.lower() in import_strings:
                # update.message.reply_text('Enter filename:')
                # update.message.reply_text('Ensure you have your seed phrases saved in seed.txt, one per line')
                update.message.reply_text('Searching for seed.txt')
                filename= r'seed.txt'
                update.message.reply_text('Importing seed phrases...')
                readFile(filename)
                update.message.reply_text('Checking for whitespaces and formating errors')
                checkForWhitespace(mnemonic)
                # while '' in mnemonic:
                    # mnemonic.remove('')
                # update.message.reply_text(mnemonic)
                multipleMnemonic2PrivateKey(mnemonic)
                # Mnemonic2PrivateKey(mnemonic)
                break
            """elif choice.lower() == 'more':
                while '.' not in mnemonic:
                    update.message.reply_text(f'Enter your 12 word seed phrase')
                    update.message.reply_text("Enter '.' to continue")
                    mnemonic.append(input(r''))
                    counter= counter + 1
                checkForWhitespace(mnemonic)
                # mnemonic.remove('.')
                multipleMnemonic2PrivateKey(mnemonic)
                # for single_mnemonic in mnemonic:
                    # Mnemonic2PrivateKey(single_mnemonic)
                break"""

        else :
            update.message.reply_text(f'Check your entry and try again.. \nAccepted options include {accepted_strings}\nYou entered {choice} ')
            continue
