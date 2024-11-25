from setuptools import setup, find_packages

setup(
    name="my_streamlit_app",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A sample Streamlit application.",
    packages=find_packages(),
    install_requires=[
        "streamlit",
    ],
    entry_points={
        "console_scripts": [
            "run-app=plot_app.app:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
