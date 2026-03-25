import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # percorso del pacchetto nav2_bringup
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    fra2mo_nav_dir = FindPackageShare('fra2mo_navigation')
    nav2_params_path = PathJoinSubstitution([fra2mo_nav_dir, 'config', 'nav2_params.yaml'])
    # Percorso della mappa
    map_path = PathJoinSubstitution([fra2mo_nav_dir, 'maps', 'mappa_leonardo.yaml'])


    navigation_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([nav2_bringup_dir, 'launch', 'navigation_launch.py'])
            ),
            launch_arguments={
                'use_sim_time': 'true',  # Obbligatorio a 'true' se stai usando Gazebo
                'params_file': nav2_params_path
            }.items()
        )
    

    amcl_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([nav2_bringup_dir, 'launch', 'localization_launch.py'])
            ),
            launch_arguments={
                'use_sim_time': 'true',
                'map': map_path,
                'params_file': nav2_params_path
            }.items()
        )
    return LaunchDescription([
        navigation_launch,
        amcl_launch
    ])