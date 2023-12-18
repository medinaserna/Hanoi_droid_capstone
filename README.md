# HANOI DROID CAPSTONE

Introducing the Hanoi Droid, a groundbreaking Capstone Project showcasing expertise with the life-size open-source robot, ['InMoov'](https://inmoov.fr/). Nestled within its enclosure are the microcontrollers, webcam, mini PC, and power supply, ensuring seamless functionality. Our robot is designed to master the Tower of Hanoi game with finesse. We employ cutting-edge technology such as OpenCV for image processing and state machines to guide the robot towards the solution – relocating all disks to Tower 3. Plus, with Python, we've incorporated speech recognition for a truly interactive experience.

## Software

This repository has 2 folders: Python files and Arduino file.

The Python code runs on a mini PC and mainly has the task for speech recognition, OpenCV features, and the finite state machine [transitions](https://github.com/pytransitions/transitions). 

Using the serial library, the Arduino code communicates with the Python code and receives the command instructions to move the arm servos to control the movements. 



## Videos

Complete game solving:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/J5HVtKAzDuo/0.jpg)](https://www.youtube.com/watch?v=J5HVtKAzDuo)


Non-matching cases:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/XxMkKzi4mR0/0.jpg)](https://www.youtube.com/watch?v=XxMkKzi4mR0)




## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


