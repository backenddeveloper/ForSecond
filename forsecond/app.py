import sys
from forsecond.file import graph_from_file
from forsecond.graph import find_most_philoprogenitive_node


def run(filename):

    graph = graph_from_file(filename)
    parent, order = find_most_philoprogenitive_node(graph)

    return f'If you start from {parent}, you can reach {order} <players>'
