from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

setup(
    name="LintAid",
    version="1.0.0",
    description="CLI tool to help seamless integration of Linters",
    long_description=README,
    author="Pratham Gupta",
    author_email="pratham.gupta@nyu.edu",
    url="https://github.com/PrathamGupta/LintAid",
    entry_points={
        "console_scripts": [
            "lintaid=LintAid.lintaid:main",
        ],
    },
    # Add other package details as needed
)

