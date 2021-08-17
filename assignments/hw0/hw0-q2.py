import snap
import collections
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def q2():
    G = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)

    stat = {}
    for node in G.Nodes():
        if node.GetOutDeg() != 0:
            stat[node.GetOutDeg()] = stat.get(node.GetOutDeg(), 0) + 1
    stat = collections.OrderedDict(sorted(stat.items(), key=lambda x: x[0]))
    x, y = np.array(list(stat.keys()), dtype=np.float64), np.array(list(stat.values()), dtype=np.float64)
    x, y = np.log10(x), np.log10(y)
    plt.bar(x, y)
    plt.plot(x, y, 'go', label='distribution')
    plt.xlabel('node out degree (log10 scale)')
    plt.ylabel('number of nodes (log10 scale)')
    plt.title('node out degree distribution')

    reg = np.polyfit(x, y, deg=1)
    ry = np.polyval(reg, x)
    plt.plot(x, ry, 'b^', label='regression')
    plt.legend()
    plt.show()
    print("regression: ", reg)


q2()