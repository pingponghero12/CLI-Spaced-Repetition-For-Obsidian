from setuptools import setup, find_packages

setup(
    name="srcli",
    version="1.0",
    description="Simple CLI spaced repetition tool for Obsidian",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pingponghero12/CLI-Spaced-Repetition-For-Obsidian",
    author="Manfred Gawlas",
    author_email="manfredgawlas12@gmail.com",

    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "pandas",
        "tabulate",
        "numexpr>=2.8.4",
        "bottleneck>=1.3.6"
    ],
    entry_points={
        'console_scripts': [
            'srcli=srcli.sr:main',  # Assuming sr.py has a main() function
        ],
    },

    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
)
