============================================================

&#x20;FR Series Robot Gazebo Simulation Usage Guide

============================================================



All 11 robot packages (fr3v6, fr3c, fr3wml, fr3wms, fr5v6, fr5c, fr5l,

fr10v6, fr16v6, fr20v6, fr30v6) use the ros2\_control mode (GazeboSystem).





1\. fr3v6\_ros2\_control — ros2\_control (GazeboSystem)

============================================================



Features: standard ros2\_control architecture, joint\_trajectory\_controller, supports trajectory control



Launch:

&#x20; source /opt/ros/humble/setup.bash

&#x20; source \~/ros2\_control\_ws/install/setup.bash

&#x20; source \~/FR\_Gazebo\_ws/install/setup.bash

&#x20; ros2 launch fr3v6\_ros2\_control spawn\_fr3v6.launch.py



Control (JointTrajectory):

&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[1.57, -0.78, -1.57, -1.2, 1.57, 1.3],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



Monitor:

&#x20; ros2 topic echo /joint\_states



Demo:

&#x20; python3 \~/FR\_Gazebo\_ws/src/fr3v6\_ros2\_control/scripts/fr3v6\_demo.py





2\. fr3c\_ros2\_control — ros2\_control (GazeboSystem)

============================================================



Features: standard ros2\_control architecture, joint\_trajectory\_controller, supports trajectory control



Launch:

&#x20; source /opt/ros/humble/setup.bash

&#x20; source \~/ros2\_control\_ws/install/setup.bash

&#x20; source \~/FR\_Gazebo\_ws/install/setup.bash

&#x20; ros2 launch fr3c\_ros2\_control spawn\_fr3c.launch.py



Control (JointTrajectory):

&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[1.57, -0.78, -1.57, -1.2, 1.57, 1.3],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



Monitor:

&#x20; ros2 topic echo /joint\_states



Demo:

&#x20; python3 \~/FR\_Gazebo\_ws/src/fr3c\_ros2\_control/scripts/fr3c\_demo.py





3\. fr3wml\_ros2\_control — ros2\_control (GazeboSystem)

============================================================



Features: standard ros2\_control architecture, joint\_trajectory\_controller, supports trajectory control



Launch:

&#x20; source /opt/ros/humble/setup.bash

&#x20; source \~/ros2\_control\_ws/install/setup.bash

&#x20; source \~/FR\_Gazebo\_ws/install/setup.bash

&#x20; ros2 launch fr3wml\_ros2\_control spawn\_FR3WML.launch.py



Control (JointTrajectory):

&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[1.57, -0.78, -1.57, -1.2, 1.57, 1.3],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



Monitor:

&#x20; ros2 topic echo /joint\_states



Demo:

&#x20; python3 \~/FR\_Gazebo\_ws/src/fr3wml\_ros2\_control/scripts/fr3wml\_demo.py





4\. fr3wms\_ros2\_control — ros2\_control (GazeboSystem)

============================================================



Features: standard ros2\_control architecture, joint\_trajectory\_controller, supports trajectory control



Launch:

&#x20; source /opt/ros/humble/setup.bash

&#x20; source \~/ros2\_control\_ws/install/setup.bash

&#x20; source \~/FR\_Gazebo\_ws/install/setup.bash

&#x20; ros2 launch fr3wms\_ros2\_control spawn\_FR3WMS.launch.py



Control (JointTrajectory):

&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[1.57, -0.78, -1.57, -1.2, 1.57, 1.3],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



Monitor:

&#x20; ros2 topic echo /joint\_states



Demo:

&#x20; python3 \~/FR\_Gazebo\_ws/src/fr3wms\_ros2\_control/scripts/fr3wms\_demo.py





5\. fr5v6\_ros2\_control — ros2\_control (GazeboSystem)

============================================================



Features: standard ros2\_control architecture, joint\_trajectory\_controller, supports trajectory control



Launch:

&#x20; source /opt/ros/humble/setup.bash

&#x20; source \~/ros2\_control\_ws/install/setup.bash

&#x20; source \~/FR\_Gazebo\_ws/install/setup.bash

&#x20; ros2 launch fr5v6\_ros2\_control spawn\_fr5v6.launch.py



Control (JointTrajectory):

&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[1.57, -0.78, -1.57, -1.2, 1.57, 1.3],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



Monitor:

&#x20; ros2 topic echo /joint\_states



Demo:

&#x20; python3 \~/FR\_Gazebo\_ws/src/fr5v6\_ros2\_control/scripts/fr5v6\_demo.py





6\. fr5c\_ros2\_control — ros2\_control (GazeboSystem)

============================================================



Features: standard ros2\_control architecture, joint\_trajectory\_controller, supports trajectory control



Launch:

&#x20; source /opt/ros/humble/setup.bash

&#x20; source \~/ros2\_control\_ws/install/setup.bash

&#x20; source \~/FR\_Gazebo\_ws/install/setup.bash

&#x20; ros2 launch fr5c\_ros2\_control spawn\_fr5c.launch.py



Control (JointTrajectory):

&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[1.57, -0.78, -1.57, -1.2, 1.57, 1.3],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



Monitor:

&#x20; ros2 topic echo /joint\_states



Demo:

&#x20; python3 \~/FR\_Gazebo\_ws/src/fr5c\_ros2\_control/scripts/fr5c\_demo.py





7\. fr5l\_ros2\_control — ros2\_control (GazeboSystem)

============================================================



Features: standard ros2\_control architecture, joint\_trajectory\_controller, supports trajectory control



Launch:

&#x20; source /opt/ros/humble/setup.bash

&#x20; source \~/ros2\_control\_ws/install/setup.bash

&#x20; source \~/FR\_Gazebo\_ws/install/setup.bash

&#x20; ros2 launch fr5l\_ros2\_control spawn\_fr5l.launch.py



Control (JointTrajectory):

&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[1.57, -0.78, -1.57, -1.2, 1.57, 1.3],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



Monitor:

&#x20; ros2 topic echo /joint\_states



Demo:

&#x20; python3 \~/FR\_Gazebo\_ws/src/fr5l\_ros2\_control/scripts/fr5l\_demo.py





8\. fr10v6\_ros2\_control — ros2\_control (GazeboSystem)

============================================================



Features: standard ros2\_control architecture, joint\_trajectory\_controller, supports trajectory control



Launch:

&#x20; source /opt/ros/humble/setup.bash

&#x20; source \~/ros2\_control\_ws/install/setup.bash

&#x20; source \~/FR\_Gazebo\_ws/install/setup.bash

&#x20; ros2 launch fr10v6\_ros2\_control spawn\_fr10v6.launch.py



Control (JointTrajectory):

&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[1.57, -0.78, -1.57, -1.2, 1.57, 1.3],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



Monitor:

&#x20; ros2 topic echo /joint\_states



Demo:

&#x20; python3 \~/FR\_Gazebo\_ws/src/fr10v6\_ros2\_control/scripts/fr10v6\_demo.py





9\. fr16v6\_ros2\_control — ros2\_control (GazeboSystem)

============================================================



Features: standard ros2\_control architecture, joint\_trajectory\_controller, supports trajectory control



Launch:

&#x20; source /opt/ros/humble/setup.bash

&#x20; source \~/ros2\_control\_ws/install/setup.bash

&#x20; source \~/FR\_Gazebo\_ws/install/setup.bash

&#x20; ros2 launch fr16v6\_ros2\_control spawn\_fr16v6.launch.py



Control (JointTrajectory):

&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[1.57, -0.78, -1.57, -1.2, 1.57, 1.3],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



Monitor:

&#x20; ros2 topic echo /joint\_states



Demo:

&#x20; python3 \~/FR\_Gazebo\_ws/src/fr16v6\_ros2\_control/scripts/fr16v6\_demo.py





10\. fr20v6\_ros2\_control — ros2\_control (GazeboSystem)

============================================================



Features: standard ros2\_control architecture, joint\_trajectory\_controller, supports trajectory control



Launch:

&#x20; source /opt/ros/humble/setup.bash

&#x20; source \~/ros2\_control\_ws/install/setup.bash

&#x20; source \~/FR\_Gazebo\_ws/install/setup.bash

&#x20; ros2 launch fr20v6\_ros2\_control spawn\_fr20v6.launch.py



Control (JointTrajectory):

&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[1.57, -0.78, -1.57, -1.2, 1.57, 1.3],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



Monitor:

&#x20; ros2 topic echo /joint\_states



Demo:

&#x20; python3 \~/FR\_Gazebo\_ws/src/fr20v6\_ros2\_control/scripts/fr20v6\_demo.py





11\. fr30v6\_ros2\_control — ros2\_control (GazeboSystem)

============================================================



Features: standard ros2\_control architecture, joint\_trajectory\_controller, supports trajectory control



Launch:

&#x20; source /opt/ros/humble/setup.bash

&#x20; source \~/ros2\_control\_ws/install/setup.bash

&#x20; source \~/FR\_Gazebo\_ws/install/setup.bash

&#x20; ros2 launch fr30v6\_ros2\_control spawn\_fr30v6.launch.py



Control (JointTrajectory):

&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[1.57, -0.78, -1.57, -1.2, 1.57, 1.3],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



&#x20; ros2 topic pub --once /joint\_trajectory\_controller/joint\_trajectory \\

&#x20;   trajectory\_msgs/msg/JointTrajectory \\

&#x20;   "{joint\_names: \[j1,j2,j3,j4,j5,j6],

&#x20;     points: \[{positions: \[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],

&#x20;               time\_from\_start: {sec: 2, nanosec: 0}}]}"



Monitor:

&#x20; ros2 topic echo /joint\_states



Demo:

&#x20; python3 \~/FR\_Gazebo\_ws/src/fr30v6\_ros2\_control/scripts/fr30v6\_demo.py





12\. Angle Conversion

============================================================

&#x20; radian = degree \* pi / 180

&#x20; 90° = 1.5708 rad

&#x20; -90° = -1.5708 rad

&#x20; 100° = 1.7453 rad





13\. Notes

============================================================

1\. Before launching, it is recommended to close the old Gazebo first:

&#x20;  pkill -9 gzserver; pkill -9 gzclient



2\. ros2\_control packages must source ros2\_control\_ws

&#x20;  (in \~/ros2\_control\_ws/install)



3\. Two packages cannot run at the same time



4\. Launch wait: it takes about 30 seconds from launch to controller ready

&#x20;  - mainly the gazebo\_ros2\_control plugin loading mesh files and waiting for

&#x20;    robot\_state\_publisher service discovery

&#x20;  - the launch automatically polls and waits for controller\_manager to be ready

&#x20;    before loading the controller

&#x20;  - "Successfully loaded controller joint\_trajectory\_controller into state active"

&#x20;    means ready



5\. The demo script automatically waits for controller\_manager to be ready before moving

&#x20;  - if the demo is stuck at "Waiting for controller\_manager..." for more than 2 minutes,

&#x20;    press Ctrl+C to exit and retry



6\. When using ros2 topic pub for manual control, note:

&#x20;  - must wait for the controller to finish loading before publishing

&#x20;  - use a timestamp later than the current time



