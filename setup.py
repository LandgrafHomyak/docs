import sys
from distutils.core import setup

args = dict(
    name="lh_docs",

    packages=["lh_docs"],
    # entry_points={"console_scripts": {
    #     "lh_docs": "lh_docs:main"
    # }}
    package_data={"lh_docs": []}
)

if sys.version_info >= (3, 5):
    args["package_data"]["lh_docs"].extend(["py.typed"])

setup(
    **args
)
