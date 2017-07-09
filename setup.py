from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

    setup(
        name='weather',
        version='0.1',
        py_modules=['weather', 'settings'],
        install_requires=requirements,
        packages=find_packages(),
        entry_points='''
            [console_scripts]
            weather=weather.weather:cli
        ''',
    )
