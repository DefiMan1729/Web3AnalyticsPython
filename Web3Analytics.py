import json
from web3 import Web3, HTTPProvider
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import dotenv
import os
from dotenv import load_dotenv
load_dotenv()


blockchain_address = os.getenv("GANACHE_URL")

# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account
web3.eth.defaultAccount = web3.eth.accounts[0]

#If you are using Infura to connect to public testnet your intance will look something like this
#web3_ropsten = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/<API_KEY>'))

#define the graph object
G=nx.DiGraph()

#I used the local contract JSON ABI path 
compiled_contract_path = os.getenv("ABI_JSON_PATH")
with open(compiled_contract_path) as file:
    contract_json = json.load(file)  
    contract_abi = contract_json['abi']  

#you can also paste the ABI directly. Copying the ABI is very easy if you are using Remix
#contract_abi='<ABI>'

deployed_contract_address = Web3.toChecksumAddress(os.getenv("CONTRACT_ADDRESS"))
# deployed_contract_address = Web3.toChecksumAddress(0xd154b3bEB9A1461DcB529DbF49E77d7ccD6521F9)

# Call function (this is not persisted to the blockchain)
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
message1 = contract.functions.name().call()
print(message1)
message2 = contract.functions.symbol().call()
print(message2)

#mint token from default address web3.eth.defaultAccount = web3.eth.accounts[0] to itself
tx_hs = contract.functions.safeMint(web3.eth.accounts[0],'defiman1729.eth.limo').transact()
receipt = web3.eth.get_transaction_receipt(tx_hs)
# print(receipt)

_to=contract.events.Transfer().processReceipt(receipt)[0]['args']['to']
print(_to)
_from=contract.events.Transfer().processReceipt(receipt)[0]['args']['from']
print(_from)
_tokenid=contract.events.Transfer().processReceipt(receipt)[0]['args']['tokenId']
print(_tokenid)

G.add_node(_from)
G.add_node(_to)
G.add_edge(_from,_to)


#transfer token from default address accounts[0]  accounts[1] to 
tx_hs = contract.functions.safeTransferFrom(web3.eth.accounts[0],web3.eth.accounts[1],_tokenid).transact()
receipt = web3.eth.get_transaction_receipt(tx_hs)
print(receipt)

_to=contract.events.Transfer().processReceipt(receipt)[0]['args']['to']
print(_to)
_from=contract.events.Transfer().processReceipt(receipt)[0]['args']['from']
print(_from)
_tokenid=contract.events.Transfer().processReceipt(receipt)[0]['args']['tokenId']
print(_tokenid)

G.add_node(_from)
G.add_node(_to)
G.add_edge(_from,_to)



web3.eth.defaultAccount = web3.eth.accounts[1]
#transfer token from default address accounts[1]  accounts[2] to 
tx_hs = contract.functions.safeTransferFrom(web3.eth.accounts[1],web3.eth.accounts[2],_tokenid).transact()
receipt = web3.eth.get_transaction_receipt(tx_hs)
print(receipt)

_to=contract.events.Transfer().processReceipt(receipt)[0]['args']['to']
print(_to)
_from=contract.events.Transfer().processReceipt(receipt)[0]['args']['from']
print(_from)
_tokenid=contract.events.Transfer().processReceipt(receipt)[0]['args']['tokenId']
print(_tokenid)

G.add_node(_from)
G.add_node(_to)
G.add_edge(_from,_to)


web3.eth.defaultAccount = web3.eth.accounts[2]
#transfer token from default address accounts[2]  accounts[0] to 
tx_hs = contract.functions.safeTransferFrom(web3.eth.accounts[2],web3.eth.accounts[0],_tokenid).transact()
receipt = web3.eth.get_transaction_receipt(tx_hs)
print(receipt)

_to=contract.events.Transfer().processReceipt(receipt)[0]['args']['to']
print(_to)
_from=contract.events.Transfer().processReceipt(receipt)[0]['args']['from']
print(_from)
_tokenid=contract.events.Transfer().processReceipt(receipt)[0]['args']['tokenId']
print(_tokenid)

G.add_node(_from)
G.add_node(_to)
G.add_edge(_from,_to)

pos = nx.circular_layout(G)    
nx.draw(G, pos, with_labels = True, edge_color = 'b', arrowsize=9, arrowstyle='fancy')   
plt.show()
