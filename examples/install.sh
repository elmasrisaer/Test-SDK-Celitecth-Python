python -m venv .venv
. .venv/bin/activate
pip install build
python -m build --outdir dist ../
pip install dist/saer-1.0.5-py3-none-any.whl --force-reinstall
