from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="todo",
    version="0.1.0",
    author="Jaisurya",
    author_email="pjaisurya.ml@gmail.com",
    url = "https://github.com/JaiSuryaPrabu/todo",
    description="A simple todo list manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "todo = todo.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
