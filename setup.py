from setuptools import find_packages, setup

setup(name='czds_api_client',
      version='0.1.0',
      description='Python client for the CZDS API',
      packages=find_packages("src"),
      package_dir={"": "src"},
      provides=["czds_api_client"],
)