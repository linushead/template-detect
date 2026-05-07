from setuptools import setup, find_packages

setup(
    name='templatedetect',
    version='0.1',
    description='A library for detecting blobs and arcs in images using template matching',
    author_email='head.linus0@gmail.com',
    zip_safe=False,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    # python_requires=">=3.8",
)
