from setuptools import find_packages, setup

setup(
    name="tbd_dagster",
    version="0.1.0",
    description="TBD Dagster Project",
    author="Josh Hanson",
    author_email="hanson377@gmail.com",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "dagster>=1.5.0",
        "dagster-cloud>=1.5.0",
        "dagster-postgres>=0.21.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
    ],
)