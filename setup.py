from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="convertify-py",
    entry_points={
        "console_scripts": [
            'convertify-py=convertify.__main__:main'
        ]
    },
    version="0.0.7",
    description="A small CLI tool to convert units.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ulises-codes/convertify",
    author="Ulises Himely",
    license="GNU",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    project_urls={
        "Bug Tracker": "https://github.com/ulises-codes/convertify/issues"
    },
    package_data={
        'convertify': ['resources/data.csv']
    }
)
