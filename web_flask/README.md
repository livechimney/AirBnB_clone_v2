<<<<<<< HEAD
# AirBnB Clone: Flask Web Application

## Description

This directory contains all the Web Application files for the Python Flask App.
The Flask App and nginx are connected with gunicorn Web Server Gateway
Interface (WSGI).

## Environment

* __OS:__ Ubuntu 14.04 LTS
* __language:__ Python 3.4.3
* __application server:__ Flask 0.12.2, Jinja2 2.9.6
* __database:__ mysql Ver 14.14 Distrib 5.7.18
* __python style:__ PEP 8 (v. 1.7.0)
* __web static style:__ [W3C Validator](https://validator.w3.org/)

## Tests

* Test Flask App integration with Storage Engine:

```
$ cat 7-dump.sql | mysql -uroot -p
```

* Test complete integation with files AirBnB HTML: `10-hbnb.py` &
  `100-hbnb.html`. Execute from root directory (`AirBnB_clone`) with all the
  necessary environmental variables to establish the database storage model:

```
$ cat 100-dump.sql | mysql -uroot -p
$ python3 -m web_flask.100-hbnb
```

## License

MIT License
=======
<<<<<<< HEAD
# 0x04. AirBnB clone - Web framework
=======
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7)
All your files must be executable
The length of your files will be tested using wc
All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
HTML/CSS Files
Allowed editors: vi, vim, emacs
All your files should end with a new line
A README.md file at the root of the folder of the project is mandatory
Your code should be W3C compliant and validate with W3C-Validator (except for jinja template)
All your CSS files should be in the styles folder
All your images should be in the images folder
You are not allowed to use !important or id (#... in the CSS file)
All tags must be in uppercase
Current screenshots have been done on Chrome 56.0.2924.87.
No cross browsers
>>>>>>> 43a24faa69bbd151b8fec987ee56df7de02c39b7
>>>>>>> 2f0813143d9d93724458ff791ae5501a83b7fc94
