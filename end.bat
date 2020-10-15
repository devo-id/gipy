@echo off
cd %1\%2
git remote add origin https://github.com/%3/%2.git
git add . 
git commit -m "first commit"
git push -u origin master
code .