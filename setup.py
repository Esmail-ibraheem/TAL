from setuptools import setup, find_packages

setup(
    name='transformer_lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'torch>=1.6.0',
    ],
    python_requires='>=3.6',
)