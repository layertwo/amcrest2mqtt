from setuptools import find_packages, setup


def get_version():
    with open("VERSION") as fp:
        return fp.read().strip()


setup(
    name="amcrest2mqtt",
    version=get_version(),
    description="Expose all events from an Amcrest device to an MQTT broker",
    author="Daniel Chesterton",
    author_email="daniel@chestertondevelopment.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    scripts=["bin/amcrest2mqtt"],
    install_requires=[
        "amcrest==1.9.7",
        "paho-mqtt==1.6.1",
        "python-slugify==7.0.0",
        "urllib3==1.26.17",
        "requests==2.28.1",
    ],
)
