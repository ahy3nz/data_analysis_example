# Data Analysis Example  
This assignment will test your data-processing skills in Python.  
## Background
According to statistical mechanics, temperatures are distributed according to a normal or Gaussian distribution. 
We will be taking temperature data from a molecular dynamics simulation and confirming whether or not the thermostat is yielding temperatures consistent with a normal distribution.
## Assignment
This repo contains the file `temp.xvg`. This files contains temperature information from a GROMACS simulaion. The file has some comments at the beginning, but the data is represented in 3 columns: Time (ps), Temperature of non-water component, Temperature of water component (each group is thermostatted separately).  
1. Fork this repo from GitHub
2. In this repo, make a folder (name should be your username). Your work should all be saved in this folder.
3. Given these temperatures, construct a figure that compares the probability distribution of the temperature from the simulation and a normal distribution (with mean and standard deviation equivalent to those from the simulation). 
4. Add, commit, and push your changes to your fork.
5. When you have finished the assignment, submit a pull request to the main branch.
A sample figure is provided below
![Sample figure](solution.png)
