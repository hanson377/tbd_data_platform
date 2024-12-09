from setuptools import find_packages, setup

setup(
    name="tbd_dagster",
    packages=find_packages(exclude=["tbd_dagster_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "ics",
        "arrow",
        "slack_sdk",
        "datetime",
        "os"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
