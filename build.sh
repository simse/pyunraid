#/bin/bash
pip3 install -U sphinx
pip3 install -e .
make -C docs html
cp -r docs/_build web/docs
