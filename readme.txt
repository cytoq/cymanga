(message for the person grading this project: i forgot to add the .env info in the form before i submit it, feel free to DM me on discord for it my account is @cyto_oq)                                                                                                          (also as of the time im writing this, i am currently sick so please go easy on me! :) )

Hey, hello! Welcome to Cymanga! This app allows you to take a look at various mangas and check their user-given ratings and comments to decide if they're worth a try. What does it feature?

A homepage that lets you login/register. (Or not, if you're already logged in. Then it looks like a typical homepage)
Several options on the header:
1. Home (self explanatory, you get redirected to the homepage)
2. Manga List - You get a full view of all the mangas that the site has to offer. Their covers are displayed alongside an option to check them out in a more detailed manner (Seeing genre, whether they're still ongoing or already completed, rating and comments from other users)
3. Profile - General info about your profile with the option to delete your edit or delete your account, but not without confirmation ofcourse. You can also reset your password. (That one took a while to get to work)
4. Logout (pretty self explanatory as well)

You, as a user, also get the oppurtunity to leave comments on mangas you find interesting, with the option to later edit or delete them if you've changed your mind. (Or if you said something embarassing)
You can also leave ratings that together with everyone else's will get taken into account when calculating a certain manga's average rating!


INSTRUCTIONS TO SETUP:

Prerequisites:

Git: Ensure you have Git installed on your system.
Python and Django: Make sure you have Python and Django installed.

1. Cloning the Repository:
Open your terminal or command prompt.

Navigate to the desired directory: Use the cd command to navigate to the directory where you want to clone the project.   

Clone the repository: Use the following command

git clone https://github.com/cytoq/cymanga.git

2. Setting Up the Virtual Environment:
Navigate to the Project Directory:

Use the cd command to navigate into the cloned directory:

cd your_repository_name

Create a Virtual Environment:

Create a virtual environment to isolate project dependencies:
     python -m venv venv

3. Activate the Virtual Environment:

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate
  
Installing Dependencies:

Install the required packages listed in the requirements.txt file:

pip install -r requirements.txt

Running Migrations:

Apply any database migrations:

python manage.py migrate

Activate API:

python manage.py import_mangas

Starting the Development Server:

Start the Django development server:


python manage.py runserver

