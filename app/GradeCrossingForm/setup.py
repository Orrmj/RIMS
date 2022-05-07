from setuptools import setup, find_packages

setup(
    name='Grade Crossing Form',
    version='1.0',
    author='Michael Orr',
    author_email='orr.michael4@gmail.com.com',
    description='Grade Crossing Assess Form',
    url="http://gradecrossingform.example.com",
    license='MIT',
    long_description=open('README.rst', 'r').read(),
    keywords='grade crossing form pyqt5',
    project_urls={
        'Author Website': 'https://www.example.com',
        'Publisher Website': 'https://example.com',
        'Source Code': 'https://git.example.com/gradecrossingform'
    },
    #packages=['qtictactoe', 'qtictactoe.images'],
    packages=find_packages(),
    install_requires=['PyQt5 >= 5.12'],
    python_requires='>=3.6',
    #extras_require={
    #    "NetworkPlay": ["requests"]
    #},
    #include_package_data=True,
    package_data={
        'qtictactoe.images': ['*.png'],
        '': ['*.txt', '*.rst']
    },
    entry_points={
        'console_scripts': [
            'gradecrossingform = gradecrossingform.__main__:main'
        ]
    }
)
