# Web3 Analytics Python 

Public blockchain networks allow us to access radical new datasets that can reveal patterns in the movement of Assets, Cryptos or NFTs, which in turn can be leveraged for monitoring transactions and potentially aiding AML/CFT initiatives.
This repo is a introduction to Network Analysis using event data emitted from a blockchain transaction. Such analysis can enable fraud investigators to uncover and prevent increasingly sophisticated fraud schemes with more ease and confidence.

```shell
1. Import libraries
2. Establish connection with blockchain RPC (in this case Ganache)
3. Create Graph object
4. Add graph nodes and edges by from Transfer event trigged by Solidity contract 
5. Plot graph
6. Generate additional statistics
```

![image](https://user-images.githubusercontent.com/115624087/198863254-4928d5ca-5829-426b-8912-de90df521651.png)
![image](https://user-images.githubusercontent.com/115624087/198863296-88596fc1-f1ef-494b-a71f-bda52ea5b1ac.png)



**Centrality Analysis**

Centrality measures are a vital tool for understanding the structural dynamics of nodes in a network.

Degree Centrality: it scores the number of connections/links held by each node of the network. It is useful to find the most influential or connected account.

Betweenness Centrality: it measures the number of times a node lies on the shortest path between other nodes. A high betweenness score implies that the account holds high degree of influence across multiple network clusters.

Closeness Centrality: it scores each node based on their ‘closeness’ to all other nodes in the network. It usually implies a good 'broadcaster'.

Eigen Centrality: it takes into account how well connected a node is, and how many links their connections have, and so on through the network. It can identify the account that has influence over the entire network.

These measures can be used to mark suspicious accounts.
