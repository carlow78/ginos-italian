# Ginos Italian: 

This website is designed for a fictional Italian restaurant based in Carlow, Ireland. 

The website has been created as the Fourth Milestone project for Code Institute's Diploma in Full Stack Software Development (E-commerce Applications).  Gitpod was used to write code and to add, commit and push changes/updates to the project's Github repository. Heroku was used to deploy the website.


### View the live website [here](https://ginos-italian-9732d83f0d42.herokuapp.com/)
![Live Website](/static/images/readme/main-page.jpg)

***
## Table of content: 
 1. [Site Goals](#Site-Goals)
 1. [User Experience UX](#user-experience-ux)
      1. [User Stories](#User-Stories)
      1. [Development Plan](#Development-Plan)
            * [Scope](#Scope)
            * [Structure](#Structure)
            * [Skeleton](#Skeleton)
            * [Surface](#Surface)
      1. [Color](#Color)
      1. [Font](#Font)
      1. [Images](#Images)
 1. [Features](#Features)
 1. [Testing](#Testing)
 1. [User Stories Met](#User-Stories-Met)
 1. [Bugs](#Bugs)
 1. [Technologies Used](#Technologies-Used)
 1. [Validation](#Validation)
 1. [Accessibility](#Accessibility)
 1. [Deployment](#Deployment)
 1. [Credits](#Credits)
 1. [Acknowledgements](#Acknowledgements)

***
 
## Site Goals:

The primary goals for this site are as follows:
* Allow users to make a booking at the restaurant
* Allow users to edit or cancel their booking
* Allow users to view the menu of whats on offer at the restaurant with prices etc.


## User Experience UX:

### User stories:
Github was used to define an Agile approach for this project, A User Story template was created for the project. GitHub issues was then used to create the user stories using the newly created custom template for this project. A Kanban board was used to record all the user stories. All issues were assigned to me as the website developer. All issues were moved from 'To Do' to 'In Progress' to  'Done' as the project progressed.


***

#### New User:  
* As a new user, I want to register so I can make a booking 
* As a new user, I want to book a table at the restaurant
* As a new user, I want to pick the time, date and number of people for the booking
* As a new user, I want to be able to view menu
* As a new user, I want to be able to log in to edit or cancel my booking 

#### Returning User:
* As a returning user, I want to log in to my account
* As a returning user, I want to book a table at the restaurant
* As a returning user, I want to view all my bookings
* As a returning user, I want to be able to edit or cancel my bookings 
* As a returning user, I want to see if the menu have been updated

## Development Plan:
Developers must consider every aspect of the website and the way users will interact with it in order to produce user-friendly, comprehensive websites. Every user story that has been described in the sections above must be taken into account.  


#### The primary goals for a user to achieve using this website is to
* Make a booking
* Log into their account 
* Edit a booking
* Cancel a booking 

#### The website needs to allow the restaurant owner to:  

* Track bookings that are coming into the restaurant 
* Manage the number of people per table via the booking model    

## Scope:  

With the structure in place, it was then time to move onto the scope plane. This was all about developing website requirements based on the goals set out in the strategy plane. These requirements are broken down into two categories. 

### Content Requirements:
1. The user will be looking for:
      * Location of the restaurant
      * Menus 
      * Opening Times

### Functionality Requirements:
1. The user will be able to:
      * Book a table at a certain time and date
      * Choose the number of people for the booking 
      * Edit bookings 
      * Cancel bookings 

***

## Structure:

The information above was then used to create a structure for the website. Below is a site map showing how users can navigate the website. Sitemap created using [Gloomaps](https://www.gloomaps.com/).
<details>
<summary>Sitemap</summary>

![Sitemap](/static/images/readme/site-structure.jpg)
</details>


## Skeleton:
[Wireframes](/static/documents/WIREFRAMES.md) were created to set out the initial appearance of the website. The wireframes were created using [Balsamiq](https://balsamiq.com/).  

## Surface:
[Please see the live site here](https://ginos-italian-9732d83f0d42.herokuapp.com/)  

***
[Back to top](#Ginos-Italian)  

### Color: 
For this website, I wanted to make it visually appealing and easy for people to read being for a fictional italian restaurant, I decided to use green for the header, off-white for the main section and red for the footer. The 3 primary colors for the Italian flag. 

### Font:
For the fonts I imported 2 Google Fonts to my CSS for the title and headers "Playwrite CU", with a backup of sans-serif and for the main-font: "Nanum Gothic" with a back of sans-serif.

 
### Images:

Imagery was sourced from [Pexel](https://www.pexels.com/).  


***
[Back to top](#Ginos-Italian)  


## Features:
The website consists of the following features: 

### General:

<details>
<summary>Header and Nav Bar: New User & Logged In User</summary>

![Header and Nav Bar - New User](/static//images/readme/ginos-header.jpg)
![Header and Nav Bar - Logged User](/static//images/readme/ginos-header-logged-in.jpg)
</details>
Each page has a Header and Navigation bar section, located at the top of the page. 
The navigation bar consisted of links to a Make a Reservation page, a Login page, a Register page and for authorised users a Manage Bookings, as well as a Home button that brings the user back to the index page. The landing page can also be reached by clicking on the restaurant title in the top left corner.

&nbsp;

<details>
<summary>Footer Information:</summary>

![Opening Hours & Social Media](/static/images/readme/gino-footer.jpg)
</details> 
Each page contains a footer section which contains a About Us paragraph, a Contact Us section with details about how to get in touch with the restaurant and finally a Social Media with links to the restaurant social media sources (all these links open in a new tab - better UX design).

&nbsp;

### Home page:
The *Home* page contains the header and footer as mentioned above. 

<details>
<summary>Main Area:</summary>

![Main Area of Home Page](/static/images/readme/ginos-main-area.jpg)
</details>
The main focus on the *Home* page is the hero image, this is an image of fresh Italian food ingredients.


### Menu Page:
The next page on the site is the *Menu* page. This has all the header and footer features mentioned above.

<details>
<summary>Menu Option:</summary>

![Menu](/static/images/readme/ginos-menu.jpg)
</details>
This page is very simplistic it contains a image of plate of pasta in the background and a "View our menu" link to the restaurants specials menu. The menu was created using a <i>Canva</i> free template.

&nbsp;

### Make a Reservation Page:
Next there is the *Make a Reservation* page. Which has all the previously mentioned header and footer features. 

<details>
<summary>Booking Form:</summary>

![Add-Reservation](/static/images/readme/ginos-add-reservation.jpg)
</details> 
Once a user has either logged into their account or created an account they will be able to view the booking form. 

&nbsp;

<details>
<summary>Date Picker:</summary>

![Date-Picker](/static/images/readme/gino-date-picker.jpg)
</details>
On the booking form, the user has the option to pick the date they would like to make the bookings. This can be done by either typing the date in the date section or by clicking on the little calendar in the corner of the box and popping out the date picker calendar. They will receive a red error message if they try and book a date in the past.

&nbsp;

<b>Number of People and Time Dropdowns:</b>

The booking form features two drop-down menu. A Number of people and Time drop-down menu. Number of people (options 1 to 8) Time (options 12:00pm to 9:00pm) the times the restaurant is opened.

&nbsp;

<b>Text fields (Booking Name, Telephone Number, and Additional Comments):</b>

<u>1. Booking Name</u>

This is required field and must be filled in.


<u>2. Telephone Number</u>

This is required field and must only contain digits. The minimum digits required are 10 and maximum of 15 digits.

<u>3. Additional Comments</u>

This is not a required field. Its purpose is the user wants to ask further questions.



## Future Features:
Some future features I would like for this app are:
* Automated confirmation emails - that will be sent out to a user when they have made, edited or cancelled a booking
* Avoid overbookings - a backend feature that filters through all the bookings at a certain time and makes sure that the number of bookings does not exceed the number of available seats
* A Review page - this is a page where users can view reviews from previous patrons and can also leave their reviews on the restaurant
* A ordering page where users can order food from the restaurant
***

[Back to top](#Ginos-Italian)  

## User Stories Met:
This section is to look back at the User stories established during the planning of the project
 
#### New User: 
* As a new user, I want to register so I can make a reservation 
**Met on the Make a Reservation Page**
* As a new user, I want to book a table at thr restaurant   
**Met on Add Booking Page**
* As a new user, I want to pick the time, date and number of people for the booking      
**Met on the Booking form on Add Booking page**
* As a new user, I want to be able to view menu  
**Met on the Menu page, users can view the main menu for the restaurant**
* As a new user I want to be able to log in to edit or cancel my booking   
**Met on the Edit reservation page once the user is logged in**


#### Returning User:
* As a returning user, I want to log in to my account  
**Met on the Log in page**
* As a returning user, I want to book a table at the restaurant   
**Met on the Make a Reservation Page**
* As a returning user, I want to view my bookings    
**Met on the Manage Booking page once the user is logged in**
* As a returning user, I want to be able to edit or cancel my bookings   
**Met on the Edit resevation page once the user is logged in**


***

## Testing:
Testing information can be viewed [here](/static/documents/TESTING.md)

***

## Bugs:

<u>Heroku Gunicorn install error:</u>

When I first tried to deploy the website to Heroku it was failing after using <i>web: gunicorn reservationsystem.wsgi</i>

Gunicorn install issue thankfully a post in Slack resolved the issue. My settings.py was located in the main folder. 

![Gunicorn Issue](/static/images/readme/gunicorn-fix.png) 

<u>CSS not appearing in Heroku</u>

When I deployed the site to Heroku, no CSS was appearing and in Devtools a 404 not found was appearing for the base.css file.
      

After googling the issue I found the solution from this 
[Stack Overflow post](https://stackoverflow.com/questions/28961177/heroku-static-files-not-loading-django)  and then remembered I had run the code previously during the I Think I Blog walkthrough project.

Once I ran a <b>python manage.py collectstatic</b> committed my changes and attempted a redeploy all the CSS then worked perfectly on the site.

<u>Booking ID Primary Key Issue - Unresolved Bug</u>

During my final 3rd Mentor 1to1 with my Mentor Precious. He pointed out that edit/ or delete (bookingID) ideally should not be appearing for a user in the URL as a security concern and bad UX. I did try experimenting to try to resolve the issue but time was against me after illness. Its something I hope to resolve in the future and to deploy my project sooner for my mentor to review. 


***

[Back to top](#Ginos-Italian) 

## Technologies Used:
For this project, the following technologies were used:  

### Languages:
* HTML
* CSS
* Python
* Javascript
 

### Frameworks, Libraries, Programs & Applications Used:
* Django
* PostgreSQL
* Bootstrap

#### Google Font
* Google Font was used to import the two chosen fonts for this project for the headers and title: "Playwrite CU", and for the main-font: "Nanum Gothic", sans-serif was used as the backup for both fonts.

#### Font Awesome
* Font Awesome was used on each page of the website to provide icons for UX purposes.  

#### GitPod
* GitPod was used for writing all the code for this project. It was also used to commit and push to GitHub.  

#### GitHub 
* GitHub was used to store this project.

#### Heroku
* Heroku was used to deploy the project.

#### Cloudinary
* Cloudinary was used to store some of the images used in this project

#### Balsamiq 
* Balsamiq was used to draw initial Wireframes for this project.

#### Gloomap
* Gloomap was used to create a sitemap of the website. 

#### Google Development Tools
* Google Dev Tools was used to edit code and check responsiveness

### Windows Photo Editor and Convertio.io
* Windows Photo Editor was used to save Pexel *.PNG files as *.JPG afterwards each file was converted to *.WEBP using Convertio.io online conversion tool. Images were then uploaded to Cloudinary.

*** 

[Back to top](#Ginos-Italian)

## Validation:

* HTML:
      - No errors were found when passed through the [W3C Validator tool](https://validator.w3.org/#validate_by_input)
      - To view screenshots of validations please click [here](/static/documents/VALIDATION.md)

* CSS:
      - No errors were found when passed through the [W3C Validator tool](https://jigsaw.w3.org/css-validator/validator) 

* JavaScript: 
      - Very little Javascript was used in this project. Apart from the autohide messages added at the bottom of base.html. This code was passed using [JShint](https://jshint.com/.)

* Python: 
      - No errors were found when passed through [PEP8 Validator](http://pep8online.com/)

***

[Back to top](#Ginos-Italian)

## Accessibility:
![LightHouse Report (Index)](/static/images/readme/lighthouse-index.jpg)
![Lighthouse Report (Menu)](/static/images/readme/lighthouse-menu.jpg)

***

## Deployment:
Deployment information can be found [here](/documents/DEPLOYMENT.md)



## Credits:
The initial setup of the Django project was done following Code Institute's Alumi now Mentor - Daisy McGirr (Slack @Daisy Mc) [Youtube](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy) Recipe Sharing Django Project series.  Thanks to Slack @Amy_CI for sharing.

And to CI past student Martina Martin (Martiless) for her [Non-Dairy Godmother PP4 project](https://github.com/Martiless/nondairy-godmother) which made developing my project a lot easier due to the similarities of our projects and for the [Readme](https://github.com/Martiless/nondairy-godmother/blob/main/README.md) and testing templates.


## Acknowledgements:
* I would like to thank Precious Ijege for being my mentor for this project.
* I would like to thank the Slack, Stack Overflow community.

*** 
[Back to top](#Ginos-Italian) 