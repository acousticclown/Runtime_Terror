from setuptools import setup
import os

DIRECTORY = os.path.dirname(__file__)

REQUIREMENTS = open(os.path.join(DIRECTORY, "REQUIREMENTS.txt")).read().split()
EXTRAS = {
    "async": ["aiohttp"],
    "fast_async": ["aiohttp", "cchardet", "aiodns"]
}
VERSION = open(os.path.join(DIRECTORY, "wizard", "VERSION.txt")).read()
READ_ME = open(os.path.join(DIRECTORY, "README.rst")).read()

setup(
    name="wizard.py",
    version=VERSION,
    author="skt2020",
    author_email="innuganti.ashwin@gmail.com",
    packages=["wizard", "wizard.async_wiz"],
    package_data={
        "wizard": ["VERSION.txt"]
    },
    url="https://github.com/skt2020/wizard.py",
    project_urls={
        "Documentation": "https://github.com/skt2020/wizard.py/blob/master/README.rst",
        "Source": "https://github.com/skt2020/wizard.py",
        "Tracker": "https://github.com/skt2020/wizard.py/issues",
        "Say Thanks!": "https://saythanks.io/to/skt2020"
    },
    license="MIT",
    description="An API wrapper for the online game, wizard, written in Python",
    long_description=READ_ME,
    long_description_content_type="text/x-rst",
    keywords="wizard api",
    install_requires=REQUIREMENTS,
    extras_require=EXTRAS,
    python_requires=">=3.5.3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Topic :: Utilities"
    ]
)
