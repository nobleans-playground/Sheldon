from setuptools import setup

package_name = 'sheldon_simulation'

data_files = []
""" Main data files"""
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name, ['package.xml']))

""" Custom data files"""
data_files.append(('share/' + package_name + '/launch', ['launch/robot_launch.py']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/example_world.wbt', ]))
data_files.append(('share/' + package_name + '/protos', ['protos/sheldon.proto']))

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mathijsio',
    maintainer_email='mathijs.schouten@nobleo.nl',
    description='The simulation package of the robot',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sheldon_driver = sheldon_simulation.sheldon_driver:main'
        ],
        'launch.frontend.launch_extension': ['launch_ros = launch_ros']
    },
)
