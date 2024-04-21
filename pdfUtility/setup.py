from setuptools import setup, find_packages

setup(
    name='pdfUtility',
    version='0.1.0',
    description='A Python library for uploading and downloading PDF files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ayush Jadhav',
    author_email='jadhavayush2020@email.com',
    url='https://github.com/your_username/pdftility',
    packages=find_packages(),
    license='MIT',
    install_requires=[
        'requests',
    ],
)
