import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mycolab",
    version="$VERSION",
    author="Joe Harrison",
    author_email="joseph@mycolab.org",
    description="Mycolab core lib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mycolab/mycolab",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'redis==4.0.2'
    ],
    include_package_data=True
)
