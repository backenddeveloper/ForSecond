from unittest.mock import patch
from forsecond.app import run


class TestApp:

    @patch('forsecond.app.graph_from_file')
    @patch('forsecond.app.find_most_philoprogenitive_node')
    def test_it_follows_the_expected_soluton_logic(self, graph_patch, file_patch):

        file_patch.return_value = 'some_graph'
        graph_patch.return_value = 'some_parent', 'some_order'

        assert 'If you start from some_parent, you can reach some_order <players>' == run('path/to/mock/file')
        file_patch.assert_called_with('path/to/mock/file')
        graph_patch.assert_called_with('some_graph')
