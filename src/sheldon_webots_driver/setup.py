from setuptools import setup

package_name = 'sheldon_webots_driver'

data_files = []
""" Main data files"""
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name, ['package.xml']))

""" Custom data files"""
data_files.append(('share/' + package_name, ['launch/robot_launch.py']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/sheldon_example.wbt', ]))
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
    description='Webots driver for Sheldon',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sheldon_driver = sheldon_webots_driver.sheldon_driver:main',
            'sheldon_teleop = sheldon_webots_driver.teleop_twist_keyboard:main'
        ],
        'launch.frontend.launch_extension': ['launch_ros = launch_ros']
    },
)
