python -m venv .venv
. .venv/bin/activate
pip install build
python -m build --outdir dist ../
pip install dist/ups_locator_client-1.0.0-py3-none-any.whl --force-reinstall
