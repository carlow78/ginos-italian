## Testing of Ginos Italian website: 

## Table of content: 
 1. [Manual Testing](#manual-test)
    1. [General](#General)
    1. [Navbar and Footer Links](#navbar-and-footer-links)
    1. [Menu Page](#menu-page)
    1. [Register](#register)
    1. [Login](#log-in)
    1. [Add Booking](#add-booking)
    1. [Booking Success](#booking-success)
    1. [Manage Booking](#manage-booking)
    1. [Delete Reservation](#delete-reservation)
    1. [Other User Delete/Edit Attempt](#other-user-deleteedit-attempt)
 1. [Automated Testing](#automated-test)
 1. [JavaScript Testing](#javascript-testing)
 


## Manual Test:

### General:
The website pages were tested using Google chrome devtools. To see how they functioned on various screen sizes. Testing was also performed on personal owned android(OnePlus Nord 3)and iPad 6 (2018) devices. With Bootstrap being installed this made writing less css code for smaller media screens - such as tablets and mobile. 

### Navbar and Footer Links: 
On each page there is a navigation bar and a footer that needs to be tested, the following checks were made: 
* By clicking on the resturant title the home page was displayed across all pages
* By clicking on each of the tabs in the navbar you are redirected to the right page
* All social media links worked correctly, opening the social network website on a new tab

***

### Menu page:
On the menu page the user can click on the "View our menu" which opens the menu for the restauranted hosted on Cloudinary. 
* The menu link, once clicked on, opens up correctly and on a new tab

### Register (Sign Up):
The Register page has a form for the user to fill out.
* The first test on the Register page was to check if the link to the "Register" page at the top of the form works. Clicking on this link will bring the user straight to the Login Page. 
* Click on the 'Submit' button without entering any details, this will cause an error message to appear staing ***"Please fill out this field"***. This message will appear each time the user tries to submit the form without filling in the required fields. 
* If the user tried to create a password that is too easy or similar to username/email or too common they will not be able to proceed and will get all or some of the following messages: 
    * This password is too short. 
    * It must contain at least 8 characters.
    * This password is too common.
    * This password is entirely numeric.
* Once the user has filled out all the required fields and created a strong enough password, they can then click the submit button. This will redirected them back to the home page where a message will pop up "Successfully signed in as 'Username"
During testing of the Register page, it was noted that when the password messages appeared the submit button was moved outside the container box, this was a quick css fix, changing the height of the box from a certain number of pixels to auto. 


### Log In:
The Log in page is a simple test, there was just two elements on the page that needs to be tested. These checks are as follows:
* Try clicking on the 'Submit' button without entering any details in the log in form, this will cause an error message to appear staing ***"Please fill out this field"***. This message will appear each time the user tries to submit the form without filling out any of the fields in the form. 
* If the user attempts to log in with an incorrect username or password they will get the following message ***"The username and/or password you specified are not correct."***
* Once the user has enter the correct username and password they now have the option to tick the 'remember me' box which will keep them logged in on their browser. 
* Clicking on the 'Log In' button redirects the user back to the home page.


### Add Booking:

Contains 6 elements on it
1. Booking Name
1. Email Address
1. Contact Number
1. Number of People
1. Date
1. Time
1. Additional comments

These elements need to be filled out before the user can make a booking, the checks for this page are as follows:
* Try clicking on the 'Submit' button without entering any details in the log in form, this will cause an error message to appear staing ***"Please fill out this field"***. This message will appear each time the user tries to submit the form without filling out any of the fields in the form. 
* Selecting a date is done using the calender widget. Click on the calendar icon on the right and select a date. If the user chooses past date they will receive an error message - "The reservation date cannot be in the past."
* Number of People and Time, are all selected using the dropdown menu, this is done but clicking on the arrow and choosing the option that best suits the booking. If the user attempts to make a booking without making one of these choices they will receive the following message ***"Please select an item in the list"***

The below screenshot displays what happens when the user clicks on "Add Booking" button with invalid input. The form will only be submitted when all valid information is entered by the user.

![Add Booking](/static/images/testing/testing-add-booking.jpg)

### Booking Success

When the user submits valid information they are brought to the Booking Success page which thanks them for the booking. A brief message appears for 2 seconds "Booking added successfully." and then disappears. This reservation is now in the database and can be viewed by the user when they click on the "Manage Booking" header link.

![Booking Success](/static/images/testing/testing-booking-success.jpg)


### Manage Booking:
The Manage Booking page is a page where all the bookings from the user will appear in the order of their most recent bookings. From there the user has the option to Edit a reservation or to delete a reservation.   
The checks for My Bookings are as follows:
* When a user clicks on the 'Edit Reservation' button they are redirected to the Edit Booking page, where they can make adjustments to their booking.

Test performed was to reduce amount of people from 5 to 4 people. Click on "Update Booking" button and to confirm that booking was updated to 4 people on the "Manage Booking" webpage.

<b>Before</b>

![Manage Booking(Before)](/static/images/testing/testing-manage-booking.jpg)

<b>After</b>

![Edit Booking](/static/images/testing/testing-edit-reservation.jpg)

![Manage Booking(After)](/static/images/testing/testing-manage-booking-after.jpg)

## Delete Reservation

* When a user clicks on the 'Delete Reservation' button they are redirected to the Delete reservation page to 'confirm deletion' and when then they do they are returned to the home page, where they get a message pop up stating ***"Booking deleted successfully."***

![Delete Reservation](/static/images/testing/testing-delete-reservation.jpg)

When the test user created returned to their "Manage Booking" page there was no bookings after they deleted their only existing reservation.

![Return to Manage Booking](/static/images/testing/testing-deletion-result.jpg)

***

## Other User Delete/Edit Attempt

Test user (username = tester) trying to alter test user (TomDunne's) reservation

For this scenario I created another reservation using the test user (TomDunne's) account and using the url I tried to edit and delete booking id 59. Thankfully has hoped this was not possible and tester was given a 404 page not found error.

Booking ID = 59


![Non-user deletion attempt](/static/images/testing/non-user-edit-delete.jpg)

Ideally I would prefer the edit id number to not be visible (primarily for security reason) I did try to implement other solutions (slug and uuid) but unfortunately I had to revert back to the working model. 


## Automated Test:
Automated testing was attempted using the test.py file located in reservationsystem app. The goal was to test the functionality of using the main views of the reservation app. Adding a user, then adding, editing, and deleting a reservation by the created test user. 
To view the automated testing attempt please go to [test.py](reservationsystem/test.py)
For testing the view I created 6 automated tests. The main test point was to try and to test the CRUD functionality. 

The main issue I encountered was "AssertionError: 200 != 302" for 3 of my test cases when I changed 200 (status ok code) for 302 (temporary redirect code) as recommended in the terminal feedback. All tests passed. Unfortunately, due time constraints I had to rely on manual testing (which I was going to do anyway) I intend to looking into this issue at a later date to understand why 302 is working and 200 (the code I hoped and expected to see).

When I performed the automated tests I used the default sqllite database as recommended by the Code Institute Django walkthrough I Think I Blog project.

![Automated Testing (200)](/static/images/testing/testing-200-error.jpg)

!![Automated Testing (Fixed)](/static/images/testing/testing-200-fix.jpg)

***

## JavaScript Test

Very little Javascript was written personally for this project the only JavaScript deployed was to automatically hide the bootstrap user messages after 2 seconds before this the user had to click on the x button to close the message which is bad User UX. This script is located at the bottom of the base.html web page. Other messages include when the user add/edit/delete reservations.

![JavaScript Test](/static/images/testing/test-message-without-autohide-script.jpg)


[Back to Top of Testing](#testing-of-ginos-italian-website)     
[Back to README](/README.md)

