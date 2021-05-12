"""ROS2 sheldon driver."""

import rclpy
from webots_ros2_core.webots_differential_drive_node import WebotsDifferentialDriveNode

class SheldonDriver(WebotsDifferentialDriveNode):
    def __init__(self, args):
        super().__init__(
            'sheldon_driver',
            args,
            left_encoder='left wheel sensor',
            left_joint='left wheel motor',
            right_encoder='right wheel sensor',
            right_joint='right wheel motor',
            robot_base_frame='base_link',
            wheel_distance=0.160,
            wheel_radius=0.033
        )
        self.start_device_manager({
            'robot': {'publish_base_footprint': True},
            'LDS-01': {'topic_name': '/scan'},
            'inertial_unit+accelerometer+gyro': {'frame_id': 'imu_link', 'topic_name': '/imu'}
        })


def main(args=None):
    rclpy.init(args=args)
    driver = SheldonDriver(args=args)
    rclpy.spin(driver)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
