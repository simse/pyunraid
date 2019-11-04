#/bin/bash
pip install -U sphinx
pip install -e .
make -C docs html
cp -r docs/_build/html web/assets/docs
npm install
brunch build --production
