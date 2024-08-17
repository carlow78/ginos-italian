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
[Back to top](#Non-dairy-Godmother)  

### Color: 
For this website, I wanted to make it visually appealing and easy for people to read being for a fictional italian restaurant, I decided to use green for the header, off-white for the main section and red for the footer. The 3 primary colors for the Italian flag. 

### Font:
For the fonts I imported 2 Google Fonts to my CSS for the title and headers "Playwrite CU", with a backup of sans-serif and for the main-font: "Nanum Gothic" with a back of sans-serif.

 
### Images:

Imagery was sourced from [Pexel](https://www.pexels.com/).  


***
[Back to top](#Ginos-Italian)  


## Features:
There are several features on this site to help users get the most out of their visit to the site.  

### General:

<details>
<summary>Header and Nav Bar:</summary>

![Header and Nav Bar](/static/images/header_nav.png)
</details>
Each page has a Header and Navigation bar section, located at the top of the page. 
The navigation bar consisted of links to a Book A Table page, a Newsletter page, a Login page, a Register page and for authorised users a My Bookings, as well as a Home button that brings the user back to the landing page. The landing page can also be reached by clicking on the restaurant logo.

&nbsp;

<details>
<summary>Footer Information:</summary>

![Opening Hours & Social Media](/static/images/footer.png)
</details> 
Each page also contains a footer element that consists of the restaurant's social media accounts (Facebook, Twitter and Instagram), as well as the opening hours for the restaurant and copyright information. 

&nbsp;

### Home page:
The *Home* page contains the header and footer as mentioned above 

<details>
<summary>Main Area:</summary>

![Main Area of Home Page](/static/images/main_area.png)
</details>
The main focus on the *Home* page is the hero image, this is an image of the restaurant with a green overlay welcoming site visitors to the website. 

&nbsp;

### Menus Page:
The next page on the site is the *Menu* page. This has all the header and footer features mentioned above.

<details>
<summary>Menu Options:</summary>

![Menus](/static/images/menus.png)
</details>
A visitor to the site can view the three menus available at the restaurant, that is, a Lunch Menu, a Dinner Menu and a Cocktails Menu. 
Each menu can be viewed by clicking on the menu name or can be downloaded for viewing at a later point. 

&nbsp;

### Book A Table Page:
Next up is the *Book A Table* page. Which has all the previously mentioned header and footer features. 

<details>
<summary>Booking Form:</summary>

![Menus](/static/images/book_a_table.png)
</details> 
Once a user has either logged into their account or created an account they will be able to view the booking form. 

&nbsp;

<details>
<summary>Date Picker:</summary>

![Menus](/static/images/date_picker.jpg)
</details>
On the booking form, the user has the option to pick the date they would like to make the bookings. This can be done by either typing the date in the date section or by clicking on the little calendar in the corner of the box and popping out the date picker. 

&nbsp;

<details>
<summary>Time Picker:</summary>

![Menus](/static/images/time_picker.jpg)
</details>
On the booking form, the user has the option to pick the time they would like to make the bookings. This is done by clicking on the dropdown menu of times and clicking on the time the user wishes to make the booking. 

&nbsp;

<details>
<summary>Location Picker:</summary>

![Menus](/static/images/location_picker.jpg)
</details>
On the booking form, the user also has the option to pick where in the restaurant they would ideally like to sit. This is done by clicking on the dropdown menu of locations and clicking on the user's peferred location. 

&nbsp;

<details>
<summary>Occasion Picker:</summary>

![Menus](/static/images/occasion_picker.jpg)
</details>
The user also has the option to provide the restaurant with a reason for making the booking, be it a birthday, night out with friends or no particular reason at all. This can be done by clicking on the dropdown menu and picking which occasion best suits the booking.    

&nbsp;

## Future Features:
Some future features I would like for this app are:
* Automated confirmation emails - that will be sent out to a user when they have made, edited or cancelled a booking
* Avoid overbookings - a backend feature that filters through all the bookings at a certain time and makes sure that the number of bookings does not exceed the number of available seats
* Dinner Club Login - where members can see the special offers that are only for members
* A Review page - this is a page where users can view reviews from previous diners but can also leave their reviews on the restaurant
* Gallery page - which would be linked to the restaurant's Instagram account 
* A shop - where users can buy vouchers, in-house wines, oils, dressings, etc

***

[Back to top](#Non-dairy-Godmother)  

## User Stories Met:
This section is to look back at the User stories we established during the strategy phase of the project. 
We are looking to see if we have met all the goals we set out. 
#### New User: 
* As a new user, I want to register so I can make a booking   
**Met on the Book a Table Page**
* As a new user, I want to book a table at Non-Dairy Godmother restaurant   
**Met on the Book a Table Page**
* As a new user, I want to pick the time, date and number of people for the booking   
**Met on the Book form on the Book a Table page**
* As a new user, I also want the option to pick the occasion and area I would like to site   
**Met on the Book form on the Book a Table page**
* As a new user, I want to be able to view menus  
**Met on the Menus page, users can view three menus for the restaurant**
* As a new user I want to be able to log in to edit or cancel my booking   
**Met on the My Bookings page once the user is logged in**
* As a new user, I want to be able to sign up for the restaurant's monthly newsletter  
**Met on the Newsletter page**

#### Returning User:
* As a returning user, I want to log in to my account  
**Met on the Log in page**
* As a returning user, I want to book a table at Non-Dairy Godmother restaurant   
**Met on the Book a Table Page**
* As a returning user, I want to view my bookings    
**Met on the My Bookings page once the user is logged in**
* As a returning user, I want to be able to edit or cancel my bookings   
**Met on the My Bookings page once the user is logged in**
* As a returning user, I want to see if the menus have been updated   
**Met on the Menus page**

***

## Testing:
Testing information can be viewed [here](/documents/TESTING.md)

***

## Bugs:
1. The styling of the base page was not consistent across all pages on the site.
      * I had not included "{% load static %}" at the beginning of my base.html page. Once this was edited, all pages loaded correctly. 
1. The booking page was not loading, the below error message was coming up:
      * After reading through the yellow error page, it showed elements of the booking model didn't exist. I realised that I had changed elements of the model without making any migrations.
<details>
<summary>Booking Page Error</summary>

![Booking Page Error](/static/images/booking_page_error.png)
</details>

1. Bookings appeared to be completed on the site but nothing was happening in the backend. 
      * One reason this wasn't working was that I had manually entered the booking form into the bookings.html file as opposed to entering it using Django's built-in features.
      * Once this was fixed I then had to add the POST function to the bookings view. 

1. When trying to add specific users the booking form loaded but throw up a ProgrammingError when the user clicked on "Book Now"
      * I had to do a bit of troubleshooting to solve this one. After spending a bit of time researching and chatting with other students on Slack it was discovered that my view for the booking form was written for the older version of the booking model and had to be updated to include the user request.
      * After making these changes a user was now able to complete the booking and was redirected to the "Thank you" page.
<details>
<summary>ID Error</summary>

![ID Error](/static/images/id_error.png)
</details>

1. After correcting the above ID error it caused another ProgrammingError when I logged into the Django admin page and clicked on the bookings tab.
      * After countless attempts to solve this error but debugging, troubleshooting and reaching out to various programming communities (including Slack) I had to eventually contact the CI tutors. 
      * There were several attempts to find the issue in the code, looking at the 'list_display' in the admin.py file and correcting errors in the models.py file neither of which solved the problem.
      * We cleared the previous migrations to create the admin page again but the tutor noticed that the Heroku Postgres database was still connected. 
      * I reset the database from inside Heroku and performed the migrations, this corrected the issue 
<details>
<summary>Admin Page Error</summary>

![Admin Page Error](/static/images/admin_page_error.png)
</details>

1. Bookings were not showing up on the "My Bookings" page.
      * In my view, I had created a variable called my_bookings and then used this as the context in my view.
      * In the my_bookings.html page, I had created a for loop to iterate through the bookings of an authorised user and display them for editing or cancelling. However, in creating this for loop I had used the wrong variable. The context in my views.py file was "my_bookings" whereas in the loop I had used "for booking in bookings" Therefore there was a context/template mismatch. 
      * Once I removed the line of code in the view.py file which included the "my_bookings" variable as it was irrelevent and changed the context to bookings (as this was the query that was filtering the user's bookings) the bookings appear on the "My Bookings" page of the site. 

1. CSS was not appearing when the site was deployed.
      * When I delpoyed the site to Heroku, the site would be built but the CSS was not appearing.
      * This was something that I could not figure out as I had changed DEBUG to False and removed DISABLE COLLECTSTATIC from the config var (as per the CI vidoes)
      * I contacted the CI tutors who were able to walk me through what I needed to do: 
            * Set the DISABLE COLLECTSTAIC again in Heroku
            * Set the DEBUG back to True and commit the changes
            * Delete all files from my Cloudinary account
            * I then had to change the DEBUG back to FALSE before removing DISABLE COLLECTSTATIC from the config vars and commit and push the changes. 
            * This then allowed Heroku to Collectstatic and added all the static files to Cloudinary
      * All the CSS then worked perfectly on the site 
1. Server 500 error coming up when trying to register a user.
      * When trying to register a new user to the site and an email address was provided a server 500 error was coming up
      * After chatting with the tutors at CI it was discovered that if an email was provided the site send a verification email with a link, but as I don't have emails set up it was causing an issue.
      * To ensure email wasn't required to verify a login the following code was put into the settings.py file:
            * ***ACCOUNT_AUTHENTICATION_METHOD = 'username'***
            * ***ACCOUNT_EMAIL_VERIFICATION = 'none'*** 
      * Setting the ACCOUNT_EMAIL_VERIFICATION to none means that the user does not need to click on a link to confirm login. 

1. PFD files not working on live site:
      * This was because of the Cloudinary account I have. When I tried to add a PDF file through Cloudinary I got the following error message:  
      ***Delivery of PDF assets is not currently permitted for this account.*** 
      * My solution to this problem was to create a seperate folder within my Django app called "documents" which housed all the relevant documentations for this project including all PDF files neede for the website and md files. 


1. During the testing stage, it was discovered that both the Newsletter form and the Book a Table form had elements of it that were not showing up as being a required field. After a quick search, I found that I needed to provide each field with a handle that checks if the field is required. I also added labels for each of these required fields, along with placeholders.  

***

[Back to top](#Non-dairy-Godmother) 

## Technologies Used:
For this project, the following technologies were used.  

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
* Google Font was used to import the chosen font for this project Lora.

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

#### Figma
* Figma was used during the structure phase of this project. It was used to create a sitemap of the website. 

#### Google Development Tools
* Google Dev Tools was used to edit code and check responsiveness before making the changes permanent.

*** 

[Back to top](#Non-dairy-Godmother)

## Validation:

* HTML:
      - No errors were found when passed through the [W3C Validator tool](https://validator.w3.org/#validate_by_input)
      - To view screenshots of validations please click [here](/documents/VALIDATION.md)

* CSS:
      - No errors were found when passed through the [W3C Validator tool](https://jigsaw.w3.org/css-validator/validator) 

* JavaScript: 
      - No costume Javascript was used in this project. The Javascript included at the end of my base.html was taken from the Code Institutes walkthrough project. 

* Python: 
      - No errors were found when passed through [PEP8 Validator](http://pep8online.com/)

***

[Back to top](#Non-dairy-Godmother)

## Accessibility:
![LightHouse Report](/static/images/lighthouse_report.png)

***

## Deployment:
Deployment information can be found [here](/documents/DEPLOYMENT.md)

***

## Credits:
* The initial setup of the Django project was done following the Code Institutes walkthrough project.  


## Acknowledgements:
* I would like to thank Brian O’Hare for being my mentor for this project.
* I would like to thank Ed from tutor support.
* I would like to thank Ger from tutor support.
* I would like to thank the Slack community for all their support and encouragement during this and all my projects. 

*** 
[Back to top](#Non-dairy-Godmother) 