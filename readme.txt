Prerequisites:

Git: Ensure you have Git installed on your system.
Python and Django: Make sure you have Python and Django installed.
A GitHub Account: You'll need a GitHub account to access the repository.
Cloning the Repository:
Open your terminal or command prompt.

Navigate to the desired directory: Use the cd command to navigate to the directory where you want to clone the project.   

Clone the repository: Use the following command

git clone https://github.com/cytoq/manga-tracker.git

Setting Up the Virtual Environment:
Navigate to the Project Directory:

Use the cd command to navigate into the cloned directory:

cd your_repository_name

Create a Virtual Environment:

Create a virtual environment to isolate project dependencies:
     python -m venv venv
```

Activate the Virtual Environment:
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

Starting the Development Server:

Start the Django development server:


python manage.py runserver

