#!/usr/bin/env python

import jinja2
import json
import os


def load_parameters(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
        return json.loads(data)


def digest_folder(input_folder, output_folder, parameters):
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        if not os.path.isfile(file_path):
            break
        with open(file_path, 'r') as fin:
            template = jinja2.Template(fin.read())
            html = template.render(parameters)
            with open(os.path.join(output_folder, file_name), 'w') as fout:
                fout.write(html)


def main():
    try:
        os.mkdir('output')
    except OSError:
        pass
    parameters = load_parameters('parameters.json')
    digest_folder('input', 'output', parameters)


if __name__ == '__main__':
    main()
