# peri-period-app
## About Peri:
Peri is a simple period app where you can store notes about your cycle without worrying about data privacy. All data is stored in your local SQL database and you can export the data into a csv or delete the data any time you want.

## How it works:
- Click on the calendar dates to post, edit, or delete your notes.
- Navigate the calendar with the left and right arrows at the top.
- Today button to jump to today's date.
- On/Off button to toggle light and dark mode.
- Export button to retrieve all data into a csv.
- Delete button to delete all entries in calendar.

**How to run locally on your computer**: Activate your virtual environment with `source venv/bin/activate` and then use `run flask` in the folder where your app is located.

## What the application looks like:
![Screenshot of Home page in Light mode](https://imgur.com/bhjpGSJ.jpg)
_View of Home page in Light mode_\
Click on the calendar dates to view or create a note
![Screenshot of Home page in Dark mode](https://imgur.com/WLeJsjF.jpg)
_View of Home page in Dark mode_\
Click on the `on` button to toggle from light to dark mode
![Screenshot of Note](https://imgur.com/0n47ZXQ.jpg)
_View of Note creation, edit, and deletion_\
Check, add, edit, or delete a note's information

### Other notes:
- Fullcalendarjs used as template for the calendar.
- Flask with Jinja templates used to handle front-end and routing.
- SQLLite used for the database through SQLAlchemy.