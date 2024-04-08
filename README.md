### Mini Project 4
### Austin Howard
### INF601 - Advanced Programming in Python

# Mini Project 4 - The ID10 Ticketing System

## Description
This project is an introduction into making webapps with Django and Bootstrap.  
  
I decided to make mine into a basic ticketing system. This will allow users to create tickets and
administrators to edit them.

On top of making the core pieces of a django project (Models, Views, URLs, and Settings Python files),
I added a bootstrap modal to make a comment system for the tickets.

## Getting Started
All dependencies can be obtained through the command console in the Python IDE of your choosing.

### Step 1: Pip install requirements.txt
In a terminal window, please type the following:
```
pip install -r requirements.txt
```

### Step 2: Create SQL entries needed for the database
In a terminal window, please type the following:
```
python manage.py makemigrations
```

### Step 3: Apply the migrations to the SQL database
In a terminal window, please type the following:
```
python manage.py migrate 
```

### Step 4: Create a super user
In a terminal window, please type the following:
```
python manage.py createsuperuser 
```

### Step 5: Start the server
In a terminal window, please type the following:
```
python manage.py runserver
```

### Step 6: Navigate to the site
In your browser's URL bar, please type the following:
```
http://localhost:8000
```

## Authors
Austin Howard - [Email](A_Howard4@mail.fhsu.edu)  


## Version History

* 0.1
    * Initial release to complete the assignment

## License

This project is licensed under the GNU GPL-3.0 License - see the LICENSE file for details

## Acknowledgments
Inspiration, code snippets, etc. :
# Thanks to
* [Jason Zeller](https://www.youtube.com/watch?v=DZWe-oU5Rfg&list=PLE5nOs3YmC2THmgcLi-ogD8KiIfCjS06V&pp=iAQB)
* [Django Tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
* [Bootstrap](https://getbootstrap.com/docs/4.0/components/modal/) 
