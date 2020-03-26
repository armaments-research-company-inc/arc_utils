import setuptools

setuptools.setup(
    name="arc_utils",
    version="0.2.11",
    url='https://github.com/armaments-research-company-inc/arc_utils',
    author="Minhaj Uddin Khan",
    author_email="minhajuddin.khan@tenpearls.com",
    description="Utility methods for ARC",
    python_requires='>=3.6',
    packages=['arc_utils'], 
    package_dir={'arc_utils': 'src/arc_utils'},  
)
