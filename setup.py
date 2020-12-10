import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="num2azerbaijani",
    version="0.0.3",
    author="Yunis Huseynzade",
    author_email="yunisdev.04@gmail.com",
    description="Convert integers into Azerbaijani string",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YunisDEV/num2azerbaijani",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'
)