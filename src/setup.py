import setuptools
import os

setuptools.setup(
    name="mymodule",
    version="0.1.0",
    #py_modules=['mymodule'],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(include=['src']),
    install_requires=[
      #  'z-quantum-core',
        'cmake',
        'gcc7',
        'qulacs'
    ]
)

