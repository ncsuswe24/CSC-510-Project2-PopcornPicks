# Setup and Installation Procedure

### Step 1: Clone the repository from GitHub
```bash
git clone https://github.com/ncsuswe24/CSC-510-Project2-PopcornPicks
```

(OR) Download the .zip file on your local machine from the following link:
```bash
https://github.com/ncsuswe24/CSC-510-Project2-PopcornPicks
```

### Step 2: Install required packages with pip
```bash
cd CSC-510-Project2-PopcornPicks
pip install -r requirements.txt
```
Note: We use python version 3.10 to quickly install requirements and run the project.

### Step 3: Get a TMDB API key at their website [here](https://www.themoviedb.org/signup)
- Your API key can be generated under the settings page after you create your account.
```bash
To get an API from TMDB:
* Signup to your https://www.themoviedb.org/signup
* Under the Account icon, click Settings.
* On the API page, click on the link under the Request an API Key section.
* Register an API key.
* Agree to the terms of use and fill in the required information.
```

### Step 4: Create a `.env` file to place the API key in
```bash
touch app/src/.env
vim .env
...
TMDB_API_KEY=...
```

### Step 5: Setup DB and start server
```bash
cd app
python3 app/init_db.py
python3 app/run.py
```

### Step 6: You can now open the website on [localhost](http://127.0.0.1:8000/)
