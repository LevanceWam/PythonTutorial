# PythonTutorial
Welcome to my Python tutorial series.
Videos by Mosh Hammedani
https://youtu.be/_uQrJ0TkZlc

## Tools Used
```
Pycharm
Anaconda
Jupyter
Bootstrap
Django
Python
HTML
Terminal
VS Code
dbsqlite
Excel
Github
Git branches
```


## Hello World

This folder contains a file with the basics of Python.
From Loops, If Statements, Tuples, List, and etc.
You will find all the core skills you need in this folder 
from what I learned in this tutorial.

Each Section is commented out so if there is a specific part you are looking for 
it should not be hard to find.

To run any of the code in the HelloWorld folder use the run this code feature in 
pycharm and it will run in the terminal provided in pycharm.

### Excel.py

The Excel files provided in project can be found in the youtube video description 
provided above.

This file was a small tutorial on how to use Python to interact with Excel files.

This code below is needed to interact with Excel

```
pip install openpyxl 
```

## Machine Learning

This folder contains lessons on machine learning with python.
The preferred tools to use for this is Anaconda and Jupyter.

The idea for this project is to get the machine to make a predicion
on what kind of music a person listens too based on age and gender.

First Download Anaconda this will also download jupyter to the project.

```
https://www.anaconda.com/distribution/
```

Download version mentioned in the video

Then run the next line of code to start a Jupyter notebook

```
jupyter notebook
```

## Django Project

First Project in Django,
This is a basic project that helps us understand.
The amount of cool thiings that Django is capable of.
We are shown the admin controls and many other interesting skills.

### Terminal Commands Used
```
 pip install django==2.1  
 django-admin startproject pyshop . 
 python3 manage.py runserver
 python3 manage.py startapp products
 python3 manage.py makemigrations
 python3 manage.py migrate
 python3 manage.py createsuperuse
 ```

 # ***IMPORTANT***

 During the creation of the project there was an issue when you get to the admin
 And you are going to add the products to the database from the admin panel.

 The way I solved the issue was deleting the db.sqlite file and restarted the migrations again 
 So keep an eye out for that if that happens