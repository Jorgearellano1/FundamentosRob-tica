from setuptools import setup
import glob

package_name = 'my_robot'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/urdf', ['urdf/robot_dh.urdf']),
        ('share/' + package_name + '/meshes',
         [*glob.glob('my_robot/meshes/*.stl'), *glob.glob('my_robot/meshes/*.STL')]),
        ('share/' + package_name + '/launch', ['launch/display.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='you',
    maintainer_email='you@example.com',
    description='DH robot demo',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'joint_state_publisher = my_robot.joint_state_publisher:main',
        ],
    },
)
