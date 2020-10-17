# Gipy
Gipy is a python and batch script-based program for Windows, which helps the programmers to automates the process of connecting local project files to the GitHub repository, in the beginning, using CMD.
If you are not using GitHub desktop software then it might take time to do these steps-
1. Navigating to the project folder
2. Create a folder as the project name
3. Getting into it
4. Creating a README.md file
5. In CMD: git init
6. Doing  GitHub login, and create a new repository.
7. Copy the remote line
8. Adding remote to the local folder
9. CMD: git add .  
10. CMD: git commit -m "first commit"
11. CMD: git push -u origin master
12. CMD:  code .

Gipy can do these all steps in a single command.

## Install
```cmd
git clone https://github.com/devo-id/gipy.git
```

## Requirement
webdriver,
selenium,
python environment

## Prerequisite
Update the path for project folder and webdriver in gipy.py.

## Usage
Run it in CMD as
```cmd
python gipy.py username password repo_name
```

