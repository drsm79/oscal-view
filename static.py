import shutil
import json
from collections import defaultdict
from server import populate_schemas, schemas, inject_schema

populate_schemas()

def render_schemas():
    with open('jsonschemaviewer/index.html') as f:
        template_string = f.read()

    for s in schemas:
        with open(f'build/{s}.html', 'w') as f:
            f.write(inject_schema([s], template_string))

def copy_statics():
    shutil.copytree('jsonschemaviewer/css', 'build/css')
    shutil.copytree('jsonschemaviewer/js', 'build/js')

def extract_definitions():
    definitions = defaultdict(dict)
    string = ''
    for s in schemas:
        string += f'## {s}\n\n'
        data = json.loads(schemas[s].strip())
        string += f'> {data["$comment"]}\n\n'

        for k, v in data['definitions'].items():
            if k in definitions[s].keys():
                print(f'{k} already found')
                print('title matches:', v['title'] == definitions[s][k]['title'])
                print('description matches:', v['description'] == definitions[s][k]['description'])
            string += f"- **{v['title']}**: {v['description']}\n"
            definitions[s][k] = {
                'title': v['title'],
                'description': v['description']
            }
        string += f'\n'

    with open(f'build/terms.md', 'w') as f:
        f.write(string)

    string = ''
    found_in = defaultdict(list)
    for schema, terms in definitions.items():
        for t in terms:
            found_in[t].append(schema)

    for term, schema_list in found_in.items():
        hold = ''
        same = True
        for s in schema_list:
            if hold and hold != definitions[s][term]:
                same = False
                print(f'definition for {term} is different for {s}')
            else:
                hold = definitions[s][term]
        string += f"- **{definitions[s][term]['title']}** (`{term}`) is found in {schema_list_links(schema_list)}\n"
        if not same:
            string += f"  - definition for **{definitions[s][term]['title']}** is different between these schemas\n"
            for s in schema_list:
                string += f"    - {s}: {definitions[s][term]['description']}\n"
        else:
            string += f"  - definition: {definitions[s][term]['description']}\n"


    with open(f'build/glossary.md', 'w') as f:
        f.write(string)


def schema_list_links(schema_list):
    s = ''
    for i, item in enumerate(schema_list, 1):
        if i == len(schema_list) and i > 1:
            s = s.strip(', ')
            s += ' & '
        s += f'[{item}]({item}.html), '

    return s.strip(', ')

if __name__ == "__main__":
    shutil.rmtree('build')
    copy_statics()
    render_schemas()
    extract_definitions()