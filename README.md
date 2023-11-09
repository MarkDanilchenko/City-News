## Description
This is a Django test project using MySQL, Docker and Django Rest Framework.


## Launch instructions
_____

1. Clone repository to your local folder;
2. *Install all packages from requirements.txt: ```pip install -r requirements.txt```;
3. *Insatll all packages from package.json: ```cd ./static && npm install```;
4. Copy dev.env to .env file: ```cp dev.env .env```;
5. Open and follow the instructions in the new created .env file;
6. For this step you should already have installed Docker and docker-compose on your PC:
- make sure You are in project folder: ```cd 'root project folder' ```;
- Run docker-compose: ```docker-compose up --build```;
- Installation can take some time, it depends on your PC resources;
- After the installation is completed, the server will start automatically on 0.0.0.0:8900;
- Open app using http://0.0.0.0:8900/ in your browser;
7. The superuser has been already created;
- You can login under current superuser using standart credentials: ```login: admin; pass: admin```;
- For password change use: ```cd 'root project folder' && python3 manage.py changepassword admin```
- Or You can manually create superuser for Your own purpose: ```cd 'root project folder' && python3 manage.py createsuperuser``` ;
8. Note that DataBase - MySQL;
9. To stop the server: ```Ctrl+C```;
10. To completely remove all created docker containers, images and volumes: ```docker-compose down --volumes```.

_____
*p.s. points № 3 and 2 are not necessary* 