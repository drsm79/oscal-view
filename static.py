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
    for s in sorted(schemas):
        data = json.loads(schemas[s].strip())
        definitions[s]["$comment"] = data["$comment"].replace(": JSON Schema", "")
        for k, v in sorted(data['definitions'].items()):
            if k in definitions[s].keys():
                print(f'{k} already found')
                print('title matches:', v['title'] == definitions[s][k]['title'])
                print('description matches:', v['description'] == definitions[s][k]['description'])

            definitions[s][k] = {
                'title': v['title'],
                'description': v['description'],
                'type': v['type']
            }

    found_in = defaultdict(list)
    for schema, terms in definitions.items():
        for t in terms:
            if t == '$comment':
                continue
            found_in[t].append(schema)

    return definitions, found_in


def build_terms(definitions):
    string = ''
    for s, terms in sorted(definitions.items()):
        string += f'## {s}\n\n'
        string += f'> {definitions[s]["$comment"]}\n\n'
        for k, v in sorted(terms.items()):
            if k == '$comment':
                continue
            string += f"- **{v['title']}**: {v['description']}\n"
        string += f'\n'

    with open(f'build/terms.md', 'w') as f:
        f.write(string)
        string += f'## {s}\n\n'


def build_objects(definitions, found_in):
    string = ''
    for term, schema_list in sorted(found_in.items()):
        hold = ''
        same = True
        for s in schema_list:
            if hold and hold != definitions[s][term]:
                same = False
                print(f'definition for {term} is different for {s}')
            else:
                hold = definitions[s][term]
        if definitions[s][term]['type'] != 'object':
            continue
        string += f"- **{definitions[s][term]['title']}**"
        string += f"(`{term}` `type:{definitions[s][term]['type']}`)"
        string += f" is found in {schema_list_links(schema_list)}\n"
        if not same:
            string += f"  - definition for **{definitions[s][term]['title']}** is different between these schemas\n"
            for s in schema_list:
                string += f"    - {s}: {definitions[s][term]['description']}\n"
        else:
            string += f"  - definition: {definitions[s][term]['description']}\n"

    with open(f'build/objects.md', 'w') as f:
        f.write(string)
        string += f'## {s}\n\n'


def build_glossary(definitions, found_in):
    string = ''

    for term, schema_list in sorted(found_in.items()):
        hold = ''
        same = True
        for s in schema_list:
            if hold and hold != definitions[s][term]:
                same = False
                print(f'definition for {term} is different for {s}')
            else:
                hold = definitions[s][term]
        string += f"- **{definitions[s][term]['title']}**"
        string += f"(`{term}` `type:{definitions[s][term]['type']}`)"
        string += f" is found in {schema_list_links(schema_list)}\n"
        if not same:
            string += f"  - definition for **{definitions[s][term]['title']}** is different between these schemas\n"
            for s in schema_list:
                string += f"    - {s}: {definitions[s][term]['description']}\n"
        else:
            string += f"  - definition: {definitions[s][term]['description']}\n"


    with open(f'build/glossary.md', 'w') as f:
        f.write(string)
    return found_in


def make_index(defintions):
    page = f'''- [catalog](catalog.html) - {definitions["catalog"]["$comment"]}
- [profile](profile.html) - {definitions["profile"]["$comment"]}
- [component](component.html) - {definitions["component"]["$comment"]}
- [ssp](ssp.html) - {definitions["ssp"]["$comment"]}

----

- [objects](terms.html)
- [glossary](glossary.html)
- [terms](terms.html)'''
    with open(f'build/index.md', 'w') as f:
        f.write(page)


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
    definitions, found_in = extract_definitions()
    build_terms(definitions)
    build_glossary(definitions, found_in)
    build_objects(definitions, found_in)
    make_index(definitions)