# pronto_code_challenge
Requirements:
1. Create a cli application to take input from user as a string to make a robot move and find the distance from final position to starting position.
2. Make the robot move with four available command:
	F - Move forward 1 unit
	B - Move backward 1 unit
	R - Turn right 90 degree
	L - Turn left 90 degree
3. Find the shortest distance from robot's current location to start position.

conditions:
	1. Robot can turn 90 degrees at a time.

* **Main.py** - This is the main module to start the program.

* **Movement.py** - This is the file which has the commands such as move forward, move backwar, turn left, turn right.

* **Orientation.py** - This contains the enum **North**, **South**, **East** and **West** which is used in robot's orientation.

* **Robot.py** - This file contains all the singleton structure for initialising the robot, getting direction as well the axis values.
* **UserInput.py** - This file takes the user's input and converts to commands for the robot.
* **DistanceFinder.py**  - This is the file which conains the Dijkstra's algorithm to get the shortest route for the robot to it's way back home.

## Assumptions made:
	* Robot cannot rotate more than once at a time, but can rotate with consecutive commands. 
		For example, F1,R3 won't work whereas F1,R1,R1,R1 will work.
	* Robot can move upto 9 times at a time to reduce the complexity.
	* Robot's staring position is 0,0 at North. This can be changed from the Movement.py file.
	
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 


### Prerequisites

Things you'll need to install before running the program:
* [python 3.7](https://www.python.org/downloads/release/python-373/)

check the python version to verify installation was successful

 For python 3
 ```
- python3 version
 ```
<p align="center">
  <img src="version_check.png" width="350" title="hover text">
</p>

 
## Installing

## For python 3.7
After installing python 3.7, please install the following libraries. (This procudes are for macOS only!)

Update the pip first to latest version.
 ```
pip3 install --upgrade pip
 ```

If needed:
Install requests[security] to resolve the issue with SSLError from requests
```
pip3 install -U requests[security]
```

## Running Main program
Git clone the repository by typing in your command promt/terminal :

change directory to pronto_code_challenge by typing:
``` cd 	pronto_code_challenge ```

And then run the main program
```
python3 Main.py
```
This wil show the main menu and ask for user input.



The program can be also run in executable format.
First, make the program executable
```
chmod +x Main.py 
```
Then 
```
./Main.py
```
to run the main program.

## Running the tests

This program is tested on 
- macOS Mojave 
   - python 3

## Alternate Way:
    The rotation of robot facing could be done with Matrix which will reduce 
    the coupling and increase cohesion in the code. This would work like, If 
    user's input contains 'L1,F4', a matrix will be multiplied to the current
    axis values which will give the 90 degree anti-clockwise rotation. The 'F4'
    will then be multiplied with that result to get the overall outcome. 
    
## Shortest Distance:
    To find the shortest distance, Dijkstra's algorithm should be used where it will check
    if robot's current location is smaller than it's neighbour, then robot will move to   
    the position. This will continue until the robot reaches home at (0, 0). 
    I wasn't aware of the Dijkstra's algorithm, I tried with A** Search but didn't get
    the shortest route as expected which was mentioned in some of the conversation in
    stackoverflow too but eventually this consumed some of my time. 
    I beleive with this logic and use of Dijkstra's algorithm would make
    it possible to find the shortest distance.
    

## Author

* **Ahnaf Shahriar Abir** - [pronto_code_challenge](https://github.com/AhnafShahriarAbir/pronto_code_challenge)
   **email:** abir3577189@gmail.com

### Thank you for Reading me          - Readme.md :)
