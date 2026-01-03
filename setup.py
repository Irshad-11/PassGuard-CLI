from setuptools import setup, find_packages

setup(
    name="passguard",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'colorama',
        'pyperclip',
    ],
    entry_points={
        'console_scripts': [
            'passguard=passguard.app:main',
        ],
    },
)