
Version_00_QtHelloWorld : The work started with making hallo world application.
Version_01_Form: The work continued making simple application on the base of single Widget - Form 
Version_02_MainWindow with some more advanced functionality, but shitte developer work without possibility to 
	to change methods of main object. 


Here we work with creation of new version, which will inherite MainWindow and allow us to define its methods as much as we need!

NOTE: 
Readin of readme.txt of versions 00 01 02 could help. Well especialy of previous version for current version


pyuic4   glDesignMW.ui -o glDesignMW.py
python gl.py

well for definition of menu functions simply def in derived object did not helped. Yet


# to get WiFi working in debian:
sudo apt install wireless-tools

Git Getting started:
		
https://git-scm.com/book/en/v1/Getting-Started-Git-Basics


# Assume - git is installed (on Linux)
# Do it also on Windows. See Manual above

git config --global user.name "Pavel Paulau"


use wuthout --global   for specific projects:
git config  --global user.email pavel.paulau@desy.de
p.v.paulau@gmail.com


go to Project Folder and 
git init
git add src
git add WindowsPyQT4
git commit -m 'initial project version'

git commit -m 'Clean auto generated folders and files'

in project folder:
git config   user.email p.v.paulau@gmail.com

remote repository is registered on webpage of gihub
git remote add origin https://github.com/paulau/guteluftGUI.git

git push -u origin master





git + eclipse
http://www.vogella.com/tutorials/EclipseGit/article.html

