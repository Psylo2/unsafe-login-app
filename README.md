# Safe Register & Login Administration

__Unsafe mode for Demonstration.__

Build with:

__BACKEND:__ _Python 3.9 & Flask_

__FRONTEND:__ _JS, HTML & CSS_

__INTEGRATIONS:__ _Jinja2_

Deployed over Docker, inorder to contain a safety lab environment

## Endpoints

**Home**

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

endpoint: `/`\
![Home](https://user-images.githubusercontent.com/71320956/132021532-a0627e90-6b8b-4986-b463-d527121cdbd1.png)


## User

### Register

User Register by given _Name_, _E-mail_, _Password_ and _re-Password_

__methods:__ `GET`, `POST`\
__endpoint:__ `/users/register`
![Register](https://user-images.githubusercontent.com/71320956/132022005-2f2ef168-eca6-4b47-be77-e3874cc761c7.png)

__CSRF attack on endpoint:__
````
$ curl -X POST -F 'username=Hacker' -F 'email=yougot@HACKED.com' 
-F 'password=AAaa1212@!12' -F 're_password=AAaa1212@!12' 
http://127.0.0.1:5000/users/register
````
\
__Result of attack:__\
![HackerRegistrationDB](https://user-images.githubusercontent.com/71320956/128612992-0c331aad-93c2-46d2-97a6-5ffe32c645da.PNG)


### Login

User Login by given _Name\Email_ and _Password_

__methods:__ `GET`, `POST`\
__endpoint:__ `/users/login`

![Login](https://user-images.githubusercontent.com/71320956/132021786-a0692f42-5684-443d-9e47-1c41ade33482.png)
__CSRF attack on endpoint:__
````
$ curl -X POST -F 'name_email=Hacker' -F'password=AAaa1212@!12' 
http://127.0.0.1:5000/users/login
````
__Result of attack:__\
![HackerLogin](https://user-images.githubusercontent.com/71320956/132028332-a50810ff-ff66-4d7c-9aae-61b58ccc2ef5.png)

### Change Password

User Change Password by given _Username_, _E-mail_, _New Password_ and _re-Password_

__methods:__ `GET`, `POST`\
__endpoint:__ `/users/change_password`

![ChangePassword](https://user-images.githubusercontent.com/71320956/132022600-dc246f61-4f28-44cd-b211-d8e4a6c5473d.png)
__CSRF attack on endpoint:__
````
$ curl -X POST -F 'username=Hacker' -F 'email=yougot@HACKED.com' 
-F 'password=BBbb1212@!12' -F 're_password=BBbb1212@!12' 
http://127.0.0.1:5000/users/change_password
````
__Result of attack:__\
![HackerChangePassword](https://user-images.githubusercontent.com/71320956/128613015-03a99a41-9c0f-45a7-9a0f-826468d10328.PNG)


### Logout

User Logout

__methods:__ `GET`\
__endpoint:__ `/users/logout`
![Logout](https://user-images.githubusercontent.com/71320956/132023375-5e99e325-8b4d-4442-8b9b-710505dfeb8a.png)

## Admin

### Admin's Menu

__methods:__ `GET`\
__endpoint:__ `/admin/menu`

![AdminMenu](https://user-images.githubusercontent.com/71320956/132023684-0d6a389c-528a-430b-95b1-f89cc7cc7581.png)

### User's List

Display all registered users & __Block/Unblock__ users

__methods:__ `GET`\
__endpoint:__ `/admin/all_users`

![UsersList](https://user-images.githubusercontent.com/71320956/132024331-fa5fb0f4-97ba-42c1-afe2-a515b37d6e4b.png)

### Password Configuration

Change password configuration:

* Length
* Complexity
* History
* Fail attempts

__methods:__ `GET`, `POST`\
__endpoint:__ `/admin/password_config`

![PasswordConfiguration](https://user-images.githubusercontent.com/71320956/132024704-0e2f0304-a427-4671-9132-be957b3d5477.png)

__CSRF attack on endpoint:__
````
$ curl -X POST -F 'upper=0' -F 'lower=0' -F 'digits=0' 
-F 'spec=0' -F 'use_dict=0' -F 'length=0' -F 'history=10' 
-F 'tries=1000'  http://127.0.0.1:5000/admin/password_config
````
