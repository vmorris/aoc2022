import setuptools

dependencies = ["wheel", "Jinja2", "Click"]
tests_dependencies = ["pytest", "pytest_cov"]
extras = {"test": tests_dependencies}

setuptools.setup(
    name="aoc2022",
    version="0.0.1",
    description="Advent of Code 2022 Solutions",
    author="Vance Morris",
    author_email="vmorris@us.ibm.com",
    packages=setuptools.find_packages(),
    install_requires=dependencies,
    tests_require=tests_dependencies,
    extras_require=extras,
    entry_points={
        "console_scripts": ["newday = newday.newday:newday"],
    },
)
