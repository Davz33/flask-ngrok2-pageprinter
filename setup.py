import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask-ngrok2-pageprinter",
    version="0.2.6",
    author="Davide Vitiello",
    description="A successor to to the successor to flask-ngrok for demo Flask apps using ngrok with ngrok tunnel info at disposal at runtime.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Davz33/flask-ngrok2-pageprinter",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    keywords='flask ngrok2 pageprinter demo',
    install_requires=['Flask>=0.8', 'requests'],
    py_modules=['flask_ngrok2_pp']
)
