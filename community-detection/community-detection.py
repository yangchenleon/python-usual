import networkx as nx
from networkx.algorithms.community import k_clique_communities
import matplotlib.pyplot as plt

file = '.\community-detection\dolphins\dolphins.gml'
G = nx.read_gml(file)
klist = list(k_clique_communities(G,4)) #list of k-cliques in the network. each element contains the nodes that consist the clique.
print(len(klist))

#plotting
pos = nx.spring_layout(G)
plt.clf()
nx.draw(G, pos = pos, with_labels=False)
nx.draw(G, pos = pos, nodelist = klist[0], node_color = 'b')
nx.draw(G, pos = pos, nodelist = klist[1], node_color = 'y')
nx.draw(G, pos = pos, nodelist = klist[2], node_color = 'r')
nx.draw(G, pos = pos, nodelist = klist[3], node_color = 'g')

plt.show()