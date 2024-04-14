from setuptools import setup, find_packages

setup(
    name='snake_game',
    version='0.1',
    author='smitwaman',
    author_email='smitwaman007@gmail.com',
    description='A classic snake game written in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/smitwaman/snake-game-python',
    packages=find_packages(),
    install_requires=[
        # Add your requirements here
        'pygame>=2.0.1',
    ],
    entry_points={
        'console_scripts': [
            'snake_game=snake-game-python.main:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
    ],
)
