import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="multitaper_toolbox",
    version="26_JUL_2023",
    author="Thomas Possidente",
    author_email="tpossidente@bwh.harvard.edu",
    description="implementations of the multitaper spectrogram analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paul-wispr/multitaper_toolbox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
    ],
    install_requires=[
        'numba', 'pandas',
        'numpy', 'scipy', 'toml'
    ],
)
