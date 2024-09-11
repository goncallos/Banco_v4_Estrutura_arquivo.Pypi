from setuptools import setup, find_packages

setup(
    name='my_frontend_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
    ],
    entry_points={
        'console_scripts': [
            'run-app = app:app.run'
        ]
    }
)
