from setuptools import setup, find_packages

setup(
    name="relayService",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "asyncio"
    ],
    description="Package to send messages from a docker container to a discord bot",
    author="RealBeastman",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)