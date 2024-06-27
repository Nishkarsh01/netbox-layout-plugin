from setuptools import find_packages, setup

setup(
    name='netbox-layout-patch',
    version='0.1',
    description='A plugin to add layout cards on location pages with clickable links to racks.',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

