python -m venv .venv
call .venv\Scripts\activate
pip install build
python -m build --outdir dist ..\
pip install dist\saer-1.0.4-py3-none-any.whl --force-reinstall
deactivate
