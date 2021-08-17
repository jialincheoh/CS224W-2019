import snap
import collections
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def q1():
    G = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)

    cnt_node = 0
    cnt_self_edge = 0
    cnt_directed_edge = 0
    uedge = set()
    cnt_undirected_edge = 0
    reciedge = set()
    cnt_reciprocated_edge = 0
    cnt_zero_outd = 0
    cnt_zero_ind = 0
    cnt_ten_outd = 0
    cnt_ten_ind = 0

    for u in G.Nodes():
        cnt_node += 1
        for v in u.GetOutEdges():
            if v == u.GetId():
                cnt_self_edge += 1
            else:
                cnt_directed_edge += 1
                if (u.GetId(), v) not in uedge and (v, u.GetId()) not in uedge:
                    uedge.add((u.GetId(), v))
                    cnt_undirected_edge += 1
                reciedge.add((u.GetId(), v))
                if (v, u.GetId()) in reciedge:
                    cnt_reciprocated_edge += 1
        if u.GetInDeg() == 0:
            cnt_zero_ind += 1
        if u.GetInDeg() < 10:
            cnt_ten_ind += 1
        if u.GetOutDeg() == 0:
            cnt_zero_outd += 1
        if u.GetOutDeg() > 10:
            cnt_ten_outd += 1

    print("node ", cnt_node)
    print("self edge ", cnt_self_edge)
    print("directed edge ", cnt_directed_edge)
    print("undirected edge ", cnt_undirected_edge)
    print("reciprocated edge ", cnt_reciprocated_edge)
    print("zero out node ", cnt_zero_outd)
    print("zero in node ", cnt_zero_ind)
    print("ten out node ", cnt_ten_outd)
    print("ten in node ", cnt_ten_ind)


q1()



