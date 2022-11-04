# Web3 Analytics Python 

Public blockchain networks allow us to access radical new datasets that can reveal patterns in the movement of Assets, Cryptos or NFTs, which in turn can be leveraged for monitoring transactions and potentially aiding AML/CFT initiatives.
This repo is a introduction to Network Analysis using event data emitted from a blockchain transaction. Such analysis can enable fraud investigators to uncover and prevent increasingly sophisticated fraud schemes with more ease and confidence.

>*In Solidity, events are dispatched signals the smart contracts can fire. Dapps, or anything connected to Ethereum JSON-RPC API, can listen to these events and act accordingly. An event can also be indexed so that the event history is searchable later. https://ethereum.org/en/developers/tutorials/logging-events-smart-contracts/*

In this example I have leveraged the default "Transfer" event that gets emitted from an Openzepelin ERC721 contract.
```shell
emit Transfer(from, to, tokenId);
```
When a NFT is transferred from one account to another, I capure the "from" and "to" attributes of the transfer event to draw a directed graph connecting the "from" and the "to" nodes. 


```shell
Code Structure
1. Import libraries (web3, JSON etc)
2. Establish connection with blockchain RPC (in this case: Ganache)
3. Create Graph object
4. Add graph nodes and edges from the parameters of the "Transfer" event trigged by Solidity contract 
5. Plot graph
6. Generate additional statistics
```

Sample graph generated using python's Networkx package

![image](https://user-images.githubusercontent.com/115624087/198863254-4928d5ca-5829-426b-8912-de90df521651.png)
![image](https://user-images.githubusercontent.com/115624087/198870286-7aea8b7e-cba9-432b-a3f3-25fafe1a349c.png)




**Centrality Analysis**

*Centrality measures are a vital tool for understanding the structural dynamics of nodes in a network.*

Degree Centrality: it scores the number of connections/links held by each node of the network. It is useful to find the most influential or connected account.

Betweenness Centrality: it measures the number of times a node lies on the shortest path between other nodes. A high betweenness score implies that the account holds high degree of influence across multiple network clusters.

Closeness Centrality: it scores each node based on their ‘closeness’ to all other nodes in the network. It usually implies a good 'broadcaster'.

Eigen Centrality: it takes into account how well connected a node is, and how many links their connections have, and so on through the network. It can identify the account that has influence over the entire network.

These measures can be used to identify suspicious accounts.
