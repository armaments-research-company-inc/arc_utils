import setuptools
from setuptools import find_packages
setuptools.setup(
    name="arc_utils",
    version="0.3.1",
    url='https://github.com/armaments-research-company-inc/arc_utils',
    author="Minhaj Uddin Khan",
    author_email="minhajuddin.khan@tenpearls.com",
    description="Utility methods for ARC",
    python_requires='>=3.6',
    # packages=['arc_utils'],
    packages = find_packages(), 
)
