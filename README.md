# Words counter for Voxy's test

Words counter provides a simple way to count words inputted in the text field.

This counter already ignores the following characters:

##### . , ! ? " ; :

## Getting started
___ 
1) Create and activate a virtual environment
   ```
   $ python3 -m venv env
   $ source env/bin/activate
   ```
2) Install all required Libraries given in requirement.txt
   ```
   $ pip install -r requirement.txt
   ```
3) Start Django development server
   ###### Make sure that you are in root directory
   ```
   $ Python manage.py runserver
   ``` 
4) Visit http://127.0.0.1:8000/counter/ with your web browser.
<img width="1512" alt="words_counter" src="https://user-images.githubusercontent.com/88399737/178083126-0c618d9b-c4c7-4db1-a52b-43bf24ab26b9.png">


5) Type or paste any text and press Run counter

## TODO list

- [ ] Implement field validation using validators
- [ ] Fix the result output appearing before request
- [ ] Improve appearance and styling

### Project's Scheme
                  
      ├── apps
      │   └── forms
      │       ├── templates
      │       ├── admin.py
      │       ├── apps.py
      │       ├── forms.py
      │       ├── models.py
      │       ├── tests.py
      │       ├── urls.py
      │       └── views.py
      ├── static
      │   ├── css
      │   ├── fa
      │   └── js
      ├── words_calculator
      │   ├── asgi.py
      │   ├── settings.py
      │   ├── urls.py
      │   └── wsgi.py
      ├── LICENSE
      ├── README.md
      ├── db.sqlite3
      ├── main.py
      ├── manage.py
      └── requirements.txt
