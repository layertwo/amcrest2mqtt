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
        "python-slugify==8.0.4",
        "urllib3==2.0.7",
        "requests==2.31.0",
    ],
)
