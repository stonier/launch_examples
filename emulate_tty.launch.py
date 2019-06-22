#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import launch
import launch_ros.actions


def generate_launch_description():
    """Main."""
    ld = launch.LaunchDescription()
    ld.add_action(launch.actions.SetLaunchConfiguration('emulate_tty', 'false'))
    ld.add_action(
        launch_ros.actions.Node(
            package='demo_nodes_py', node_executable='talker', output='screen',
            remappings=[('chatter', 'my_chatter')])
    )
    return ld
