# Trouble Less Events

### Information about the directory structure

http://www.revsys.com/blog/2014/nov/21/recommended-django-project-layout/

### MINIMUM PLAN

- Add accounts in the app.
- Start by creating the templates for participants.
- The participant view must consist of a login window.
- If logged In take them to the view having three buttons.
  - Add profile.( create view)
  - Update a profile.( Update view and delete view)
  - see all profiles.( Retrieve view)
  - Participate in an event.




### Future plan

For the time being the event proposal are shared by using email. I want to create an interface through which the users can create and share their ideas directly into the app. The app interface will look like this:

Event Name - .....
Event coordinator Name - ......
Coordinator Branch - ......
Event coordinator Year - .....
Number of members - .....
Proposal - ............

SUBMIT

The core-team has the power to select or deselect the event. If a user has logged IN as a core member he or she can select as well as reject the event. Here voting can happen: If more than half core members decide to reject the event and if more than half people decide to accept the event then the event is selected. After selecting the event the room and time is going to be allocated to the event.

Once all details are filled by the core team, special Id and password will be generated for the event coordinator and he can futher generate as many ID's and passwords as the number of members as he suggested in last step. The event coordinator must take care of this step and allow proper sending of userIDs and passwords. He can ask the main programmer to increase or decrease the allowed members, if needed.

#### Role of event coordinators

#### Role of event members

- Members can allow the submittion of the forms and check for the presence of the participants. If the member is not present remove there names from the list. This means for the members, we need the participants view with the permission of update and delete.


#### Role of participants

- Participants can login using google or email and then they can add a profile. The profile is going to made visible to the member and then member can take the entry fees and select the check box for the fees submitted.

- There is no much need of participant to be authenticated. But if authenticated we can save their profiles

- Participant can also add multiple profiles.

- When the members take the attendence the non present members must be sent to a trash list from where they can be retreived. The participants who have not paid are also going to be in the same list.

- Certificates will only be issued to the people who have registred, appeared and paid the fees.

- The extra money of the students who have not appeared must be given to the programmer :)
