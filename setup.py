# setup.py for GMMPytorch
# This file defines how to build and install the GMMPytorch package.

from setuptools import setup, find_packages

# Read dependencies from requirements.txt
def read_requirements(path='requirements.txt'):
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='GMMPytorch',         # Package name matching your root folder
    version='0.1.0',           # Version of your fork
    description='Gradient-based Gaussian Mixture Models for PyTorch',
    author='Michael Ogezi',
    author_email='michael@outlook.com',
    url='https://github.com/mikeogezi/GMMPytorch',
    packages=find_packages(),   # Auto-discovers GMMPytorch and submodules at repo root
    install_requires=read_requirements(),  # Dependencies listed in requirements.txt
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',    # Minimum Python version
)

