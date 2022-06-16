# Deegagh Sea Salt
 
<img src="docs/mock-up/mock-up.png" alt="Mockup of my site across multiple devices">
<a href="https://donegal-courts.herokuapp.com/" alt="link to Deegagh Sea Salt" target="_blank" rel="noopener">Link to The Deegagh Sea Salt</a>

<p> In order to view this project correctly in github, please add the following into the terminal: "pip3 install -r requirements.txt"</p>

## Project Goals 
<ul>
    <li> The main goal of this project is to create a website that site users can buy sea salt from.</li>
    <li>The E-Commerce site will be fully functional and will allow users from all age demographics and tech experience to use the site easily. </li>
</ul>
<hr>

## Table of Contents
1. [Project Goals](#project-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements](#user-requirements)
    3. [User Stories](#user-stories)
3. [Technical Design](#technical-design)
    1. [Flow Chart](#flow-chart)
    2. [Database Diagram](#database)
    3. [User Manual](#user-manual)
    4. [Wireframes](#wireframes)
4. [Technology](#technology)
    1. [Develpoment Languages Used & 3rd Party Libraries:](#develpoment-languages-used)
5. [Features](#features)
6. [Testing](#testing)
    1. [Python Validation](#python-validation)
    2. [HTML Validation](#html-validation)
    3. [CSS Validation](#css-validation)
    4. [JavaScript Validation](#javascript-validation)
    5. [Accessibility](#accessibility)
    6. [Performance](#performance)
    7. [Testing user stories](#testing-user-stories)
7. [Bugs](#Bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
10. [Acknowledgements](#acknowledgements)
11. [Future Features](#future-features)

### User Experience:

### Target Audience 
<p>The Donegal Courts blog was inspired by the local newspaper of Donegal - the Donegal News/ Derry people, so the target audience would be of readers of that or for people who are native to Donegal that live away and want to stay up to date. In short, the Target audience is mainly Donegal Natives or people who have Donegal Ties that want to stay up to date with the court listings. </p>

### User Requirements
<p>As I have mentioned, the blog has a very niche target audience. However, the age demographics are quite broad and because of this the blog has to be easy to use for every age group. I have taken the following approach to make sure that all User Requirements to access and use the blog has been covered:</p>
<ul>
    <li>Have a clear understanding of the layout of the site -> clear navigation.</li>
    <li>The blog has to be formal and factual, information on the site has to be easily accessibile to the user.</li>
    <li>The option of customizing the blog posts by the owner has to be limited it the authorisation. A random user of the blog can not have permition to comment or post on the blog.</li>
    <li> As the topics discussed on the site contain sensitive information, I want the admin to be able to choose what comments get posted or not.
</ul>

### User Stories

### First time and Recurring Stories
<ol>
    <li>As a user of the site, I want to be able to Browse through content on the website.</li>
    <li>As a user of the site, I want to be able to View Court News Stories.</li>
    <li>As a user of the site, I want to be able to View Court News Stories in a List.</li>
    <li>As a user of the site, I want to be able to open and read the court news stories.</li>
    <li>As a user of the site, I want to be able to View comments under each post.</li>
    <li>As an authorized user of the site, I want to be able to Post Comments. </li>
    <li>As a user of the site, I want to be able to Register for an account.</li>
</ol>

### Site's Owner Stories
<ol>
    <li>As an authorized owner of the site, I want to be able to Post Stories to the site.</li>
    <li>As an authorized owner of the site, I want to be able to Create story drafts to come back to.</li>
    <li>As an authorized owner of the site, I want to be able to Manage site content.</li>
    <li>As an authorized owner of the site, I want to be able to Manage comments under posts.</li>
</ol>

## Technical Design

### Flow Chart
<p> I used the flow chart to design a clear map of my site that would help me design the functionality of the site and the logic and guidence for user stories. I did this by using Lucid Chart</p>
<details><summary>Flow Chart</summary>
        <img src="docs/flowchart/flowchart.png"></details>
<hr>

### Database 
<p> My Database has four models:
<p> My project uses the relational databse -> PostgreSQL.</p>
<p> The data is handeled within the application with Django. </p>
<ul>
<li> Profile </li>
<li> Post </li>
<li> Comment </li>
<li> Contact </li>
</ul>
<ul>
<p> Profile: </p>
<li> The Profile model in my application creates the users profile.</li>
<li> It is part of the django.db library. </li>
<li> It includes the following fields: user, bio, profile_pic, website_url, facebook_url, twitter_url, instagram_url, pinterest_url.</li>
<li> It includes a One to One field which is apart of a command to delete history of a user if the user is deleted.</li>
<br>
<p> Post: </p>
<li> This post model will allow me to post onto the site, and create the required variables fields.</li>
<li> It is used by the admin to post blog posts to the site, there for it uses a Foreign Key as an ID of the admin/ author. </li>
<li> It includes the following fields: title, title_tag, featured_image, snippet, author, body and post_date.</li>
<br>
<p> Comment: </p>
<li> This comment model will allow users to post comments under the blog post.</li>
<li> It is used by several users to post comments under the blog post, there for it uses a Foreign Key. </li>
<li> It includes the following fields: post, name, body, date_added.</li>
<br>
<p> Contact: </p>
<li> This contact model will allow me to save the contact forms that are sent to the admin of the site, and store the details in the admin section of the site so the admin can easily get back to the user trying to get in contact.</li>
<li> It is used by several users to contact the admin of the site, there for it uses a input fields. </li>
<li> It includes the following fields: name, email and message.</li>
<br>
<p> Comment has a many to one relationship and also uses the imported User class model for username and user unigue        passwords.</p>
<p> Post has a many to manny relationship and also uses the imported User class model for username  to help calculate the likes on each blog post.</p>
<details><summary>Database Diagram</summary>
        <img src="docs/database-diagram/database.jpg"></details>
<br/>

### User Manual:
<ol>
<li>The site admin username is admin (lowercase) and the password is Frious.30.</li> 

<li>The Site is very simple in design - It includes a home section where a user can view a blog post, a members section for login and registration, and then a contact section located at the bottom of the webpage.</li>
<li>The blog posts have a very simple design - the title, the post body, the author section with information of the author and the comments section for views to create a comment.</li>
    <p> -- If the user is the site admin a edit post and delete post section is added.</p>
<li>The login in section is simple as it is restricted to asking for the username and password. The registration form is also simple and easy to follow.</li>
<li> Finally the contact Page allows the user to simply message the admin of the site to get more information or to leave a comment. The address and phone number are also on the page.</li>
<li> The admin mainly uses the Admin section of the site to post blog posts, look at messages that were left by users of the contact form and to manage comments left in the site ie. delete abusive comments if they are left.</li>
</ol>

<hr>

### Wireframes:


<details><summary>Home Page</summary>
        <img src="docs/wireframes/home.png"></details>

<details><summary>Home Page: Membership Option</summary>
        <img src="docs/wireframes/home-members.png"></details>

<details><summary>Login</summary>
        <img src="docs/wireframes/login.png"></details>

<details><summary>Register</summary>
        <img src="docs/wireframes/register.png"></details>

<details><summary>Home page: Loggined-In User</summary>
        <img src="docs/wireframes/home-logged-in.png"></details>

<details><summary>Blog Post</summary>
        <img src="docs/wireframes/posts.png"></details>

<details><summary>Comments</summary>
        <img src="docs/wireframes/comment.png"></details>

<details><summary>Blog Post: Edit (Only admin View)</summary>
            <img src="docs/wireframes/edit-post.png"></details>

<details><summary>Blog Post: Delete (Only admin View)</summary>
            <img src="docs/wireframes/delete-post.png"></details>

<details><summary>User Profile</summary>
            <img src="docs/wireframes/user-profile.png"></details>

<details><summary>Contact Page</summary>
            <img src="docs/wireframes/contact-page.png"></details>

        
<hr>

### Technology:

### Develpoment Languages Used

<ul>
<li> Python </li>
<li> HTML </li>
<li> CSS </li>
<li> JavaScript </li>
</ul>

###  Frameworks and Tools used & 3rd Party Libraries:
<ul>
<li> Git, GitHUb, and GitPod </li>
<li> Lucid Chart </li>
<li> Balsamiq - Wireframes </li>
<li> quickdatabasedesign.com </li>
<li> Heroku </li>
<li> Django </li>
<li> BootStrap 5 </li>
<li> Ajax</li>
</ul>
<hr>

## Features:

### Home
<p> The home page is the main landing page that includes a bulk of the features of the site.</p>
<ul>
    <li>Slider: The slider adds a nice dynamic aspect to the site and helps users identify the site as legal in theme.</li>
    <li>Blog Post List: The blog post list includes all the blog posts on the site allowing the user to browse through the posts. You can click on these posts to read the story in more depth.</li>
    <li> Login/ Registration: The registration section allows the user to become a member of the site, leave a comment under the posts and add a bit of personalisation to the blog by adding their name to the landing page and editing their profile details.  </li>
    <li>The logout section: Gives the users the option of signing out, this specifically removes the user from being logged into the site and the obvious change is the name removed from the site navbar.</li>
    <li>Contact Us: Contact page with a contact form for the user to easily contact the admin of the site. It also contains the contact information ie. address and phone number. The contact page will have a pop-up when the form is submited to tell the user the form has been successfully submitted.</li>
</ul>
 <p>User Stories covered : 1, 2, 3, 4, 7</p>
 <p>Site Owner's Stories covered: 0 </p>
        <details><summary>Slider</summary>
        <img src="docs/user-stories/slider.png"></details>
        <details><summary>Blog Post List</summary>
        <img src="docs/user-stories/blog_post_list.png"></details>
        <details><summary>Login/ Registration (nav)</summary>
        <img src="docs/user-stories/login:register.png"></details>
        <details><summary>The logout section (nav)</summary>
        <img src="docs/user-stories/logout.png"></details>
        <details><summary>Contact Us (footer)</summary>
        <img src="docs/user-stories/contact.png"></details>

#### Blog Post
<p> The blog post page holds the most content for users on the site. </p>
<ul>
    <li>Blog post: Where users can view and read the blog posts.</li>
    <li> Back Button: Directly under the post title is a back button the user can use to look through the other blog posts.</li>
    <li> Like: The user can like the post and the like will be counted. The user can only like the post if they are logged in with an account. </li>
    <li> User Profile: The admin has a section under the post that displays the authors bio, urls and a link to the authors user profile on the site. The user profile is an oppurtunity for the author to add a bio about themselves that highlights their experiecnce and education. </li>
    <li> Comment Section/ Comment Form: The comment section is an area under the blog post that allows the user of the site to add comments to the blog post to help create a public discussion on each blog post that is on the site. The users of the site, if logged in, are freely allowed to post in real-time, but if its offensive the admin can delete it in the admin section of the site.</li>
    <li> Delete and Edit Section: If the user is a superuser of the site they will be able to delete and edit the blog post as the want using forms. </li>
</ul>
    <p> User Stories covered:4, 5, 6</p>
    <p>Site Owner's Stories covered: 4 </p>
        <details><summary>Blog post</summary>
        <img src="docs/user-stories/blog_post.png"></details>
        <details><summary>Back Button</summary>
        <img src="docs/user-stories/like.png"></details>
        <details><summary>Like</summary>
        <img src="docs/user-stories/like.png"></details>
        <details><summary>User Profile</summary>
        <img src="docs/user-stories/user_profile.png"></details>
        <details><summary>Comment Section/ Comment Form</summary>
        <img src="docs/user-stories/comment.png"></details>
        <details><summary>Delete and Edit Section</summary>
        <img src="docs/user-stories/delete:edit.png"></details>

#### Admin Section
<p> The admin section is the backend of the site that the admin can log into to create blog posts, create blog post drafts, delete posts, delete comments, and add more content to their admin user profile. </p>
<ul>
    <li>Users: The user section includes the superuser information for the admin of the site. </li>
    <li>Posts: The post section is the area where the admin can create, draft and delete blog posts that will be displayed on the site. The content uploaded to thei section contains: title, snippet, image, body, author, category, and title tag.</li>
    <li> Comments: The section where the admin can view the comments left on the blog posts and delete, manage or keep.</li>
    <li> Profile: This is the section that stores the User information created by visitors. </li>
    <li>Contact: This section stores the data sent by the user to the admin via the contact for. It includes the user's name, email and message.</li>
</ul>
    <p> User Stories covered: 0 </p>
    <p>Site Owner's Stories covered: 1, 2, 3, 4 </p>
        <details><summary>Users</summary>
        <img src="docs/user-stories/users.png"></details>
        <details><summary>Posts</summary>
        <img src="docs/user-stories/posts.png"></details>
        <details><summary>Comments</summary>
        <img src="docs/user-stories/comments.png"></details>
        <details><summary>Profile</summary>
        <img src="docs/user-stories/profile.png"></details>
        <details><summary>Profile</summary>
        <img src="docs/user-stories/admin-contact.png"></details>
<hr>

## Testing:

### Python Validation
<p> To Validate my Python I used the ExtendsClass Free Online Toolbox for developers (https://extendsclass.com/python-tester.html). All python code passed its Validation with no errors but one warnings as shown below in the pictures.</p>

<h4> Blog (App)</h4>
<details><summary>admin.py</summary>
<img src="docs/python-validation/admin.blog.png"></details>

<details><summary>forms.py</summary>
<img src="docs/python-validation/forms.blog.png"></details>

<details><summary>models.py</summary>
<img src="docs/python-validation/models.blog.png"></details>

<details><summary>urls.py</summary>
<img src="docs/python-validation/urls.blog.png"></details>

<details><summary>views.py</summary>
<img src="docs/python-validation/views.blog.png"></details>

<h4> Members (App)</h4>
<details><summary>forms.py</summary>
<img src="docs/python-validation/forms.members.png"></details>

<details><summary>urls.py</summary>
<img src="docs/python-validation/urls.memeber.png"></details>

<details><summary>views.py</summary>
<img src="docs/python-validation/views.memebers.png"></details>

<h4> Contact (App)</h4>
<details><summary>admin.py</summary>
<img src="docs/python-validation/admin.contact.png"></details>

<details><summary>forms.py</summary>
<img src="docs/python-validation/form.contact.png"></details>

<details><summary>urls.py</summary>
<img src="docs/python-validation/urls.contact.png"></details>

<details><summary>views.py</summary>
<img src="docs/python-validation/views.contact.png"></details>

<details><summary>models.py</summary>
<img src="docs/python-validation/models.contact.png"></details>

<br>

### HTML Validation
<p> To Validate my HTML I used the WC3 Validator. All HTML code passed its Validation with a few errors as documented below. All errors are due to using the django/python framework.</p>

<details><summary>Home Page</summary>
<img src="docs/html/home.html.png"></details>
<details><summary>Add Comment </summary>
<img src="docs/html/add_comment.html.png"></details>
<details><summary>Base</summary>
<img src="docs/html/base.html.png"></details>
<details><summary>Delete Pose</summary>
<img src="docs/html/delete-post.png"></details>
<details><summary>Update Post</summary>
<img src="docs/html/update-post.html.png"></details>
<br>

<details><summary>Contact</summary>
<img src="docs/html/contact.html.png"></details>
<br>

<details><summary>Change Password</summary>
<img src="docs/html/change-pass.png"></details>
<details><summary>Edit Profile</summary>
<img src="docs/html/edit-profile.png"></details>
<details><summary>Login</summary>
<img src="docs/html/login.png"></details>
<details><summary>Password Success</summary>
<img src="docs/html/pass_success.png"></details>
<details><summary>Register</summary>
<img src="docs/html/reg.png"></details>
<details><summary>User Profile</summary>
<img src="docs/html/user-prof.png"></details>
<br>

### CSS Validation
<p> To Validate my CSS I used the Jigsaw W3 Validator. All CSS code passed its Validation with no errors or warnings as shown below in the pictures.</p>

<details><summary>CSS Validation</summary>
<img src="docs/validation/css_validation.png"></details>

### Accessibility
<p> To Validate the Accessibility of the site I used the Wave Web Accessibility Validator.</p>

<details><summary>Home page</summary>
<img src="docs/accessibility/home.png"></details>

<details><summary>Contact page</summary>
<img src="docs/accessibility/contact-wave.png"></details>

<details><summary>Login page</summary>
<img src="docs/accessibility/login_access.png"></details>

<details><summary>Register</summary>
<img src="docs/accessibility/register.png"></details>

<details><summary>Post Details</summary>
<img src="docs/accessibility/post_detail.png"></details>

<details><summary>User Profile</summary>
<img src="docs/accessibility/user-profile.png"></details>

<details><summary>Comment Form</summary>
<img src="docs/accessibility/comment-form.png"></details>

<details><summary>Delete Post</summary>
<img src="docs/accessibility/article-delete.png"></details>

<details><summary>Update Post</summary>
<img src="docs/accessibility/article-update.png"></details>

### Performance
<p> To Validate the Performance of the site I used the lighthosue tool in the browser'git ps develpoments tools.</p>

<details><summary>Home</summary>
<img src="docs/performance/home-performance.png"></details>

<details><summary>Contact page</summary>
<img src="docs/performance/contact-performance.png"></details>

<details><summary>Login page</summary>
<img src="ddocs/performance/login-performance.png"></details>

<details><summary>Register</summary>
<img src="docs/performance/register-performance.png"></details>

<details><summary>Post Details</summary>
<img src="docs/performance/post-performance.png"></details>

<details><summary>User Profile</summary>
<img src="docs/performance/user-performance.png"></details>

<details><summary>Comment Form</summary>
<img src="docs/performance/comment-performance.png"></details>

<details><summary>Delete Post</summary>
<img src="docs/performance/delete-performance.png"></details>

<details><summary>Update Post</summary>
<img src="docs/performance/edit-performance.png"></details>
<hr>

### Testing User Stories

    1."As a user of the site, I want to be able to Browse through content on the website."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Home section of blog post site| The user can scroll through the content uploaded by the site admin| The user can browse through the content on the site| Works as expected|

<details><summary>User Testing 1</summary>
<img src="docs/test-user-stories/content.png">
</details>
<hr>

    2."As a user of the site, I want to be able to View Court News Stories."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Home section of blog post site| The user can scroll through the content uploaded by the site admin and read the court news stories| The user can browse through the content on the site| Works as expected|

<details><summary>User Testing 2</summary>
<img src="docs/test-user-stories/content.png">
<img src="docs/test-user-stories/read_post">
</details>
<hr>

    3."As a user of the site, I want to be able to View Court News Stories in a List."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Home section of blog post site| The user can scroll through the content uploaded by the site admin. The blog posts are shown in a list formate| The user can browse through the content on the site| Works as expected|
<details><summary>User Testing 3</summary>
<img src="docs/test-user-stories/view_stories.png"></details>
<hr>

    4."As a user of the site, I want to be able to open and read the court news stories."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Detailed blog post section of the site| The user can read the blog post stories once they have navigated into a story the want to read.| The user can read the post on the site| Works as expected|

<details><summary>User Testing 4</summary>
<img src="docs/test-user-stories/read_post.png"></details>
<hr>

    5."As a user of the site, I want to be able to View comments under each post."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Comments section under blog post| The user can read comments left by other users that have visited the site| The user can read the comments for posts on the site| Works as expected|

<details><summary>User Testing 5</summary>
<img src="docs/test-user-stories/view_comment.png"></details>

<hr>

    6."As an authorized user of the site, I want to be able to Post Comments."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Comments section under blog post| The user can create and post comments under the blog posts| The user can create the comments for posts on the site| Works as expected|

<details><summary>User Testing 6</summary>
<img src="docs/test-user-stories/post_comment.png"></details>

   7."As a user of the site, I want to be able to Register for an account."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Register Section in Nav Bar| The user can create an account with the site| The user can create their account and leave comments if wanted | Works as expected|

<details><summary>User Testing 7</summary>
<img src="docs/test-user-stories/register.png"></details>


### Testing Site Owner's Stories

    1."As an authorized owner of the site, I want to be able to Post Stories to the site."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Django admin section| The admin can create blog post to be displayed in the site| The admin can create a blog post in their admin section to be displayed on the site | Works as expected|

<details><summary>User Testing 8</summary>
<img src="docs/test-user-stories/post_admin.png"></details>
<hr>

    2."As an authorized owner of the site, I want to be able to Create story drafts to come back to."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Django admin section| The admin can create blog post to be displayed in the site. If the user doesn't want to post the blog post right away they can save it as a draft and come back to it| The admin can create a blog post in their admin section and save it as a draft | Works as expected|

<details><summary>User Testing 9</summary>
<img src="docs/test-user-stories/post_admin.png">
</details>
<hr>

    3."As an authorized owner of the site, I want to be able to Manage site content."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Django admin section| The admin can create a blog post, delete a blog post, post comments and delete comments on posts to be displayed in the site.| The admin can create a blog post, delete a blog post, post comments and delete comments in their admin section | Works as expected|

<details><summary>User Testing 10</summary>
<img src="docs/test-user-stories/admin-control.png">
</details>
<hr>

    4."As an authorized owner of the site, I want to be able to Manage comments under posts."
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Django admin section| The admin can delete comments on posts to be displayed in the site.| The admin can delete comments in their admin section, if the comments are offensive etc. | Works as expected|

<details><summary>User Testing 11</summary>
<img src="docs/test-user-stories/manage_comment.png"></details>
<hr>

## Bugs:

| **Bug** | **Fix** |
<p> I couldn't get my django messaging to work and therefore tried to create a backup messaging service using Ajax. I called tutors, looked for hours on google, stackover flow and youtube and I just couldn't figure out on time why my messages weren't working. Below is a list of resources I used to try and figure out the error.</p>

<ul>
<li>https://ordinarycoders.com/blog/article/extend-and-include-django-template-tags</li>
<li>https://docs.djangoproject.com/en/4.0/ref/contrib/messages/</li>
<li>https://www.javatpoint.com/django-form-validation</li>
<li>https://www.youtube.com/watch?v=Mf_97YaUKag</li>
</ul>

<p> When talking to tutor support they suggest the following which I tried with no success:</p>

<ul>
<li>Suggestion 1: Make use of the Google console - I can see that there is an error coming from the js, so i would recommend you make more use of these tools to help improve your debugging skills and get you through this issue.
</li>
<li>
Suggestion 2: Double check that the bootstrap version is not causing issues with the js functionality - this is a very common thing to see. You may want to check the exact version used in the walkthrough, or do some further research into how to apply messages for your specific bootstrap version.
</li>
<li>
Suggestion 3: Run through the course materials again and use diffchecker to check the source code versus your own to highlight any obvious errors.
</li>
<li>
With this in mind, we recommend:
 -  Recommendation 1: Reviewing the following lessons and resources, which are directly applicable to the code you are currently working on:
 - Recommendation 2: If you are stuck overall, chat to your mentor, and come up with a clear plan (a set of concise steps which you feel comfortable implementing) which will achieve a passing grade, and work on that.
 - Recommendation 3: Google is a programmer’s best friend. Everybody gets stuck at some point when coding, and the first thing they do is turn to Google. If you’re struggling with a particular piece of functionality or don’t understand what a particular line of code does, try Googling it! Every built-in function has extensive documentation available online. For example, W3Schools contains detailed explanations on every piece of HTML, CSS, JavaScript, and Python code you could think of. For example, here’s their doc for the JavaScript Array.indexOf() function: https://www.w3schools.com/jsref/jsref_indexof_array.asp They provide working code examples, descriptions of the function, and information about similar functions!
</li>
<p> I am stuck tryin to fix this at them moment, I have tried the tutors recommendations but with no luck. I think I would try restart the page and see if there was a deeper issue in the page I can't see at the moment, I have just ran out of time.</p>

<br>
|<p> The other bug is the comment form, the comment posts to the site fine, the validation just doesn't work or prompt the user.</p> | <p> Just like the previous bug I would have to figure out why my form validation isn't working. I would re-write the comment form in this case though.</p>

<p> I managed to get form validation on the contact form. I had to re-write the messages section in the base.html and add a message.addmessage to the views.py</p>
<details><summary>Contact Form Validation</summary>
<img src="docs/validation/form-validation.png"></details>
</ul>
<hr>

## Deployment:

### Deploying to Heroku (Automatic)

<ul> 
<li> Use pip3 freeze > requirements.txt in terminal to save libraries that need to be installed on Heroku as well.</li>
<li> Create Procfile and add web: gunicorn blog.wsgi.</li>
<li> Log in to Heroku.</li>
<li> Click on the new button in the top right corner and in the drop down menu choose Create New App.</li>
<li> Choose a name for your app and a region and then click Create App.</li>
<li> Go to the resources tab and go to add-ons, search for postgres and ass heroku postgres.</li>
<li> Go to the settings tab and go to Config Vars, click Reveal Config Vars and copy the DATABASE_URL_VALUE. Add DATABASE_URL and Value to the env.py in the code.</li>
<li> Add SECRET_KEY and VALUE to Config Vars and add to the env.py in code.</li>
<li> Add DATABSES in settings.py to fork with heroku database.</li>
<li> Write python3 manage.py migrate in terminal.</li>
<li> Add url in settings.py on ALLOWED_HOSTS.</li>
<li> Go to the deploy tab and pick GitHub as deployment method.</li>
<li> Search for a repository and connect to it.</li>
<li> Click the button enable automatic deploys and the button deploy branch.</li>
<li> Wait for the app to build and then click the rview button.</li>
</ul>
<br>

### Deploying to Heroku (Manual CLI)
<ul>
<p> In Gitpod terminal; </p>
<li>enter in 'heroku login -i'</li>
<li> Then enter 'heroku apps</li>
<li> Set the heroku remote > enter into the terminal 'heroku git:remote -a 'your app name'</li>
<li> git add . and git commit -m </li>
<li> git push origin main </li>
<li> git push heroku main </li>
</ul>

### Forking a Repository

<ol> 
<li> Log into Github. </li>
<li> Find the Repository you wish to fork.</li>
<li> In the top right corner click the fork button. </li>
<li> Now you will have a copy of the repository in your account! </li>
</ol>
<br>

### Cloning a Repository

<ol> 
<li> Log into Github. </li>
<li> Find the Repository you wish to clone.</li>
<li> Above the file window locate the green code button and click it. </li>
<li> To clone the repository using https copy the link. </li>
<li> Open Git Bash. </li>
<li> Change the current directory to where you wnat the repository cloned. </li>
<li> In your terminal type now type "Git Clone" followed by the repository you copied. </li>
<li> Press Enter.</li>
</ol>

<br>

## Credits:
### Source Code Used in Site

<p> Due to limitations in my knowledge I used youtube tutorials/ stack overflow articles to guide me with creating the blog:</p>
<ul>
<li> Codemy: https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi </li>
<li>Django Documentation: https://docs.djangoproject.com/en/4.0/topics/email/</li>
<li> SitePoint: https://www.sitepoint.com/django-send-email/</li>
<li> Plainenglish: https://python.plainenglish.io/how-to-create-a-contact-page-for-your-django-website-6b97dddedb2d</li>
<li>https://learncodeweb.com: Used for the AJAX Pop-Up: https://learncodeweb.com/web-development/how-to-create-a-custom-popup-form-with-php-and-ajax/</li>
<li>https://docs.djangoproject.com/en/4.0/ref/contrib/messages/</li>
</ul>
<br>
<p> I used these videos/ articles soley as a guide I did not copy and paste.</p>
<ul>
<li>Photo by Moose Photos: https://www.pexels.com/photo/woman-wearing-pink-collared-half-sleeved-top-1036623/</li>
        <li> Other images used were from donegal daily in their court posts with no clear owner.</li>
<hr>
<br>

## Acknowledgements:
<p> I would like to take this oppurtuinity to thank and acknowlege the following people:
<ul>
<li> I would like to thank Mo Shami - my mentor - for his feedback and guidence whilst creating the project.</li>
<li> I would like to thank those on the code institute slack channel for help with any issues I had.</li>
<li> I would also like to thank Conor lawton who helped me with understanding some of the code.</li>
</ul>

## Future Features
<p>In future, I would like to add a section where users could view a list of solicitors and barristers in the area that could help them if they needed legal advice.</p>