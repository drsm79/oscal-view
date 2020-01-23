# oscal-view


You'll need python 3 (developed with Python 3.7.5), verify with `python --version`

- clone repo: `git  clone git@github.ibm.com:simonmetson/oscal-view.git`
- `cd oscal-view`
- pull in submodules: `git submodule update --init`
- launch (will open a tab in a browser):

``` console
python server.py
```

- select the OSCAL schema you want to view:
  - http://localhost:8000/catalog
  - http://localhost:8000/profile
  - http://localhost:8000/component
  - http://localhost:8000/ssp

- TODO: write the c3.json schema