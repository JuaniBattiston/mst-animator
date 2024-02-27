import math
from manim import *


class GraphScene(Scene):
    def construct(self):
        # TITLE
        title = Text(f"{self.algorithm.capitalize()}' Algorithm", font_size=48)
        self.play(Write(title))
        self.play(Unwrite(title))

        # NODES
        nodes = []
        node_labels = [
            Text(str(i + 1), font_size=32, color=WHITE) for i in range(self.num_nodes)
        ]
        node_pos = {i: v for i, v in enumerate(self.gen_node_pos())}

        for i in node_pos:
            nodes.append(
                [
                    Circle(
                        radius=0.3,
                        color="#73b4ff",
                        fill_opacity=1,
                    ).set_stroke(color="#479dff"),
                    node_pos[i],
                ]
            )

        edges = {}
        for k, i in enumerate(self.graph.graph_edges):
            tmp = []
            line = Line(node_pos[i[0]], node_pos[i[1]]).set_z_index(-1)
            tmp.append(line)
            label = Text(str(i[2]), font_size=20, color=WHITE).add_background_rectangle(
                color=BLACK, opacity=1
            )
            label.move_to((line.get_start() + line.get_end()) / 2)
            tmp.append(label)
            edges[f"{i[0]}-{i[1]}"] = tmp

        # ALGORITHM
        if self.algorithm == "prim":
            algo = self.graph.prim()
        if self.algorithm == "kruskal":
            algo = self.graph.kruskal()

        algo_edges = algo[0]
        edges_to_remove = []
        for i in edges.keys():
            if i not in algo_edges:
                edges_to_remove.append(i)

        # CREATE ANIMATION
        for i, k in enumerate(nodes):
            k[0].move_to(k[1])
            self.play(Create(k[0]), run_time=0.3)
            node_labels[i].move_to(k[1])
            self.play(Write(node_labels[i]), run_time=0.3)

        for i in edges:
            self.play(Create(edges[i][0]), run_time=0.3)
            self.play(Write(edges[i][1]), run_time=0.3)

        for i in algo_edges:
            self.play(
                edges[i][0].animate.set_color(GREEN),
                run_time=0.3,
            )
            self.wait(1)
        edges_group = VGroup(
            *[edges[i][0] for i in edges_to_remove]
            + [edges[i][1] for i in edges_to_remove]
        )
        self.play(
            FadeOut(edges_group),
            run_time=0.5,
        )
        min_path = Text(f"MST Weight: {algo[1]}", font_size=30).move_to(DOWN * 3.5)
        self.play(Write(min_path))
        self.wait(2)

    def setup_cfg(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def gen_node_pos(self):
        num_nodes = self.num_nodes
        div_one = math.ceil(num_nodes / 2)
        div_two = num_nodes - div_one
        node_pos = []

        for i in range(div_one):
            coord = i * 2 - div_one + 1
            offset = -1 if i % 2 == 0 else 0
            node_pos.append((coord, 2 + offset, 0))
        for i in range(div_two):
            coord = i * 2 - div_two + 1
            offset = -1 if i % 2 == 0 else 0
            node_pos.append((coord, -2 - offset, 0))

        return node_pos
