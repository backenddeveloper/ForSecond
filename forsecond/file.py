import re
from forsecond.exceptions import ValidationException


def graph_from_file(filename):

    graph = {}

    # Any exceptions occurred in opening and reading
    # the file will be allowed to propagate and log elsewhere
    with open(filename) as file:

        for line in file:

            # Remove newlines, tabs, carriage returns and line ends
            line = line.strip()

            # Ignore blank lines
            if '' == line:
                continue

            # Then we split the line by comma
            parts = line.split(',')

            # Then we remove all white space from each name
            parts = [p.strip() for p in parts]

            # Then we convert all names to lowercase
            parts = [p.lower() for p in parts]

            # The we check all of the parts contain a valid name
            validate_names(parts)

            # Then we check for the existence of a duplicate line
            if parts[0] in graph:
                raise ValidationException(f'found a duplicate name: {parts[0]}')

            # The graph might only contain only the first name,
            # here we abuse a Python feature to set it as an empty array
            graph[parts[0]] = parts[1:]

    # Validate that the file isn't semantically empty
    if 0 == len(graph):

        raise ValidationException('empty graph generated from file')

    return graph


def validate_names(name_list):

    for name in name_list:

        if '' == name:

            # We could keep track and print the line for easy tracing
            raise ValidationException('found an empty name')

        if not re.fullmatch(r'^[0-9a-z\ \- ]{1,20}$', name):

            raise ValidationException(f'found a non-alphanumeric name: {name}')
