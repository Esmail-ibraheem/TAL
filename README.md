# transformer-architecture-library
I developed a Python library for transformers, leveraging the architecture I previously designed. With this library, users can freely install and utilize the transformer architecture.

---

1. Create a Directory Structure: Start by creating a directory structure for your package, For instance:
   - create a folder called transformer_package, then save this files in the folder.
    ```python
    my_transformer_package/
    ├── my_transformer/
    │   ├── __init__.py
    │   ├── transformer.py
    └── setup.py

    ```
2. the setup.py: This file is used to define metadata about your package and how to install it. Here's a minimal example, you can change it for example the version:
   ```python
   from setuptools import setup, find_packages

    setup(
        name='my_transformer',
        version='0.1',
        packages=find_packages(),
        install_requires=[
            'torch>=1.6.0',
        ],
        python_requires='>=3.6',
    )

   ```
3. After installing the repo, go to the terminal and type:
   ```
   pip install .
   ```
3. And then, run the test file.
   ### Now you should be able to use the transformer architecture in any python file you build.
