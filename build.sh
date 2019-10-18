#/bin/bash
pip install sphinx
pip install -e .
make -C docs html
cp -r docs/_build web/docs
