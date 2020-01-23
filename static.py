import shutil
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

if __name__ == "__main__":
    shutil.rmtree('build')
    copy_statics()
    render_schemas()