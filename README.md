# python_automation_cpp
This is python script that automate the cpp compilation throught console.

## How to use it:
First you need to have python 3.x.x and g++ compiler install. Then you will need vscode in order to run this program, on vscode install the extension "terminal-command-keys" 
<a href="https://ibb.co/fYSBZW7"><img src="https://i.ibb.co/HD21RyQ/Screen-Shot-2021-10-28-at-14-23-53.png" alt="Screen-Shot-2021-10-28-at-14-23-53" border="0"></a>

Now its time to configure your shourcuts: 
press cmd+shift+p or ctrl+shift+p type key and open the following:
<a href="https://ibb.co/vJbPS2D"><img src="https://i.ibb.co/193qkHb/Screen-Shot-2021-10-28-at-14-26-21.png" alt="Screen-Shot-2021-10-28-at-14-26-21" border="0"></a>

Inside of it copy and paste the keybinding-config.json file in this repository. 
Open a vscode file press cmd+b and cmd+h and enjoy!

## Motivation
I'm a mac user, one day I wanted to upload my C++ projects to a github repository and I noticed that I had a bunch of executable file, since C++ its a compiled lenguage. In unix based OS you cant add this executable files to .gitignore, so that was a problem. 

## Solution 
I came up with an elegant solution, when I compiled my programs, this executable files will go to a folder /bin and then I can add /bin in .gitignore and problem solved! 

## Extras: 
Alse this code give you beatifully colored message in your consolo, telling you if there are sort of mistakes or typos. 

<a href="https://ibb.co/y63QJfB"><img src="https://i.ibb.co/N94yzVn/Screen-Shot-2021-10-28-at-14-17-09.png" alt="Screen-Shot-2021-10-28-at-14-17-09" border="0"></a>
<a href="https://ibb.co/Z14mx0z"><img src="https://i.ibb.co/0V4trxy/Screen-Shot-2021-10-28-at-14-17-31.png" alt="Screen-Shot-2021-10-28-at-14-17-31" border="0"></a>
<a href="https://ibb.co/8b1HV0m"><img src="https://i.ibb.co/r3DVJmQ/Screen-Shot-2021-10-28-at-14-17-47.png" alt="Screen-Shot-2021-10-28-at-14-17-47" border="0"></a>
<a href="https://ibb.co/Xb1cQWV"><img src="https://i.ibb.co/Dth0J1L/Screen-Shot-2021-10-28-at-14-18-05.png" alt="Screen-Shot-2021-10-28-at-14-18-05" border="0"></a>

In this repository I have not exclude the /bin folder to you, but its just for demostration the ideal thing is that you add bin in your .gitignore file



