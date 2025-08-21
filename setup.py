from setuptools import setup

setup(
    name="Spaced Repetition App",
    version="1.0",
    py_modules=["cli_script"],
    entry_points={
        "console_scripts": [
            "sr=cli_script:main"
        ]
    }
)