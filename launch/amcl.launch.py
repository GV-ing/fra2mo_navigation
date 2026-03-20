import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    # percorso del pacchetto nav2_bringup
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    
    # Percorso della mappa
    map_path = os.path.join(
        get_package_share_directory('fra2mo_navigation'),
        'maps',
        'mappa2.yaml'
    )

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_bringup_dir, 'launch', 'localization_launch.py')
            ),
            launch_arguments={
                'use_sim_time': 'true',
                'map': map_path
            }.items()
        )
    ])