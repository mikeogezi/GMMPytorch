# setup.py for GMMPytorch
# This file defines how to build and install the GMMPytorch package.

from setuptools import setup, find_packages

# Read dependencies from requirements.txt
def read_requirements(path='requirements.txt'):
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='GMMPytorch',  # Replace if you rename the package
    version='0.1.0',  # Initial version of your fork
    description='Gradient-based Gaussian Mixture Models for PyTorch',
    author='Michael Ogezi',  # TODO: update with your name
    author_email='mikeogezi@users.noreply.github.com',  # TODO: update with your email
    url='https://github.com/mikeogezi/GMMPytorch',  # TODO: update with your repo URL
    packages=find_packages(),  # Automatically include all packages under src/
    install_requires=read_requirements(),  # Dependencies listed in requirements.txt
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',  # Specify minimum Python version
)
