from forsecond.exceptions import InvalidGraphException


def find_most_philoprogenitive_node(graph):

    # This might raise a validation exception
    # TODO: implement
    # validate_graph(graph)

    max_reachable_count = 0
    max_reachable_node = None

    for node in graph:

        visited = {n: False for n in graph}
        count = [0]
        depth_first_search_count_reachable(graph, node, visited, count)

        if count[0] > max_reachable_count:

            max_reachable_count = count[0]
            max_reachable_node = node

    return max_reachable_node, max_reachable_count


def depth_first_search_count_reachable(graph, node, visited, count):

    visited[node] = True
    count[0] += 1

    for neighbor in graph[node]:

        if not visited[neighbor]:

            depth_first_search_count_reachable(graph, neighbor, visited, count)


def validate_graph(graph):

    raise NotImplementedError
