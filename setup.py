from setuptools import find_packages, setup

setup(
    name="dagster_project",
    packages=find_packages(exclude=["dagster_project_tests"]),
    install_requires=[
        "dagster==1.5.4",
        "dagster-dbt==0.21.4",
        "dbt-core==1.6.0",
        "dbt-snowflake==1.6.0",
    ],
    extras_require={
        "dev": [
            "dagster-webserver==1.5.4", 
            "pytest"
        ]
    },
)
