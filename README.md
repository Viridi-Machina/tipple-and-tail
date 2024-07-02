![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/2568106f-af67-4a0a-a8d4-8e2a64867440)


# Tipple & Tail
## By Jacen Green

## Summary
Tipple & Tail is a small fictional late-night bar that that also hosts various musical events. Due to it's recent surge in popularity, they have outsourced work to a full-stack developer to create a website and booking system that will help them manage their increasing demands. The app is booking-management system that allows users to efficiently make bookings, check out various events being hosted and review any current reservations that have been made - giving aaccess to update or cancel if they require.

A live link to the deployed app can be visited [here](https://tipple-and-tail-7dca6c4d30d7.herokuapp.com/).

## Process

**Problem Statement**
> You have a client who needs a website with booking functionality that allows their customers to create customizable bookings with various packages that the client wishes to promote.

📑 **Research**
<details>
 <summary> See detail</summary>

With limited time to complete the project; data model, user story and wireframe planning have taken priority. However, core inspiration has been taken from the [Slug & Lettuce](https://www.slugandlettuce.co.uk/market-square-nottingham/party-booking) booking page:

![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/50b968e6-e6a5-4aee-94c5-df4ea8b9d044)

- First fields used are party-size and date.
- Calendar widget for quickly selecting a date.
- Drop-down list with booking package-options.
- Selected fields then filter available time slots

These elements would make up the core booking form process, with further additions such as table choice being implemented.
</details>

💠 **Design**
<details>
 <summary> Wireframes</summary>
 
 ### Low fidelity wireframing -> Balsamiq
 After initial research, including the creation of all user stories at ground zero, low fidelity wireframes were created using Balsamiq to touch upon all aspects of the user story needs.
 <br>
 <br>
 <br>
 <br>

 **Home Page:**
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/00136a7b-f9cd-4903-bcad-ddc555960b53)
 The initial thought process was to create a clean looking and open home screen, with minimal elements on the screen and a focus on stlye - the goal being to induce a sense of freedom when navigating the site.
 Two main elements appear here; a booking and a menu link -> found to be two of the most common first choices when choosing to book at a new bar or restaurant.
 This hom page would be a vertically scrolling home page that spans across the two following sections:
 <br>
 <br>
 <br>
 <br>

 **About section (home page)**
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/8826d175-1e29-45a5-ae51-3c8825846d03)
 Scrolling down to the next section brings you to the about section which pulls from an about model which the admin can update at will.
 Additionally there is a google maps API, booking times as well as a link to the *events* page which is also present in the navbar.
 <br>
 <br>
 <br>
 <br>

 **Contact and Enquiries section (home page)**
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/d2da15c3-cbea-415b-8b4c-16f8124d023b)
 The final section of the home page shows a contact form (from the same about view) giving instructions on how to make a general enquiry either by submitting a form or calling the bar's phone.
 <br>
 <br>
 <br>
 <br>

 **Bookings Pages:**
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/df2a8fe8-cf35-4e17-99d6-cd122d84aad3)
 <br>
 <br>
 <br>
 <br>
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/67f0bc80-79ab-4ca8-a259-9aec5e10343a)
 <br>
 <br>
 <br>
 <br>
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/02390635-a97b-44b8-87fc-b460ba71198e)
 <br>
 <br>
 <br>
 <br>
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/cd2667ef-61f7-4ae7-a7f7-de93b071667c)
 <br>
 <br>
 <br>
 <br>
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/b97949cd-030a-4ed2-90c5-7d1161321aad)
 <br>
 <br>
 <br>
 <br>
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/e74ecc8f-4e67-41b8-8f80-279bb1b1b8af)
 <br>
 <br>
 <br>
 <br>
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/eea3e874-f68b-417e-8ab9-6e39a8ea9ce7)
 <br>
 <br>
 <br>
 <br>
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/ba26e650-867f-41f0-8396-819bf41727c2)
 <br>
 <br>
 <br>
 <br>
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/d81d3f4e-61ca-4d44-86e9-b6065bd18c1b)
 <br>
 <br>
 <br>
 <br>
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/8ffad8ab-1993-4610-ad23-bfcd2407d797)
 <br>
 <br>
 <br>
 <br>
 **Events Pages with detail views**
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/ac3bbd07-7cd8-46e4-b907-f7977bcce4e4)
 <br>
 <br>
 <br>
 <br>
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/53a893c2-9118-452e-bd9f-53501198e518)
 <br>
 <br>
 <br>
 <br>
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/c54c72e9-67e6-4e9f-b4ee-609c6dff4826)
 <br>
 <br>
 <br>
 <br>
 **Lastly, login authentication templates**
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/709d8e75-d3f5-4157-a548-ed3475dcf786)
 <br>
 <br>
 <br>
 <br>
 ![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/99238658-4d1f-4353-a2b3-26a680c68674)
 <br>
 <br>
 <br>
 <br>

 I would only later realise just how ambitious of a project I was creating for myself, majorly overcomplicating all aspects of the site.
 Thus time was massively cut short during this project from hours of bug fixing just to get simple models in place.

</details>

## Themes

![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/baf36a9e-0af3-45af-9f35-d984193ca2c4)
<br>
<br>
The general colour palette for the site was picked at custom - drawing from the themes of freedom, excitement and fun.
Colours of bright yellow gold, purple and blues would become signature; and with nightclub atmospheres in mind this research led to 
a glow effect being applied onto dark grey slate backgrounds to achieve an exciting neon-theme.

With regards to font and general CSS styling Tailwind was used to a large degree to help speed up the process of a truly custom feeling design, 
albeit still time consuming. I had heard about the positives of using Tailwind and personally was against bootstrap's simplified and template-based design.


💠 **Development**

User Stories:
<details>
 <summary>🔵 See User Stories (User) 🔍</summary>
 
- [US-U01] 🔵 As a user, I want to view availability based on the selected date and party size,<br>
  so that I can view available booking options.
  
- [US-U02] 🔵 As a user, I want to view a table plan of available tables,<br>
  so that I can choose where to sit.
  
- [US-U03] 🔵 As a user, I want to see a list of available packages that I can add to my booking,<br>
  so that I can customize my experience.
  
- [US-U04] 🔵 As a user, I want to review booking details before finalising the booking,<br>
  so that I can check that everything is correct.
  
- [US-U05] 🔵 As a user, I want to provide personal details during the booking process,<br>
  so that I can recieve confirmation via email.
  
- [US-U06] 🔵 As a user, I want to see an about page,<br>
  so that I can learn more about the establisment before booking.
  
- [US-U07] 🔵 As a user, I want to view a drinks menu,<br>
  so I can see what options are available before making a booking.
  
- [US-U08] 🔵 As a user, I want to be able to declare allergies when making a booking,<br>
  so that the establishment is aware before arrival.
  
- [US-U09] 🔵 As a user, I want to see a map,<br>
  so that I can see how far the establishment is from my current location.
  
- [US-U10] 🔵 As a user, I want to see confirmation of a successful booking,<br>
  so that I have confidence a booking has been made.
  
- [US-U11] 🔵 As a user, I want to be able to edit a booking after it has been made,<br>
  so that I can cancel or view my booking.
  
- [US-U12] 🔵 As a user, I want to review and leave comments on events that I have been to,<br>
  so I can share my experience with others.

- [US-U13] 🔵 As a user, I want to send enquiries to the establishment, <br>
  so I can ask further questions or enquire about larger bookings.
</details>

<details>
 <summary> 🟣 See User Stories (Admin) 🔍</summary>
 
- [US-A01] 🟣 As an admin, I want to view and update details of a specific booking,<br>
  so that I can handle enquiries and make changes.
  
- [US-A01] 🟣 As an admin, I want to manage user accounts,<br>
  so I can maintain control over user access and disable accounts if necessary.
  
- [US-A01] 🟣 As an admin, I want to log in to a a secure admin panel,<br>
  so that I can access the site's administrative features.
  
- [US-A01] 🟣 As an admin, I want to manage the about page,<br>
  so I can ensure it remains up to date.
  
- [US-A01] 🟣 As an admin, I want to manage the events page,<br>
  so I can add new events and moderate customer reviews.
  
- [US-A01] 🟣 As an admin, I want to manage the menu page,<br>
  so that I can add/remove or update menu items and pictures.
  
- [US-A01] 🟣 As an admin, I want to tag certain booking packages,<br>
  so that I can upsell and make them more appealing.
</details>

MOSCOW model in use for user stories.
![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/847130a5-90e0-4ef6-b197-13da0c67ece6)
Following agile methodology a great deal of time was spent setting up the project kanban and other various boards where the project could be visualised.
Each user story was given 1-4 acceptance criteria and each given story point scores as well as their own respective tasks

![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/00a298ee-bb29-40b7-8315-21a441dcd28a)

![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/2939992a-139a-426e-9f46-405e4319df20)


💠 **Data Models**
<details>
 <summary> See detail</summary>
The data models created for this project are displayed in the image below:<br>
<br>
 
![image](https://github.com/Viridi-Machina/tipple-and-tail/assets/146846939/32bd5dc3-416c-47c0-a5be-0e69152fd14d)

<br>

The data models can be divided into 3 main apps to separate functionality:<br>
🔷 **User App**: This app handles user accounts as well as their enquiries and comments made to event posts.<br>
🔹 `User` - This model represents any user account, containing their name, email adress, mobile number, bookings and account status.<br>
🔹 `Enquiry` - This model represents enquiries made by the user, containing messages submitted to the site admin.<br>
🔹 `Comment` - This model represents comments made by the user on posted events, requiring approval by an admin.<br>
<br>
After discussing with my mentor it would become apparent that creating a custom user model was massively overcomplicating things, and a default user model was then used.

🟣 **About App**: This app handles the about and event models, both handled by the site admin.<br>
🔺 `About` - This model represents an about page, filled out and updated byu the site admin.<br>
🔺 `Event` - This model represents an events page, a psuedo blog-post view which displays events that can link to bookings.<br>
<br>

🔶 **Booking App**: This app handles the booking process; filtering available tables, timeslots and booking packages.<br>
🔸`Booking` - This model represents the core booking process, storing all associated fields.<br>
🔸`Table` - This model stores a small number of tables with unique table numbers and capacity which can be updated by an admin.<br>
🔸`TimeSlot` - This model represents the chosen time slot to be applied to the booking and table.<br>
🔸`TableSlot` - This model represents the specific tables with a chosen TimeSlot and TableSlot.<br>
🔸`Package` - This model represents additional extras for booking customization, which are also used to tag bookings.<br>
<br>
After speaking with my mentor the booking model was also overcomplicated, and in need of large changes to the model which had already been migrated, whilst removing
some unneccesary models such as TimeSlot and TableSlot and compressing them into the one Table model.


</details>

## Features
**CRUD Functionality**

**Authentication & Authorisation**

**Future Feature Implementation**
- Completion of the Event model, linked to a event detail view which also provides user interactions through leaving comments on events.
- Completion of the Enquiry form on the home page - which had to be cut from development - as the main booking system took priority and
- turned out to be rather complicated to get a grasp of.
- Menu feature in about section as well as opening times being displayed for users.
- 

## Roadmap

## Bugs

## Technologies Used
**Core Development**

**Libraries, Frameworks and Packages

**Python/Django Packages**

**Infrastructure**

## Testing
**Automated**

**Manual**
- Significant ammounts of manual testing was spent on checking form validations, error displays, invalid form submissions with booking pages and general bugfixing with the booking model view as a whole.
- ~20hrs spent on manual repeat testing, mainly with the booking forms and views.

**Genral**

**Authorisation**

**Lighthouse**

**Responsiveness**
ResponsivelyApp

**Code Validation**
W3C Markup Validation Service
JSHint
PEP8

All of the above validations were passed:
- All custom python files met pep8 criteria
- No javascript was used in the project
- All html source code checked for and found zero errors at this stage of deployment.

## Deployment
**Heroku Deployment**
<details>
 <summary>Method :purple_circle:</summary>

- From the dashboard you will be able to see your deployed projects. Click on `New`, then `Create new app`:
  <details>
    <summary>Dashboard :mag:</summary>
    
    ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/d4468782-45f9-4c26-8369-1ddffee2b408)
  </details>

- Enter a unique `App name` and `Choose a region`, then click `Create app`.<br>
  Once created navigate to the `Settings` menu.
  <details>
    <summary>App Dashboard :mag:</summary>

    ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/fde9249a-f073-46af-aeff-ddf4b7d6aacf)
  </details>
  
- Within the `Settings` menu, navigate to `Config Vars` (Also known as *Environment Variables*).<br>
  This is where private and sensitive data, such as credentials and keys, will be stored for the project.
  <details>
    <summary>App Settings :mag:</summary>

    ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/078e131f-0ec6-483f-9031-7049385cdad8)
  </details>

- If the project is dependant on a creds.json file, then this is where the data will be stored.
- Click `Reveal Config Vars`. For initial deployment of a full-stack project:<br>
  `KEY`: 'DISABLE_COLLECTSTATIC'. `VALUE` '1'<br>
  This will prevent Heroku from uploading static files to the build.<br>
  Later on, once the project has been configured with a local static file directory, this KEY/VALUE pair can be removed.
- Note that any other secret keys such as links to the prject's database will be added as the project develops.<br>
  The image below shows an example of the `config vars` panel used in a previous project.
  <details>
    <summary>Config Vars :mag:</summary>
    
    ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/0721287b-f32f-4b37-be16-ddcf1cfeb1c2)
  </details>

- A final component required for successful deployment is the use of a `Procfile`:
    - Heroku will read this file to determine how to start the server.
    - Within the Procfile a python package called *gunicorn* is referenced as a production-ready webserver for Heroku to use.
    - After installing gunicorn and adding it to the `requirements.txt` file, the following line of code needs to be added to
      the Procfile `web: gunicorn my_project.wsgi`.
    - Note that a blank line after the above code may be either required or need to be removed for Heroku to read it successfully.

### Connect to GitHub and deploy:

- Navigate to the `Deploy` menu. For `Deployment method` select GitHub. Finally, you can manually deploy the project.
  <details>
    <summary>Deploy Menu :mag:</summary>

  ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/9081df0b-d551-40f2-b9c1-f770b9d4a5fb)
  </details>




