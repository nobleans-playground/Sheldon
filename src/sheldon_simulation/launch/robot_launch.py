#!/usr/bin/env python

"""Launch robot in simulation"""

import os
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.substitutions.path_join_substitution import PathJoinSubstitution
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    package_dir = get_package_share_directory('sheldon_simulation')
    world = LaunchConfiguration('world')

    webots = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('webots_ros2_core'), 'launch', 'robot_launch.py')
        ),
        launch_arguments=[
            ('package', 'sheldon_simulation'),
            ('executable', 'sheldon_driver'),
            ('world', PathJoinSubstitution([package_dir, 'worlds', world])),
        ]
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value='example_world.wbt',
            description='Choose one of the world files from `/sheldon_simulation/world` directory'
        ),
        webots
    ])
