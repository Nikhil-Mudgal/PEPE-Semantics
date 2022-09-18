from setuptools import setup, find_namespace_packages

setup(name='pepe-semantics',
      version='0.0.2',
      package_dir={'': 'src'},
      packages=find_namespace_packages(where='src')
     )
