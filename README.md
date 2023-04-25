# Restaurant Management Project

# Table of Contents
<br>

1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Installation and Setup](#installation-and-setup)
4. [Nav Bar](#nav-bar)
5. [Footer](#footer)
6. [Landing Page](#landing-page)
7. [Menu Page](#menu-page)
8. [Reservation Page](#reservation-page)
9. [Reservation List Page](#reservation-list-page)
10. [Reservation List Users](#reservation-list-users)
11. [Edit Reservation](#edit-reservation)
12. [Sign Up Page](#sign-up-page)
13. [Admin Page Features](#admin-page-features)
14. [Testing](#testing)
15. [Wireframes from Pre-Project](#wireframes-from-pre-project)
16. [Deployment](#deployment)
17. [Agile Process](#agile-process)
18. [Credits](#credits)


## Introduction

This is a restaurant management project created using the Django web framework. The project aims to provide an efficient solution for managing various restaurant operations, such as managing menus, booking tables, and handling customer information.

<br>

## Technologies Used

- Python
- Django web framework
- PostgreSQL for database management
- Cloudinary for image and file storage
- Bootstrap4 for responsive design
- django-allauth for authentication
- django-crispy-forms for better form rendering
- django-summernote for rich text editing
- django-phone-field and django-phonenumber-field for phone number handling
- Gunicorn for deployment on Heroku

<br>

## Installation and Setup

To get this project up and running, follow these steps:

1. Clone the repository:

- https://github.com/Sajalol/Django_restaurant_proj1

2. Install the required dependencies from `requirements.txt`:
- pip install -r requirements.txt

3. Create a new file called `env.py` in the project's root directory and add the following environment variables:
- import os
* os.environ['SECRET_KEY'] = 'your-secret-key'
* os.environ['DATABASE_URL'] = 'your-database-url'
* os.environ['CLOUDINARY_URL'] = 'your-cloudinary-url'
* Replace 'your-secret-key', 'your-database-url', and 'your-cloudinary-url' with the actual values for your project.

4. Apply the database migrations:
- python manage.py migrate

4. Run the development server:
- python manage.py runserver

Now, you can access the application at `http://127.0.0.1:8000/`.

Note: Remember not to include your `env.py` file in version control, as it contains sensitive information. Add it to your `.gitignore` file to ensure it's not tracked by Git.


<br>

## Nav Bar

The navbar is easy to navigate, and features all three pages and the sign up, sign in and logout if you're logged in. And the navbar is full responsive. The navbar is alike on all the pages.

![nav_bar](https://res.cloudinary.com/saja/image/upload/v1662210575/static/img/nav_bar_pn4zur.png)

<br>

## Footer

* The footer includes: 
    - links to our social page, with included _blank to avoid the users leaving our page.
    - Location of the restaurant, with country, city and local address
    - Opening hours
    - Contact information

    - ![footer](https://res.cloudinary.com/saja/image/upload/v1662212651/static/img/footer_vyugok.png)

<br>

## Landing Page

- The landing page for the restaurant will show you some welcoming text, opening hours and easy navigation to the menu with special dishes and the reservation page. 
- When you have done an edit to your reservation, you will be redirected to the landing page with a success message
- When you have deleted one of reservations, you will be redirected to the landing page with a success message

![Welcome_text](https://res.cloudinary.com/saja/image/upload/v1662208140/static/img/welcome_ruybsa.png)

<br>

## Menu page

The menu page has a list of the restaurants special dishes.

![Menu](https://res.cloudinary.com/saja/image/upload/v1662208334/static/img/menu.page_zb7abp.png)


<br>

## Reservation Page

To access the reservation page you have to login. If you're not logged in, and you click the reservation page you will be sent to a sign in page. 

![Sign_in](https://res.cloudinary.com/saja/image/upload/v1662209060/static/img/sign_in_qiiut9.png)

After you have signed in, you will be welcomed with your username on the reservation page and asked to fill out the reservation form

![reservation_form](https://res.cloudinary.com/saja/image/upload/v1662209059/static/img/reservation_form_vibhlk.png)

When you have successfully reserved a table, you get a success message.

![reservation_success](https://res.cloudinary.com/saja/image/upload/v1662209892/static/img/reservation_successful_wjvw2g.png)

If you try to reserve a table thats already reserved on that date and time you get a error massage

![reservation_error](https://res.cloudinary.com/saja/image/upload/v1662209891/static/img/reservation_form_error_ap1ydy.png)


<br>

## Reservation List Page

To access the reservation list page, you must have staff permissions. The link in the navbar won't show unless you have staff permissions. This is how it will look if you are staff:

![reservation_list](https://res.cloudinary.com/saja/image/upload/v1662632930/static/img/reservation_list_yteqnd.png)

Without staff access the reservation list wont show

From this reservation list page you get a list of all the reservations that has been made, and you are also able to delete reservations from this page. The list is also ordered by date.

![reservation_list1](https://res.cloudinary.com/saja/image/upload/v1662633087/static/img/delete_reservations_i0cjpi.png)

When you click "Delete Reservation" you get a popup asking you if you are sure you want to delete this reservation

![reservation_delete](https://res.cloudinary.com/saja/image/upload/v1662633086/static/img/delete_reservations1_rbdpcw.png)

If you try to access the list_view link without staff permissions you get 403 error, looking like this:

![reservation_403](https://res.cloudinary.com/saja/image/upload/v1662633282/static/img/403_sjyrj4.png)


<br>


## Reservation list Users 

![reservation_user](https://res.cloudinary.com/saja/image/upload/v1681847564/Userlistreservation_he8zfq.png)

List of all your active reservations for users. You are only able to edit / delete your own reservations

<br>

## Edit reservation

![reservation_edit](https://res.cloudinary.com/saja/image/upload/v1681847727/edit_reservation_iuimcm.png)

This is the reservation edit page you get sent to when you click "edit"

<br>

## Sign Up Page

The sign up page has some welcoming text and asks for:
- Username
- Email
- Password and repeat the password again

![sign_up](https://res.cloudinary.com/saja/image/upload/v1662213001/static/img/Sign_up_yqbcrp.png)


<br>


# Admin Page Features 

<br>

## Admin Menu Page

The owner of the page can easly edit the menu page through the admin menu page. With deleting current menu's or add more / add new menu's to the page

![Menu_admin](https://res.cloudinary.com/saja/image/upload/v1662208564/static/img/menu_admin_zwahi3.png)

* To add a menu just click "+ Add" or "Add Menu +" in the top right corner and fill out the info thats needed.
* To delete a menu, just select which menu you would like to delete left of the name, and choose "Deleted selected Menus" in Action: and press "Go".
* This will add or delete a menu in the menu page

<br>

## Reservation Admin Page

When the reservation has been sent successfully, the owner of the page can easly see the reservation in the admin page with: Username, phone number, number of guests, date, time and seats.
Currently the reservations gets auto approved.

![reservation_admin](https://res.cloudinary.com/saja/image/upload/v1662210222/static/img/reservation_complete_jdfzia.png)

<br>

## Adding Tables Admin Page

The owner of the page can easly add or remove more tables available for reservation. This can be done by:
* Adding seats:
    - Click Tables and or "+Add" next to Tables or "Add Table +" in the top right corner.
    ![adding_table](https://res.cloudinary.com/saja/image/upload/v1662212065/static/img/admin_tables_yyhw6e.png)
    - Then fill out how many seats the table has, with minimum seats and maximum.

    ![adding_seats](https://res.cloudinary.com/saja/image/upload/v1662212064/static/img/seats_admin_g9tyah.png)

* Deleting seats:
    - In the "Tables" section, click the selected table you would like to delete and choose "Delete selected tables" and click "Go". 
    - ![deleting_seats](https://res.cloudinary.com/saja/image/upload/v1662212227/static/img/delete_seats_ghoepq.png)

<br>

# Testing

<br>

## Validator Testing

* HTML
    - No errors returned when passing through <a href="https://validator.w3.org/" target="_blank">HTML Validator</a>, except the django text.
* CSS
    - No errors returned when passing through <a href="https://jigsaw.w3.org/css-validator/validator" target="_blank">CSS Validator</a>.
* PythonChecker
    - Used https://www.pythonchecker.com/ to check my python code, and all of the code had no serious issues. Code average above 80% in stats. Other pep8 testers seems to be out of function at time of testing.
<br>


## Reservation Form Testing

* Variations of testing:
    - Testing to reserve on the same date, time and table. Testing with multiple users. Making sure it gives an error when trying to reserve an occupied table on the same time and date. 
    - Testing to try to reserve without filling out all the whole form.
    - Testing the access without login in.
    - Testing that the info from the user that reserves the table always comes in the admin page.

<br>

## Reservation Deletion from List View 

* Variations of testing:
    - Confirming that new reservations show up in the list view.
    - Confirming that when you delete a reservation from the list view its actually deleted with confirming in admin view.
    - List getting instantly updated

<br>

## Edit and Delete Buttons in Users List View
- During the testing phase, I also focused on ensuring that the edit and delete buttons in the users list view functioned correctly and provided the desired user experience. Here's how I tested them:

* Edit Button:
1. Logged in as a user and navigated to the user's reservation list.
2. Clicked on the 'Edit' button for a specific reservation and checked whether it redirected me to the reservation edit page.
3. Updated the reservation details, such as date, time, or the number of guests, and submitted the form.
4. Verified that the changes were saved and reflected in the user's reservation list and the admin panel.

* Delete Button:
1. Logged in as a user and navigated to the user's reservation list.
2. Clicked on the 'Delete' button for a specific reservation and checked whether a confirmation pop-up appeared, asking to confirm the deletion.
3. Confirmed the deletion and ensured that the reservation was removed from the user's reservation list.
4. Verified that the deleted reservation was also removed from the admin panel's reservation list.

Through these tests, I ensured that both the edit and delete buttons provided the desired functionality and user experience.

## Menu Form Testing

* Variations of testing:
    - Testing to delete menu and see if it gets deleted in the menu page.
    - Testing to add more menu's and see if it gets added in the menu page.

<br>

## Testing Buttons

* Testing that all the nav buttons, reservation form button, nav buttons and footer button works.

<br>

## Sign in / Sign out

* Testing that login, logout etc works without any issues

<br>

## Testing On Multiple Devices

* Testing the web page on different devices with no issues. The webpage is responsive from desktop, to small mobile phones and tablets. 
* For some reason <a href="https://ui.dev/amiresponsive" target="_blank">amIresponsive</a> won't load my web page. But tested the webpage with using the toggle device toolbar option available in the developer tools in Chrome. And also loaded the page on my physical phone and ipad to make sure it loaded. 

<br>

## Unfixed bugs

* No known bugs

<br>

# Wireframes from pre project

## Homepage

![Homepage](https://res.cloudinary.com/saja/image/upload/v1670965155/static/img/homepage_loghpn.png)

<br>

## ReservationList

![ReservationList](https://res.cloudinary.com/saja/image/upload/v1670965155/static/img/reservationlist_swgrwh.png)

<br>

## MenuList

![MenuList](https://res.cloudinary.com/saja/image/upload/v1670965155/static/img/menulist_eu0sit.png)

<br>

## Admin Reservation List

![AdminList](https://res.cloudinary.com/saja/image/upload/v1670965155/static/img/adminreservationlist_fgckoi.png)

<br>

# Deployment

This project is deployed using Heroku for the Django.

1. Create a new Heroku app.
2. Install the required Heroku add-ons, such as the PostgreSQL or another database.
3. Set the environment variables for the deployment, such as the `SECRET_KEY`, `DATABASE_URL`,`CLOUDINARY_URL` and any other necessary variables.
4. Update the `ALLOWED_HOSTS` setting in your Django project to include the Heroku app's domain.
5. Commit your changes and push the project to your GitHub repository.
6. Connect your Heroku app to your GitHub repository and enable automatic deploys.
7. Deploy your app by triggering a manual deploy or pushing new changes to your GitHub repository.

## Additional Deployment Notes

- Make sure to set the environment variables for the deployment, such as the `SECRET_KEY`, `DATABASE_URL`, and any other necessary variables.
- Remember to run `collectstatic`or any other way to serve static files for the Django app to serve static files in production.
- Add `Port` `8000` to Config vars
- Add `DISABLE_COLLECTSTATIC` `1` to config vars
- Remember to set `DEBUG = FALSE` in settings during deployment

## My deployed heroku link:

- <a href="https://django-restaurant-1.herokuapp.com/" target="_blank">Heroku Link</a>

<br>

## Agile Process
<br>

### 1. User Stories and Epics

We maintain a list of user stories and epics in this README file. Each user story includes a clear description and acceptance criteria. User stories are grouped under their corresponding epics.
<br>

### 2. Prioritization

User stories are prioritized based on their importance and complexity. High-priority user stories are listed at the top of each epic section.
<br>

### 3. Progress Tracking
<br>

To track the progress of user stories, we use the following status labels:

- [ ] To Do
- [ ] In Progress
- [ ] In Review
- [ ] Done

Update the status of a user story by checking or unchecking the corresponding checkbox.
<br>

## User Stories and Epics
<br>

### Epic 1: User Authentication
<br>

#### User Story 1.1: As a user, I want to register for an account
<br>

- [ ] Done
- Acceptance Criteria:
  - Users can provide their email, username, and password to create an account
  <br>

#### User Story 1.2: As a user, I want to log in to my account

- [ ] Done
- Acceptance Criteria:
  - Users can log in using their email/username and password
  - Users are redirected to the dashboard after successful login
  <br>

### Epic 2: Reservations
<br>

#### User Story 2.1: As a user, I want to create a reservation

- [ ] Done
- Acceptance Criteria:
  - Users can provide their phone number, date, time, and number of guests to make a reservation
  - Users receive a confirmation message after creating a reservation
  <br>

#### User Story 2.2: As a user, I want to view my reservations
- [ ] Done
- Acceptance Criteria:
    - Users can view a list of their reservations
    - Users can Edit and delete their reservations
    <br>


#### User Story 2.3: As a Admin, I want to view and manage my reservations. And edit menu

- [ ] Done
- Acceptance Criteria:
  - Admin can view a list of their reservations
  - Admin can edit or delete their reservations
  - Admin can edit menu
  <br>

#### User Story 2.4: As a user, I want to edit my reservations

- [ ] Done
- Acceptance Criteria:
  - Users can access the edit_reservation page for their reservations
  - Users can update the date, time, and number of guests for their reservations
  - Users receive a confirmation message after updating their reservations
<br>


# Credits

* Code Institute for training.
* Various articles and youtubers for ideas. 
* Bootstrap for making templates much easier.
* Code Institute Slack and Tutoring assistance. 