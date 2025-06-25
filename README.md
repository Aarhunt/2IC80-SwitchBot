# Project
This is the dashboard created by group 4 for the Lab on Offensive Computer Security course. It is a dashboard that allows the user to remotely manipulate a SwitchBot Curtain, sending various pre-programmed commands to it.

Additionally, it reads the current data of the selected SwitchBot curtain and displays it live. 

In the beginning, it can take quite a lot of time for the program to start. This is because it is scanning all the devices to find whether there is a SwitchBot present.

## Requirements
Run the following command to install the required packages:
`pip install -r requirements.txt`

This software has only been tested on Linux machines and is confirmed to run on Linux machines. 
It might work on a Windows machine, this is unknown. 

## Running
Run the following command to run the dashboard:  
`streamlit run dashboard.py` 
