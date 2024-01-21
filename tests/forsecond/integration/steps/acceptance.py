from behave import given
from behave import when
from behave import then
from unittest.mock import mock_open
from unittest.mock import patch
from forsecond.__main__ import run

@given(u'a mock file containing the following data')
def step_impl(context):

    context.file_data = context.text


@when(u'we run the application with the mock file')
def step_impl(context):

    with patch("builtins.open", mock_open(read_data=context.file_data)):

        try:

            context.result = run('patched/path/to/file')

        except Exception as raised_exception:

            context.error = raised_exception


@then(u'we get the following output')
def step_impl(context):

    assert context.text == context.result, context.result


@then(u'it raises an exception with the message')
def step_impl(context):


    assert context.text == context.error.message, context.error.message
