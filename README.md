# Django E-commerce Web App
This is an eCommerce website created using the Django Web framework.  

## Features 
- User registration and authentication
- Shopping cart for both registered and anonymous users
- Responsive design 

## Screenshots
<img src="https://user-images.githubusercontent.com/75874394/113521483-599dce00-95b7-11eb-91f0-641ecab246cf.PNG" width=400> <img src="https://user-images.githubusercontent.com/75874394/113521497-6b7f7100-95b7-11eb-857d-f272a57a28c9.PNG" width=400>

## Installation
**Clone Project**
```
$ git clone https://github.com/vrrao01/e_commerce.git
$ cd e_commerce
```
**Create Virtual Environment**
> Make sure you have already installed pipenv
```
$ pipenv install --python=3.8 -r requirements.txt
$ pipenv shell
```
**Migrate**
```
$ cd Ecommerce
$ python manage.py makemigrations
$ python manage.py migrate
```
**Run Server**
```
$ python manage.py runserver
```
> Enter [http://127.0.0.1:8000/](http://127.0.0.1:8000/) on your browser

## Possible Improvements
- [ ] Payment Integration
- [ ] Allow sellers to add their products
- [ ] AJAXify the website
