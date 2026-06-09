
# 📌 ROS2 Turtlesim Kinematics (Python & C++)

## 📖 Project Overview

This project demonstrates simple kinematics between two turtles in ROS2 turtlesim.  
It calculates the **relative position and orientation** between turtle1 and turtle2 using both Python and C++ implementations.

The node subscribes to:
- `/turtle1/pose`
- `/turtle2/pose`

and continuously computes:
- Translation vector (Tx, Ty)
- Rotation difference (theta)
- Rotation matrix between turtles

---

## 🧠 Core Idea

The program compares turtle2 with turtle1 and computes how far it is shifted and rotated relative to turtle1.

---

## 📍 Translation Vector

- Tx = x2 - x1  
- Ty = y2 - y1  

This gives the position difference between the two turtles.

---

## 🔄 Rotation Difference

- theta_diff = theta2 - theta1  
- theta_deg = (theta_diff × 180) / π  

This gives the orientation difference in radians and degrees.

---

## 🧮 Rotation Matrix

- R11 = cos(theta_diff)  
- R12 = -sin(theta_diff)  
- R21 = sin(theta_diff)  
- R22 = cos(theta_diff)  

This represents the relative orientation between the turtles.

---

## 🚀 How to Run (ALL COMMANDS)

```bash
# Terminal 1 – start turtlesim
ros2 run turtlesim turtlesim_node

# Terminal 2 – spawn second turtle (turtle2)
ros2 service call /spawn turtlesim/srv/Spawn "{x: 1.0, y: 4.0, theta: 0.0, name: 'turtle2'}"

# Terminal 3 – source workspace and run node
cd ~/robot_ws
. install/setup.bash

# run Python version
ros2 run robot_py simple_turtlesim_kinematics

# OR run C++ version
ros2 run robot_cpp simple_turtlesim_kinematics

# Terminal 4 – keyboard control
ros2 run turtlesim turtle_teleop_key
````



## 🧾 Output

The node prints:

* Translation vector (Tx, Ty)
* Rotation difference (rad, deg)
* Rotation matrix

---

## 🎯 Key Learning

* ROS2 publisher/subscriber system
* turtlesim Pose message handling
* Relative motion between two turtles
* 2D translation and rotation concepts
* Same logic implemented in Python and C++

```
```
