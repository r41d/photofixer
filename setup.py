import setuptools

with open("README", 'r') as f:
    long_description = f.read()

with open("requirements.txt", 'r') as f:
    dependencies = f.readlines()

setuptools.setup(
    name="photofixer",
    version="0.1.0",
    license="GPLv3",
    description='A useful module',
    long_description=long_description,
    author='Lennart Buhl',
    author_email='git@hackmate.de',
    url="https://github.com/r41d/photofixer",
    python_requires=">=3.10",
    packages=["photofixer"],  # TODO: Read requirements
    install_requires=dependencies,  # external packages as dependencies
    scripts=[
        'scripts/cool',
        'scripts/skype',
    ],
)
