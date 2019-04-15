# Restful movie database

## Project description
The project's goal is to build a simple wrapper for OMDb API
using [django rest framework](https://www.django-rest-framework.org).

## Functionality
Main methods for the project are:
- ​POST /movies:
  - After passing 'Title' as a request parameter user gets a JSON
    reponse containing all the data stored in OMDb and saves it
- GET /movies:
  - User gets a JSON response containing all the infromation on
    movies proviously posted
- DELETE /movies/\<movie-id>/:
  - User can delete a movie with a given id from the database
- UPDATE /movies/\<movie-id>/:
  - User can modify specified movie's field(s)
- POST /comments:
  - User can post a comment containing movie_id and its content
    using parameters ```movie``` and ```content```
- GET /comments:
  - User gets a JSON reponse containing information about all the
    comments.
- GET /comments/\<movie-id>/:
  - User gets all comments associated with the movie of the given
    id
- GET /top:
  - User gets the ranking of the best movies in terms of number
    of comments. After passing arguments ```date_from``` and ```date_to``` in format YYYY.MM.DD user can specify the time
    range of ranked comments.

Additional functions are provided thanks to ```ModelViewSet```
taking care of that

## Requirements to use locally
- OMDb API key. You can obtain one for free [here](http://www.omdbapi.com)
- Your own django SECRET_KEY. You can generate one [here](https://www.miniwebtool.com/django-secret-key-generator/)

## Development and personal use
1. Create a file ```credentials.py``` and put it the same
  folder as ```settings.py```
2. Structure the folder as such:
```python
SECRET_KEY = 'XXXX'
API_KEY = 'XXXX'
```
3. run ```pip -r install requirements.txt```
4. run ```python manage.py migrate```
5. run ```python manage.py runserver```

Congratulations! Your project is set up.

