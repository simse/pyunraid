#/bin/bash
pip install -U sphinx
pip install -e .
make -C docs html
cp -r docs/_build web/docs
