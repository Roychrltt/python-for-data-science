python3 -m pip install --upgrade pip setuptools wheel build
rm -rf build dist *.egg-info
python -m build
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
