from setuptools import setup, find_packages

setup(
    name='lib_version',
    description='Version-aware utility library',
    author='remla25-team13',
    packages=find_packages(),
    python_requires='>=3.12',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
)