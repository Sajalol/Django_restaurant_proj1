# Indian Fantastic
<br></br>

## Nav Bar

The navbar is easy to navigate, and features all three pages and the sign up, sign in and logout if you're logged in. And the navbar is full responsive. The navbar is alike on all the pages.

![nav_bar](https://res.cloudinary.com/saja/image/upload/v1662210575/static/img/nav_bar_pn4zur.png)

<br></br>

## Footer

* The footer includes: 
    - links to our social page, with included _blank to avoid the users leaving our page.
    - Location of the restaurant, with country, city and local address
    - Opening hours
    - Contact information

    - ![footer](https://res.cloudinary.com/saja/image/upload/v1662212651/static/img/footer_vyugok.png)

<br></br>

## Landing Page

The landing page for the restaurant will show you some welcoming text, opening hours and easy navigation to the menu with special dishes and the reservation page. 

![Welcome_text](https://res.cloudinary.com/saja/image/upload/v1662208140/static/img/welcome_ruybsa.png)

<br></br>

## Menu page

The menu page has a list of the restaurants special dishes.

![Menu](https://res.cloudinary.com/saja/image/upload/v1662208334/static/img/menu.page_zb7abp.png)


<br></br>

## Reservation Page

To access the reservation page you have to login. If you're not logged in, and you click the reservation page you will be sent to a sign in page. 

![Sign_in](https://res.cloudinary.com/saja/image/upload/v1662209060/static/img/sign_in_qiiut9.png)

After you have signed in, you will be welcomed with your username on the reservation page and asked to fill out the reservation form

![reservation_form](https://res.cloudinary.com/saja/image/upload/v1662209059/static/img/reservation_form_vibhlk.png)

When you have successfully reserved a table, you get a success message.

![reservation_success](https://res.cloudinary.com/saja/image/upload/v1662209892/static/img/reservation_successful_wjvw2g.png)

If you try to reserve a table thats already reserved on that date and time you get a error massage

![reservation_error](https://res.cloudinary.com/saja/image/upload/v1662209891/static/img/reservation_form_error_ap1ydy.png)


<br></br>

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


<br></br>

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

## ReservationList

![ReservationList](https://res.cloudinary.com/saja/image/upload/v1670965155/static/img/reservationlist_swgrwh.png)

## MenuList

![MenuList](https://res.cloudinary.com/saja/image/upload/v1670965155/static/img/menulist_eu0sit.png)

## Admin Reservation List

![AdminList](https://res.cloudinary.com/saja/image/upload/v1670965155/static/img/adminreservationlist_fgckoi.png)

<br>

# Deployment

This project was deployed using Heroku

* Steps for deployment:
    - Create a new Heroku App
    - Create database in heroku, using postgres
    - Link the heroku app to the repository
    - Add the needed info in config vars
    - Click Deploy
    - <a href="https://django-restaurant-1.herokuapp.com/" target="_blank">Heroku Link</a>

<br>

# Credits

* Code Institute for training.
* Various articles and youtubers for ideas. 
* Bootstrap for making templates much easier.
* Code Institute Slack and Tutoring assistance. 