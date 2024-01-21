from forsecond.exceptions import InvalidGraphException
from forsecond.graph import find_most_philoprogenitive_node


class TestGraph:

    def test_it_solves_a_trivial_example(self):

        graph = {
            'a': []
        }

        parent, order = find_most_philoprogenitive_node(graph)
        assert 'a' == parent
        assert 1 == order

    def test_it_solves_a_minimum_functional_example(self):

        graph = {
            'a': [],
            'b': ['a'],
        }

        parent, order = find_most_philoprogenitive_node(graph)
        assert 'b' == parent
        assert 2 == order

    def test_it_solves_a_communtative_example(self):

        graph = {
            'a': ['b'],
            'b': ['c'],
            'c': ['a'],
        }

        parent, order = find_most_philoprogenitive_node(graph)
        assert parent in ['a', 'b', 'c']
        assert 3 == order

    def test_it_solves_a_fully_disconnected_example(self):

        graph = {
            'a': [],
            'b': [],
            'c': [],
        }

        parent, order = find_most_philoprogenitive_node(graph)
        assert parent in ['a', 'b', 'c']
        assert 1 == order

    def test_it_solves_a_bifurcated_example(self):

        graph = {
            'a': [],
            'b': ['a'],
            'c': [],
            'd': ['c'],
        }

        parent, order = find_most_philoprogenitive_node(graph)
        assert parent in ['b', 'd']
        assert 2 == order

    def test_it_selects_the_correct_graph_from_an_example_disordered_pairing(self):

        graph = {
            'a': ['e'],
            'b': ['c'],
            'c': ['d'],
            'd': [],
            'e': [],
        }

        parent, order = find_most_philoprogenitive_node(graph)
        assert 'b' == parent
        assert 3 == order
