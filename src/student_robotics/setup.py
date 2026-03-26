from setuptools import setup
import os
from glob import glob

package_name = 'student_robotics'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Prakash Aryan',
    maintainer_email='prakash.aryan@students.unibe.ch',
    description='ROS 2 exercise: circle motion publisher and odometry monitor',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'circle_motion = student_robotics.circle_motion:main',
            'odom_monitor = student_robotics.odom_monitor:main',
        ],
    },
)
