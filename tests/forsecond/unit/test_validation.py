from unittest.mock import mock_open
from unittest.mock import patch
from pytest import raises
from forsecond.file import graph_from_file
from forsecond.exceptions import ValidationException


class TestFileValidation:

    def test_it_accepts_a_simple_valid_example(self):

        data_in_file = '''
George,Beth, Sue
Rick,Anne
Anne,Beth
Beth, Anne  ,George
 Sue,Beth
'''

        with patch("builtins.open", mock_open(read_data=data_in_file)):

            assert {
                'george': ['beth', 'sue'],
                'rick': ['anne'],
                'anne': ['beth'],
                'beth': ['anne', 'george'],
                'sue': ['beth']
            } == graph_from_file('patched/path/to/file')

    def test_it_ignores_empty_lines(self):

        data_in_file = '''
George, Sue

Anne,Beth
'''

        with patch("builtins.open", mock_open(read_data=data_in_file)):

            assert {
                'george': ['sue'],
                'anne': ['beth'],
            } == graph_from_file('patched/path/to/file')

    def test_it_rejects_an_empty_file(self):

        data_in_file = ''

        with patch("builtins.open", mock_open(read_data=data_in_file)):

            with raises(ValidationException) as raised_exception:

                graph_from_file('patched/path/to/file')

            assert raised_exception.value.message == 'empty graph generated from file'

    def test_it_rejects_a_non_alphanumeric_name(self):

        data_in_file = '''
George,Beth, Sue
Rick,Anne!!!
Anne,Beth
'''

        with patch("builtins.open", mock_open(read_data=data_in_file)):

            with raises(ValidationException) as raised_exception:

                graph_from_file('patched/path/to/file')

            assert raised_exception.value.message == 'found a non-alphanumeric name: anne!!!'

    def test_it_rejects_an_empty_name(self):

        data_in_file = '''
George,, Sue
Rick,Anne
Anne,Beth
'''

        with patch("builtins.open", mock_open(read_data=data_in_file)):

            with raises(ValidationException) as raised_exception:

                graph_from_file('patched/path/to/file')

            assert raised_exception.value.message == 'found an empty name'

    def test_it_rejects_a_duplicate_name(self):

        data_in_file = '''
Rick,Anne
Anne,Beth
Rick,Anne
'''

        with patch("builtins.open", mock_open(read_data=data_in_file)):

            with raises(ValidationException) as raised_exception:

                graph_from_file('patched/path/to/file')

            assert raised_exception.value.message == 'found a duplicate name: rick'
