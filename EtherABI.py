from web3 import Web3, HTTPProvider
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import dotenv
import os
from dotenv import load_dotenv
load_dotenv()
import requests
import json

response = requests.get(os.getenv("ETHERSCAN_URL"))
contract_json = json.loads(response.text)
contract_abi = contract_json['result']  

web3 = Web3(Web3.HTTPProvider(os.getenv("INFURA_URL")))


deployed_contract_address = Web3.toChecksumAddress(os.getenv("SEPOLIA_CONTRACT_ADDRESS"))
print(deployed_contract_address)
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
message1 = contract.functions.name().call()
print(message1)
message2 = contract.functions.symbol().call()
print(message2)

# _to=contract.events.Transfer()
# print(_to)
# event_filter = contract.events.Transfer.createFilter(fromBlock=2182561)
# print(event_filter)
_from=contract.events.Transfer.getLogs(fromBlock=2182561)[0]['args']['from']
_to=contract.events.Transfer.getLogs(fromBlock=2182561)[0]['args']['to']
_tokenId=contract.events.Transfer.getLogs(fromBlock=2182561)[0]['args']['tokenId']

G=nx.DiGraph()
G.add_node(_from)
G.add_node(_to)
G.add_edge(_from,_to)

pos = nx.circular_layout(G)    
nx.draw(G, pos, with_labels = True, edge_color = 'b', arrowsize=9, arrowstyle='fancy')   
plt.show()



# _from=contract.events.Transfer().processReceipt(receipt)[0]['args']['from']
# print(_from)
# _tokenid=contract.events.Transfer().processReceipt(receipt)[0]['args']['tokenId']
# print(_tokenid)