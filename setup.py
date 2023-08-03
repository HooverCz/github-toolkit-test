from setuptools import setup

setup(
    name='github_toolkit',
    version='0.0.1',
    packages=[
        'github_toolkit',
    ],
    license='',
    author='Simon Dalecky',
    description='package to update organisational secret with Github app private key',
    python_requires='>=3.6',
    install_requires=['requests==2.25.1', 'octokitpy==0.15.0', 'pynacl==1.5.0']
)