from setuptools import find_packages, setup

requirements = [
    'numpy',
    'pandas',
    'scikit-learn',
    'jupyter',
]

setup(name='user-requirements-classification',
      version='1.0',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requirements,
      extras_require={'dev': ['autopep8']}
      )
