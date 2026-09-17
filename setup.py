from setuptools import setup, find_packages

setup(
    name="scamhunter",
    version="1.0.0",
    author="Kuldeep",
    description="OSINT Tool for Scammer Investigation by CEH Certified Kuldeep",
    url="https://github.com/kuldeepLinux/Scam-hunter-",
    packages=find_packages(),
    install_requires=["phonenumbers>=8.13.0", "colorama>=0.4.6"],
    entry_points={"console_scripts": ["scamhunter=main:main"]},
    python_requires=">=3.8",
    license="MIT",
)
