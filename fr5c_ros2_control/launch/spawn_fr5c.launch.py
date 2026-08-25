#!/usr/bin/env python3
"""fr5c ros2_control — Gazebo simulation with ros2_control"""
import os, tempfile
from ament_index_python.packages import get_package_share_directory as pkg_dir
from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node

def generate_launch_description():
    share = pkg_dir("fr5c_ros2_control")

    with open(os.path.join(share, "urdf", "fr5c.urdf")) as f:
        desc = f.read()
    desc = desc.replace("package://fr5c_ros2_control/", share + "/")

    cleanup = ExecuteProcess(
        cmd=['bash','-c','pkill -9 gzserver 2>/dev/null; pkill -9 gzclient 2>/dev/null; sleep 1; ros2 daemon stop 2>/dev/null; sleep 1'],
        output='screen', additional_env={'GAZEBO_PLUGIN_PATH':'/opt/ros/humble/lib'})

    gz_server = ExecuteProcess(
        cmd=['gzserver','empty.world','-s','libgazebo_ros_factory.so','-s','libgazebo_ros_init.so'],
        output='screen', additional_env={'GAZEBO_PLUGIN_PATH':'/opt/ros/humble/lib'})
    gz_client = ExecuteProcess(cmd=['gzclient'], output='screen', additional_env={'GAZEBO_PLUGIN_PATH':'/opt/ros/humble/lib'})

    rsp = Node(package='robot_state_publisher', executable='robot_state_publisher',
               output='screen',
               parameters=[{'robot_description': desc, 'publish_frequency': 100.0}])

    tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.urdf', delete=False, prefix='fr5c_')
    tmp.write(desc); tmp.close()
    spawn = Node(package='gazebo_ros', executable='spawn_entity.py',
                 arguments=['-file', tmp.name, '-entity', 'fr5c'], output='screen', additional_env={'GAZEBO_PLUGIN_PATH':'/opt/ros/humble/lib'})

    # Wait for controller_manager to become available, then load both controllers
    load_controllers = ExecuteProcess(
        cmd=['bash','-c',
             'echo "Waiting for controller_manager..." ; '
             'for i in $(seq 1 120); do '
             '  if ros2 service list 2>/dev/null | grep -q "/controller_manager/load_controller"; then '
             '    echo "controller_manager ready after ${i}s" ; '
             '    sleep 3 ; '
             '    ros2 control load_controller --set-state active joint_state_broadcaster ; '
             '    ros2 control load_controller --set-state active joint_trajectory_controller ; '
             '    exit 0 ; '
             '  fi ; '
             '  sleep 1 ; '
             'done ; '
             'echo "TIMEOUT: controller_manager not ready after 120s" ; exit 1'],
        output='screen')

    return LaunchDescription([
        cleanup,
        TimerAction(period=2.0, actions=[gz_server, gz_client]),
        TimerAction(period=3.0, actions=[rsp]),
        TimerAction(period=8.0, actions=[spawn]),
        load_controllers,
    ])
