# Indian Fantastic

## Nav Bar

The navbar is easy to navigate, and features all three pages and the sign up, sign in and logout if you're logged in. And the navbar is full responsive. The navbar is alike on all the pages.

![nav_bar](https://res.cloudinary.com/saja/image/upload/v1662210575/static/img/nav_bar_pn4zur.png)



## Footer

* The footer includes: 
    - links to our social page, with included _blank to avoid the users leaving our page.
    - Location of the restaurant, with country, city and local address
    - Opening hours
    - Contact information

    - ![footer](https://res.cloudinary.com/saja/image/upload/v1662212651/static/img/footer_vyugok.png)



## Landing Page

The landing page for the restaurant will show you some welcoming text, opening hours and easy navigation to the menu with special dishes and the reservation page. 

![Welcome_text](https://res.cloudinary.com/saja/image/upload/v1662208140/static/img/welcome_ruybsa.png)



## Menu page

The menu page has a list of the restaurants special dishes.

![Menu](https://res.cloudinary.com/saja/image/upload/v1662208334/static/img/menu.page_zb7abp.png)




## Reservation Page

To access the reservation page you have to login. If you're not logged in, and you click the reservation page you will be sent to a sign in page. 

![Sign_in](https://res.cloudinary.com/saja/image/upload/v1662209060/static/img/sign_in_qiiut9.png)

After you have signed in, you will be welcomed with your username on the reservation page and asked to fill out the reservation form

![reservation_form](https://res.cloudinary.com/saja/image/upload/v1662209059/static/img/reservation_form_vibhlk.png)

When you have successfully reserved a table, you get a success message.

![reservation_success](https://res.cloudinary.com/saja/image/upload/v1662209892/static/img/reservation_successful_wjvw2g.png)

If you try to reserve a table thats already reserved on that date and time you get a error massage

![reservation_error](https://res.cloudinary.com/saja/image/upload/v1662209891/static/img/reservation_form_error_ap1ydy.png)




## Sign Up Page

The sign up page has some welcoming text and asks for:
- Username
- Email
- Password and repeat the password again

![sign_up](https://res.cloudinary.com/saja/image/upload/v1662213001/static/img/Sign_up_yqbcrp.png)





# Admin Page Features 

## Admin Menu Page

The owner of the page can easly edit the menu page through the admin menu page. With deleting current menu's or add more / add new menu's to the page

![Menu_admin](https://res.cloudinary.com/saja/image/upload/v1662208564/static/img/menu_admin_zwahi3.png)

* To add a menu just click "+ Add" or "Add Menu +" in the top right corner and fill out the info thats needed.
* To delete a menu, just select which menu you would like to delete left of the name, and choose "Deleted selected Menus" in Action: and press "Go".
* This will add or delete a menu in the menu page



## Reservation Admin Page

When the reservation has been sent successfully, the owner of the page can easly see the reservation in the admin page with: Username, phone number, number of guests, date, time and seats.
Currently the reservations gets auto approved.

![reservation_admin](https://res.cloudinary.com/saja/image/upload/v1662210222/static/img/reservation_complete_jdfzia.png)



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




# Testing


## Validator Testing

* HTML
    - No errors returned when passing through <a href="https://validator.w3.org/" target="_blank">HTML Validator</a>, except the django text.
* CSS
    - No errors returned when passing through <a href="https://jigsaw.w3.org/css-validator/validator" target="_blank">CSS Validator</a>.



## Reservation Form Testing

* Variations of testing:
    - Testing to reserve on the same date, time and table. Testing with multiple users. Making sure it gives an error when trying to reserve an occupied table on the same time and date. 
    - Testing to try to reserve without filling out all the whole form.
    - Testing the access without login in.
    - Testing that the info from the user that reserves the table always comes in the admin page.



## Menu Form Testing

* Variations of testing:
    - Testing to delete menu and see if it gets deleted in the menu page.
    - Testing to add more menu's and see if it gets added in the menu page.



## Testing Buttons

* Testing that all the nav buttons, reservation form button, nav buttons and footer button works.


## Sign in / Sign out

* Testing that login, logout etc works without any issues



## Testing On Multiple Devices

* Testing the web page on different devices with no issues. The webpage is responsive from desktop, to small mobile phones and tablets. 
* For some reason <a href="https://ui.dev/amiresponsive" target="_blank">amIresponsive</a> won't load my web page. But tested the webpage with using the toggle device toolbar option available in the developer tools in Chrome. And also loaded the page on my physical phone and ipad to make sure it loaded. 


## Unfixed bugs

* Currently no known bugs


# Deployment

This project was deployed using Heroku

* Steps for deployment:
    - Create a new Heroku App
    - Create database in heroku, using postgres
    - Link the heroku app to the repository
    - Add the needed info in config vars
    - Click Deploy
    - <a href="https://django-restaurant-1.herokuapp.com/" target="_blank">Heroku Link</a>


# Credits

* Code Institute for training.
* Various articles and youtubers for ideas. 
* Bootstrap for making templates much easier.