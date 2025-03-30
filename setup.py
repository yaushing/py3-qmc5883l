import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py3_qmc5883l",
    version="0.1.1",
    author="Kam Yau Shing",
    author_email="kam.yaushing@gmail.com",
    description="Python 3 driver for the QMC5883L 3-axis magnetic sensor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yaushing/py3-qmc5883l",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
)
