# peri-period-app
## About Peri:
Peri is a simple period app where you can store notes about your cycle without worrying about data privacy. All data is stored in your local SQL database and you can export the data into a csv or delete the data any time you want.

<p align="center">
    <img src="app/assets/Demo.gif" alt="Demo of application" width="500"/>
</p>

## How it works:
- Click on the calendar dates to post, edit, or delete your notes.
- Navigate the calendar with the left and right arrows at the top.
- Today button to jump to today's date.
- On/Off button to toggle light and dark mode.
- Export button to retrieve all data into a csv.
- Delete button to delete all entries in calendar.
- **NEW** Jump button to jump to specific month and year in the calendar.

**How to run locally on your computer**: 
1. Install `-m env venv` to create a virtual environment.
2. Activate your virtual environment with `source venv/bin/activate`.
2. Run `pip3 install -r requirements.txt` to install all of the required packages.
3. Use `flask run` in the folder where your app is located.

## What the application looks like:
![Screenshot of Home page in Light mode](https://imgur.com/bhjpGSJ.jpg)
<p align="center"><i>View of Home page in Light mode</i></p>
<p align="center">Click on the calendar dates to view or create a note</p>

![Screenshot of Home page in Dark mode](https://imgur.com/WLeJsjF.jpg)
<p align="center"><i>View of Home page in Dark mode</i></p>
<p align="center">Click on the `on` button to toggle from light to dark mode</p>

![Screenshot of Note](https://imgur.com/0n47ZXQ.jpg)
<p align="center"><i>View of Note creation, edit, and deletion</i></p>
<p align="center">Check, add, edit, or delete a note's information</p>

### Other notes:
- Fullcalendarjs used as template for the calendar.
- Flask with Jinja templates used to handle front-end and routing.
- SQLite used for the database through SQLAlchemy.