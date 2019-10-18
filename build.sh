#/bin/bash
pip install sphinx
make -C docs html
cp -r docs/_build web/docs
