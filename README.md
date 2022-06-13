1. Install & Activate Virtual Environment (optional if venv folder is missing):
    - `sudo apt install virtualenvwrapper`
    - `python3 -m virtualenv venv`
    - `. venv/bin/activate`

2. Install Dependencies:
    - `pip install -r requirements.txt` 

3. Update dotenv variables (optional)

4. Run Application:
    - `flask run --host=0.0.0.0`

Note: Run `pip freeze > requirements.txt` from the Virtual Env if additional dependencies are added.