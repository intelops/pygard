from setuptools import setup, find_packages

setup(
    name="pygard",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "pydantic",
        "uvicorn",
        "requests",
        "pyyaml",
        "click",
        "gitpython"
    ],
    entry_points={
        'console_scripts': [
            'pygard=pygard.cli:cli',
        ],
    },
    author="Vishwas Prasanna",
    description="A validation and configuration management tool using Pydantic.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
