import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="hiddenvortices",
    py_modules=[
        "dnnlib",
        "dnnlib.tflib",
        "ffhq_dataset",
        "metrics",
        "training",
        "utils",
        "generate",
        "aydao_flesh_digressions",
        "blend_models",
        "calc_metrics",
        "dataset_tool",
        "grid_vid",
        "projector",
        "style_mixing",
        "train",
    ],
    version="1.0",
    description="",
    author="Luke Nickel & Justin Focus",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    include_package_data=True,
    extras_require={"dev": ["pytest"]},
)
