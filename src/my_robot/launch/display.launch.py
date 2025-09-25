from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    urdf = os.path.join(get_package_share_directory('my_robot'), 'urdf', 'robot_dh.urdf')
    with open(urdf, 'r') as f:
        robot_desc = f.read()
    return LaunchDescription([
        Node(package='robot_state_publisher', executable='robot_state_publisher',
             name='robot_state_publisher', parameters=[{'robot_description': robot_desc}]),
        Node(package='tf2_ros', executable='static_transform_publisher',
             arguments=['0','0','0','0','0','0','world','base_link']),
    ])
