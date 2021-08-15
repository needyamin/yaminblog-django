# Distinctiveness and Complexity:
When I started the final project, I had no idea how and what I was going to do. Later I decided that since I like blogging I would create my own blog using Django. And I did.. This is an advanced dynamic and SEO friendly blogging website. I included every possible thing in my project and I can't believe it now, I created this website. This is not only finaly project for CS50W, it's my future blogging platforms. I'm feeling so proude, finally I've done this.

# YAMiN Blog AND CMS System #
Project Name: YAMiN; 
Project Type: Blog, CMS, Publishing Tool 
Framework: Django 3.2.3
Environment: Conda (BASE_ENV.yml)

# How to run this Website?
Just download this project. Activate the python conda environment to your IDE, Type the following two commands:
> $ python manage.py makemigrations

> $ python manage.py migrate

And then type this commands: 
> $ python manage.py runserver

You can see the localhost IP with the port. Open it on your web browser.

# Getting "No Module found" Errors???
> If you have get any error in your environment then please import "BASE_ENV.yml" to your conda environment. 
You will find my "BASE_ENV.yml" root directory on this project. Just import this "BASE_ENV.yml" to your conda new enviroment and run this above 3 commends.


##################################################################################################

# Site Features:
> Full Control Dynamic System 

> Mobile Friendly UI/UX Design

> SEO Friendly URL, Images, Title, Descriptions

> Diffrent Dashboard For Users and Admins

> Add Post, Edit (Post, Images, Sitecofig, Favicons)

> Delete Posts, Rejection, Warning

> Email Subscribtion/NEWSLETTER, Print as PDF

> User Profile, Name, Emails etc...

> Custom Privacy, About Us, Contact Us, Sitemap Pages..

> All Images of files uploaded separately in each user's ID folder


# Users Features:
> Create Accounts, Edit Email, Password & Other Information

> Users Advanced Dashboard, Top Ten Users, Visit Counts

> Advanced Search Options, Quick Views, Warning PopUp Model

> Add Post, Pending, Draft Systems

> Edit Post, Images, Draft..

> Username slug Profile


# Admin Features:
> Approve Post, Delete Post, Reject Post

> Print all Subscribed Emails

> Edit siteconfig, Privacy Page, About Us page, favicon, Site title, Keywords, Descriptions and much more..


****************************************************************************************************
This is final project for CS50W. This is an advanced dynamics and SEO friendly blogging website. SEO friendly url and also sitemap added on this website. Also dynamics SEO meta tags, keywords, description and cover image added to this website.

This website has two part. One is for User Panel, Another is for SuperAdmins. 

# *** For Users: ***

Here is a PieChart and top ten menu on the users dashboard where users will see their activities statistics. Users can create new accounts and submit new blog post to the website. But all new blog post will goes pending untill superadmin verify or approve the new blog post. Once superadmin approve users post, the blog post will display on the "active post" options and also goes "live" to the website. And no one either admins or users can delete or edit active post due to SEO conditions. If superadmin reject a users post for 5 times, then any superadmin can suspend users account and all users blog post, comments, drafts will permanently deleted from the website.

Also users can save their blog post to the draft. They can edit, delete their drafts or pending post. Users can change their email account, first name, last name. passwords but they can't edit their username due to security issues. Same thing happens when they edit their drafts post, they can't able to edit their slug url due to security issues. 

# *** For Admins ***
Here is another Pie chart on the super admin dashboard where admin will see full website activitie statistics. Superadmins can see all pending post on their admin dashboard. And they can read post, approve the post, reject the post or also can delete users pending post. 

Another tab for admin panel, Here is an email subscriber option, where admins can see all email subscribed users and also admin able to download or print as pdf all subscriber list.

And last tab in Admin panel, The "SiteConfig". Here super admins can update website's title, keywords, descriptions, body tags and favicons. Also they can update website's Privacy Policy and About Us page from these admin panel.
****************************************************************************************************


##################################################################################################

# Note:
> No one can post dobule entry to the website like (same slug url, same comment, same usersname).

> All images croped and all files uploaded separately in each user's ID folder ( /media/blog_users/user_ID)

> Blog slider always displayed last three blog post.




For any technical help, please feel free to contact needyamin@ansnew.com
