from setuptools import setup, find_packages

setup(
    name="LintAid",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "lintaid=lintaid:main",
        ],
    },
    # Add other package details as needed
)

