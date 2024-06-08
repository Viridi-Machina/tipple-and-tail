![image]()

# Tipple & Tail
## By Jacen Green

## Summary

## Process

**Problem Statement**

**Research**
<details>
 <summary></summary>
 
</details>

**Design**

**Development**

User Stories:
- As a user, I want to view availability based on the selected date and party size, so that I can view available booking options.
- As a user, I want to view a table plan of available tables, so that I can choose where to sit.
- As a user, I want to see a list of available packages that I can add to my booking, so that I can customize my experience.
- As a user, I want to review booking details before finalising the booking, so that I can check that everything is correct.
- As a user, I want to provide personal details during the booking process, so that I can recieve confirmation via email.
- As a user, I want to see an about page, so that I can learn more about the establisment before booking.
- As a user, I want to view a drinks menu, so I can see what options are available before making a booking.
- As a user, I want to be able to declare allergies when making a booking, so that the establishment is aware before arrival.
- As a user, I want to see a map, so that I can see how far the establishment is from my current location.
- As a user, I want to see confirmation of a successful booking, so that I have confidence a booking has been made.
- As a user, I want to be able to edit a booking after it has been made, so that I can cancel or view my booking.
- As a user, I want to review and leave comments on events that I have been to, so I can share my experience with others.

- As an admin, I want to view and update details of a specific booking, so that I can handle enquiries and make changes.
- As an admin, I want to manage user accounts, so I can maintain control over user access and disable accounts if necessary.
- As an admin, I want to log in to a a secure admin panel, so that I can access the site's administrative features.
- As an admin, I want to manage the about page, so I can ensure it remains up to date.
- As an admin, I want to manage the events page, so I can add new events and moderate customer reviews.
- As an admin, I want to manage the menu page, so that I can add/remove or update menu items and pictures.
- As an admin, I want to tag certain booking packages, so that I can upsell and make them more appealing.

**Data Models**

## Features
**CRUD Functionality**

**Authentication & Authorisation**

**Future Feature Implementation**

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

**Genral**

**Authorisation**

**Lighthouse**

**Responsiveness**
ResponsivelyApp

**Code Validation**
W3C Markup Validation Service
JSHint
PEP8

## Deployment
**Local Deployment**
**Heroku Deployment**
<details>
 <summary>Method :purple_circle:</summary>

- From the dashboard you will be able to see your deployed projects. Click on `New`, then `Create new app`:
  <details>
    <summary>Dashboard :mag:</summary>
    
    ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/d4468782-45f9-4c26-8369-1ddffee2b408)
  </details>

- Enter a unique `App name` and `Choose a region`, then click `Create app`.<br>
  Once created you navigate to the `Settings` menu.
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
- Click `Reveal Config Vars`. Type in the first `KEY`: 'CREDS'.<br>
  For the `VALUE` paste in the contents of your creds.json file from the IDE that you are using.
- It is also important to set another KEY, VALUE pair as `PORT`, `8000` respectively<br>
  or the project may not properly deploy.
  <details>
    <summary>Config Vars :mag:</summary>
    
    ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/0721287b-f32f-4b37-be16-ddcf1cfeb1c2)
  </details>

- Next, some `Buildpacks` will need to be added which will add further dependancies outisde of the project<br>
  which will allow the deployment to run in a virtual environment.
- First, click `Add buildpack` and select `python`. Then add `nodejs`. It is important that you do it in this order.<br>
  The ordering however can be changed afterwords by dragging their burger icons within the buildpacks list.
  <details>
    <summary>Buildpacks :mag:</summary>
 
    ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/d7a30ca4-e36a-44eb-8e87-5626e84e7e25)
  </details>
</details>

### Connect to GitHub and deploy:
<details>
  <summary>Method :purple_circle:</summary>

  - Navigate to the `Deploy` menu. For `Deployment method` select GitHub. Finally, you can manually deploy the project.
    <details>
      <summary>Deploy Menu :mag:</summary>

    ![image](https://github.com/Viridi-Machina/battleships/assets/146846939/9081df0b-d551-40f2-b9c1-f770b9d4a5fb)
    </details>
</details>

**Environment Variables**



