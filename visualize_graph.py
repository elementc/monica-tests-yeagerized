from yeager import nodes, edges
from graph_tool.all import *

import state_transitions.headerpage
import state_transitions.contacts
import state_transitions.login

def graph():
    g = Graph()
    g.set_directed(True)

    y_node_map = {}
    v_node_map = g.new_vertex_property("string")
    e_map = g.new_edge_property("string")

    for node in nodes:
        v = g.add_vertex()
        y_node_map[node] = v
        v_node_map[v] = str(node)

    for src in edges.keys():
        for dest in edges[src]:
            e = g.add_edge(y_node_map[src], y_node_map[dest[0]])
            e_map[e] = str(dest[1])

    # pos = radial_tree_layout(g, y_node_map[None])
    # pos = sfdp_layout(g)
    # pos = random_layout(g)
    # pos = fruchterman_reingold_layout(g)
    pos = arf_layout(g)
    graph_draw(g, pos=pos, output_size=(1920,1080), vertex_text=v_node_map,
        edge_text=e_map, vertex_size=1, edge_pen_width=1)

if __name__ == "__main__":
    graph()
