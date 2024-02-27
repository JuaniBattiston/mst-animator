from manim import *
from manim.utils.file_ops import open_file as open_media_file

from graph import Graph
from scene_loader import GraphScene

import sys


def load_grahp():
    num_nodes = int(input("Enter the number of nodes: "))
    graph = Graph(num_nodes)
    while True:
        valid_node_input = f"1-{num_nodes}"
        from_node = int(input(f"Enter the start node ({valid_node_input}): "))
        to_node = int(input(f"Enter the end node ({valid_node_input}): "))
        weight = int(input(f"Enter the weight: "))
        graph.add_undirected_edge(from_node - 1, to_node - 1, weight)
        more_edges = input("Do you want to add more edges? (y/n): ")
        if more_edges.lower() == "n":
            break

    return graph


def load_example_graph():
    graph = Graph(6)
    graph.add_undirected_edge(0, 1, 2)
    graph.add_undirected_edge(0, 2, 4)
    graph.add_undirected_edge(1, 2, 1)
    graph.add_undirected_edge(1, 3, 7)
    graph.add_undirected_edge(2, 3, 3)
    graph.add_undirected_edge(2, 4, 5)
    graph.add_undirected_edge(3, 4, 6)
    graph.add_undirected_edge(4, 5, 2)
    return graph


def main():
    algorithm_table = {1: "kruskal", 2: "prim"}
    selected_algorithm = int(
        input("Enter the algorithm 1 for kruskal and 2 for prim: ")
    )

    if sys.argv[-1] == "example":
        graph = load_example_graph()
    else:
        graph = load_grahp()

    scene = GraphScene()
    scene.setup_cfg(
        num_nodes=graph.num_nodes,
        graph=graph,
        algorithm=algorithm_table[selected_algorithm],
    )
    scene.render(preview=True)
    open_media_file(scene.renderer.file_writer.movie_file_path)


if __name__ == "__main__":
    main()
