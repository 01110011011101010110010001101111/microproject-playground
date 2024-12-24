from setuptools import find_packages, setup

package_name = 'fizzbuzz'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='genericp3rson',
    maintainer_email='genericp3rson@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'number_publisher = fizzbuzz.number_publisher_node:main',
            'fizzbuzz_subscriber = fizzbuzz.fizzbuzz_subscriber_node:main'
        ],
    },
)
