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



