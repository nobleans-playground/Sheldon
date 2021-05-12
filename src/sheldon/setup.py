from setuptools import setup

package_name = 'sheldon'

data_files = []
""" Main data files"""
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name, ['package.xml']))

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mathijsio',
    maintainer_email='mathijs.schouten@nobleo.nl',
    description='The main package of the robot',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop = sheldon.teleop:main'
        ],
    },
)
