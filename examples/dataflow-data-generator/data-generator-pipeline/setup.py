import os
import setuptools
setuptools.setup(
    name = "gcs-data-generator",
    version = "0.0.1",
    author = "Jacob Ferriero",
    author_email = "jferriero@google.com",
    install_requires=[
        'apache-beam[gcp]>=2.8.0',
        'Faker>=0.8.13',
        'faker-schema>=0.1.4',
        'google-cloud>=0.32',
        'google-cloud-bigquery>=1.1.0',
        'google-cloud-dataflow>=2.4.0',
        'google-cloud-datastore>=1.7.0',
        'google-cloud-pubsub>=0.30.1',
        'google-cloud-storage>=1.6.0',
        'google-cloud-vision>=0.31.0',
        'mock>=2.0.0',
        'numpy>=1.14.2',
        'pandas>=0.23.4',
        'six>=1.10.0',
        'scipy>=1.1.0'
    ],
    packages=['data_generator']
    )
