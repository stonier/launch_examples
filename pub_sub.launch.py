#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from launch import LaunchDescription
from launch import LaunchIntrospector
from launch import LaunchService

from launch_ros import get_default_launch_description
import launch_ros.actions


def generate_launch_description():
    """Main."""
    ld = LaunchDescription([
        launch_ros.actions.Node(
            package='demo_nodes_cpp', node_executable='talker', output='screen',
            remappings=[('chatter', 'my_chatter')]),
        launch_ros.actions.Node(
            package='demo_nodes_cpp', node_executable='listener', output='screen',
            remappings=[('chatter', 'my_chatter')]),
    ])

    print('Starting introspection of launch description...')
    print('')

    print(LaunchIntrospector().format_launch_description(ld))

    print('')
    print('Starting launch of launch description...')
    print('')
    return ld


if __name__ == '__main__':
    # ls = LaunchService(debug=True)
    ls = LaunchService()
    ls.include_launch_description(get_default_launch_description())
    ls.include_launch_description(generate_launch_description())
    ls.run()
