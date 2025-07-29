from setuptools import setup, find_packages

setup(
    name='thang_utils',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A collection of utility functions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/thang_utils',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)