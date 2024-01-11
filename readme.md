# FavoriteTunes
## Prerequisites

- Python
- Django

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/jayantpranjal0/FavoriteTunes.git
    ```

2. Change into the project directory:

    ```
    cd FavoriteTunes
    ```

3. Install the project dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Run database migrations:

    ```
    python manage.py migrate
    ```

4. Run 

    ```
    python manage.py runserver
    ```

## Creater SuperUser

1. Run 
    ```
    python manage.py createsuperuser
    ```
    and enter relvant details.

## Using the Project

1. Open the browser and go to http://localhost:8000/ for introductory screen.
2. Go to http://localhost:8000/admin/ and login with the superuser credentials.
3. Add the songs and artists in the database.
4. Go to http://localhost:8000/songs and http://localhost:8000/artists to see the list of songs and artists respectively.
5. Go to http://localhost:8000/songs/<song_id> to see the details of the song with id <song_id>.
6. Go to http://localhost:8000/artists/<artist_id> to see the details of the artist with id <artist_id>.
7. Go to http://localhost:8000/add_song to add a new song.
8. Go to http://localhost:8000/add_artist to add a new artist.

