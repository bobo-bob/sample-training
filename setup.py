from setuptools import find_packages, setup

setup(
    name="foobar",
    use_scm_version={"version_scheme": "python-simplified-semver"},
    setup_requires=[
        "setuptools_scm",
    ],
    install_requires=[
        "hydra-colorlog",
        "hydra-core",
    ],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "foo-train=foobar.__main__:main",
        ],
    },
)
