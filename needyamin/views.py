from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.core.paginator import Paginator
from django.utils.text import slugify
import socket, random, os   
from django.contrib import messages

from .models import User,Post,BlogComment, contactus, Email_Subscription, SiteConfig


def index(request):
    if request.method == "POST":
        hostname = socket.gethostname()
        ipaddress = socket.gethostbyname(hostname)
        email = request.POST["email"]
        for needyamin in email:
            if Email_Subscription.objects.filter(email=email).exists():
                messages.success(request, 'You already subscribed to our newsletter')
                return HttpResponseRedirect(("/"))
            else:
                file = Email_Subscription(ip=ipaddress,email=email)
                file.save()
                messages.success(request, 'You successfully subscribe to our newsletter')
                return HttpResponseRedirect(("/"))
    else:
        Post.objects.all()
        needyamin = Post.objects.filter(status='0').order_by('-date')
        paginator = Paginator(needyamin, 6)
        page_number = request.GET.get('page')
        config = paginator.get_page(page_number)
        most_fetch = Post.objects.filter(status='0') #fetch sidebar post
        most_list = list(most_fetch) #Make list to sidebar post list
        most = random.sample(most_list, 4) # Random cycle slidebar
        title = SiteConfig.objects.filter(id='1')
        return render(request, "index.html",
        {"posts": config,
        "sidebar":most,
        "siteconfig":title
        })

#total fetch for /post readers    
def slugs(request,user, slug):
    if request.method == "POST":
        user = request.user
        comment = request.POST['comment']
        hostname = socket.gethostname()
        ipaddress = socket.gethostbyname(hostname)
        date = datetime.today().strftime('%Y-%m-%d')
        me = Post.objects.filter(slug=slug)
        #blog comment
        for needyamin in me:
            if BlogComment.objects.filter(comment=comment).exists():
                messages.success(request, 'Duplicate comments detected')
                return HttpResponseRedirect(("#comment"))
            else:
                file = BlogComment(comment=comment,user=user,post=needyamin,ip=ipaddress,time_posted=date)
                file.save()
                messages.success(request, 'Comment successful')
                return HttpResponseRedirect(("#comment"))


    #if page not found
    if not Post.objects.filter(username=user,slug=slug).exists():
        return render(request,"404.html")
    else:
        title = SiteConfig.objects.filter(id='1')
        #fetch blog comments XXXXXXXXXXXXXXXXXXXXXXXXXXXxx
        p = Post.objects.filter(username=user,slug=slug)
        for post in p:
            post_id = post.id    
        k = BlogComment.objects.filter(post=post_id)
        
        paginator = Paginator(k, 2)
        page_number = request.GET.get('page')
        config = paginator.get_page(page_number)
        #render total templete
        needyamin =  Post.objects.filter(username=user,slug=slug)
        all = Post.objects.filter(status='0')[0:4] #loop sidebar in slugs
        return render(request,"post.html",{
            "fetch": needyamin, 
            "comm_in":config,
            "siteconfig":title,
            "all":all
            })


def user_name(request, user):
    userpost = User.objects.filter(username=user)
    needyamin = Post.objects.filter(status='0',username=user).order_by('-date')
    count_active_post = Post.objects.filter(status='0',username=user).count()
    count_pending_post = Post.objects.filter(status='1',username=user).count()
    paginator = Paginator(needyamin, 5)
    page_number = request.GET.get('page')
    config = paginator.get_page(page_number)
   
    num_visits = request.session.get(user, 0)
    request.session[user] = num_visits + 1

    title = SiteConfig.objects.filter(id='1')
    count_rejected = Post.objects.filter(status='4',username=user).count()

    return render(request,"user.html",
    {"user": userpost,
    "posts":config,
    "count_post":count_active_post,
    "num_visits":num_visits,
    "count_pending_post":count_pending_post,
    "siteconfig":title,
    "count_rejected":count_rejected
    })

def user_profile(request):
    if request.method == "POST":
        user = request.user.id
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        me = User.objects.filter(id=user).update(first_name=first_name,last_name=last_name)
        messages.success(request, 'Your Information Has Been Updated')
        return HttpResponseRedirect(reverse("user_profile"))
    else:
        me = request.user.id
        fetch = User.objects.filter(id=me)
        user = request.user
        count_active = Post.objects.filter(status='0',user=user).count()
        count_pending = Post.objects.filter(status='1',user=user).count()
        count_draft = Post.objects.filter(status='3',user=user).count()
        return render(request,"control/user_profile.html",{
            "fetch":fetch,
            "count_active":count_active,
            "count_pending":count_pending,
            "count_draft":count_draft
            })

def user_profile_email(request):
    if request.method == "POST":
        user = request.user.id
        email = request.POST["email"]
        if User.objects.filter(email=email).exists():
            messages.success(request, 'Email Already Exiests')
            return HttpResponseRedirect(reverse("user_profile"))

        me = User.objects.filter(id=user).update(email=email)
        messages.success(request, 'Your Email Has Been Updated')
        return HttpResponseRedirect(reverse("user_profile"))
    else:
        return render(request,"control/user_profile.html")


def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        title = SiteConfig.objects.filter(id='1')
        return render(request, "login.html",{"siteconfig":title})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def dashboard(request):
    user = request.user
    count_active = Post.objects.filter(status='0',user=user).count()
    count_pending = Post.objects.filter(status='1',user=user).count()
    count_draft = Post.objects.filter(status='3',user=user).count()
    count_rejected = Post.objects.filter(status='4',user=user).count()
    total_users = User.objects.all().order_by('-last_login')[0:15]
    ##visit count
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, "dashboard.html",{
        "count_active":count_active,
        "count_pending":count_pending,
        "count_draft":count_draft,
        "num_visits":num_visits,
        "total_users": total_users,
        "count_rejected":count_rejected
        })

   ## 0 for active
def active_post(request):
    user = request.user
    count_active = Post.objects.filter(status='0',user=user).count()
    count_pending = Post.objects.filter(status='1',user=user).count()
    count_draft = Post.objects.filter(status='3',user=user).count()
    needyamin = Post.objects.filter(status='0',user=user)
    return render(request,"control/active_post.html",{
        "active_post": needyamin,
        "count_draft":count_draft,
        "count_pending":count_pending,
        "count_active":count_active})

   ## 1 for pending
def pending_post(request):
    user = request.user
    count_active = Post.objects.filter(status='0',user=user).count()
    count_pending = Post.objects.filter(status='1',user=user).count()
    count_draft = Post.objects.filter(status='3',user=user).count()
    needyamin = Post.objects.filter(status='1',user=user)
    return render(request,"control/pending_post.html",{
        "pending_post": needyamin,
        "count_draft":count_draft,
        "count_pending":count_pending,
        "count_active":count_active})

    ## 3 for draft
def draft(request):
    user = request.user
    count_active = Post.objects.filter(status='0',user=user).count()
    count_pending = Post.objects.filter(status='1',user=user).count()
    count_draft = Post.objects.filter(status='3',user=user).count()
    needyamin = Post.objects.filter(status='3',user=user)
    return render(request,"control/draft.html",{
        "draft":needyamin,
        "count_draft":count_draft,
        "count_pending":count_pending,
        "count_active":count_active
        })

## Edit Save Post
def draft_edit(request):
    if request.method=="POST":
        id = request.GET.get('id')
        user = request.user
        title = request.POST["post_title"]
        image = request.FILES["image"]
        contents = request.POST["content"]
        date = datetime.today().strftime('%Y-%m-%d')
        tags = request.POST["tags"]
        ftags = tags.split(" ")
        status = request.POST["status"]
        hostname = socket.gethostname()
        ipaddress = socket.gethostbyname(hostname)
        yam = Post.objects.get(id=id)
        if len(request.FILES) != 0:
            if len(yam.image) > 0:
                os.remove(yam.image.path)
            yam.image = request.FILES['image']
            yam.save()
        Post.objects.filter(id=id).update(title=title,contents=contents,date=date,tags=ftags,status=status,ip=ipaddress)

        messages.success(request, 'Your post has been pending or draft. Please check your dashboard')
        return HttpResponseRedirect(("../../draft"))
    else:
        catch = request.GET.get('id')
        user = request.user
        count_draft = Post.objects.filter(status='3',user=user).count()
        count_active = Post.objects.filter(status='0',user=user).count()
        count_pending = Post.objects.filter(status='1',user=user).count()
        show = Post.objects.filter(id=catch,user=user)
        return render(request,"control/draft_edit.html",{
            "show":show,
            "count_draft":count_draft,
            "count_active":count_active,
            "count_pending":count_pending
            }) 

def delete_draft(request):
    id = request.GET.get('id')
    Post.objects.filter(id=id).delete()
    messages.success(request, 'Your Draft Has Been Deleted')
    return HttpResponseRedirect(("../../draft"))

def delete_pending(request):
    id = request.GET.get('active_post_id')
    Post.objects.filter(id=id).delete()
    messages.success(request, 'Your Pending Post Has Been Deleted')
    return HttpResponseRedirect(("../../pending_post"))


## Add New Post
def add_post(request):
    if request.method=="POST":
        user = request.user
        title = request.POST["post_title"]
        slug_k = request.POST["slug"]
        slug = slugify(slug_k)
        username = request.user
        image = request.FILES["image"]
        contents = request.POST["content"]
        date = datetime.today().strftime('%Y-%m-%d')
        tags = request.POST["tags"]
        ftags = tags.split(" ")
        status = request.POST["status"]
        hostname = socket.gethostname()
        ipaddress = socket.gethostbyname(hostname)
        if Post.objects.filter(username=username,slug=slug).exists():
            return render(request,"add_post.html",{"slugdetect":"Slug already exists"})
        else:
             file = Post(user=user,title=title,slug=slug,username=username,image=image,contents=contents,date=date,tags=ftags,status=status,ip=ipaddress)
             file.save()
             count_active = Post.objects.filter(status='0',user=user).count()
             count_pending = Post.objects.filter(status='1',user=user).count()
             count_draft = Post.objects.filter(status='3',user=user).count()
             return render(request,"add_post.html",
             {"message":"Your post has been pending. Our expert will review your content before publish","count_active":count_active,"count_pending":count_pending,"count_draft":count_draft})
    else:
        user = request.user
        count_active = Post.objects.filter(status='0',user=user).count()
        count_pending = Post.objects.filter(status='1',user=user).count()
        count_draft = Post.objects.filter(status='3',user=user).count()
        return render(request,"add_post.html",{
            "count_active":count_active,
            "count_pending":count_pending,
            "count_draft":count_draft
            })
    

def contactus_page(request):
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        file = contactus(name=name,email=email,content=message)
        file.save()
        return render(request, "site/contact_us.html",{"message": "Message Send Successfully"})
    else:
            report_user = request.GET.get('user')
            return render(request,"site/contact_us.html")


def privacy_info(request):
    id = '1'
    fetch = SiteConfig.objects.filter(id=id)
    return render(request,"site/privacy.html",{"fetch":fetch})

def aboutus(request):
    id = '1'
    fetch = SiteConfig.objects.filter(id=id)
    return render(request,"site/aboutus.html",{"fetch":fetch})

def site_map(request):
    needyamin = Post.objects.filter(status='0')
    return render(request,"site/sitemap.html",{"fetch": needyamin})

def search(request):
    m = request.GET.get('q')
    search = Post.objects.filter(title=m).count()
    All_Users = User.objects.all()
    All_Post = Post.objects.filter(status="0")
    All_Comments = BlogComment.objects.all()
    return render(request,'site/search.html',{
        "search":search,
        "q": m,
        "All_Users":All_Users,
        "All_Post":All_Post,
        "All_Comments":All_Comments
        })


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        title = SiteConfig.objects.filter(id='1')
        return render(request, "register.html",{"siteconfig":title})

##############################  FOR ADMIN PANEL ######################################################################
#######################################################################################################################

def siteadmin(request):
    count_active = Post.objects.filter(status='0').count()
    count_pending = Post.objects.filter(status='1').count()
    count_draft = Post.objects.filter(status='3').count()
    count_rejected = Post.objects.filter(status='4').count()
    subscriber = Email_Subscription.objects.all().count()
    return render(request,"siteadmin/index.html",{
        "count_active":count_active,
        "count_pending":count_pending,
        "count_draft":count_draft,
        "subscriber":subscriber,
        "count_rejected":count_rejected
    })



def admin_pending(request):
    count_pending = Post.objects.filter(status='1').count()
    needyamin = Post.objects.filter(status='1')
    subscriber = Email_Subscription.objects.all()
    count_subscriber = Email_Subscription.objects.all().count()
    return render(request,"siteadmin/admin_pending.html",{
        "pending_post": needyamin,
        "count_pending":count_pending,
        "subscriber":subscriber,
        "count_subscriber":count_subscriber
        })
    

def admin_subscriber(request):
    needyamin = Email_Subscription.objects.all()
    count_pending = Post.objects.filter(status='1').count()
    needyamin = Post.objects.filter(status='1')
    subscriber = Email_Subscription.objects.all()
    count_subscriber = Email_Subscription.objects.all().count()
    return render(request,"siteadmin/admin_subscriber.html",{
        "subscriber":needyamin,
        "count_pending":count_pending,
        "subscriber":subscriber,
        "count_subscriber":count_subscriber
        })

def site_config(request):
    if request.method=="POST":
        id = "1"
        title = request.POST["title"]
        keywords = request.POST["keywords"]
        description = request.POST["description"]
        script_add = request.POST["script_add"]
        SiteConfig.objects.filter(id=id).update(title=title,keywords=keywords,description=description,script_add=script_add)
        messages.success(request, 'Site Configuration Has Been Updated...')
        return HttpResponseRedirect(("site_config"))
    else:
        fetch = SiteConfig.objects.all()
        count_pending = Post.objects.filter(status='1').count()
        subscriber = Email_Subscription.objects.all()
        count_subscriber = Email_Subscription.objects.all().count()
        return render(request,"siteadmin/site_config.html",{
            "fetch":fetch,
             "count_pending":count_pending,
             "subscriber":subscriber,
             "count_subscriber":count_subscriber
            })

def admin_favicon(request):
    if request.method=="POST":
        id = "1"
        yam = SiteConfig.objects.get(id=id)
        if len(request.FILES) != 0:
            if len(yam.favourite_icon) > 0:
                os.remove(yam.favourite_icon.path)
                yam.favourite_icon = request.FILES['favourite_icon']
                yam.save()
                messages.success(request, 'Favicon Has Been Updated...')
                return HttpResponseRedirect(("../../site_config"))
 
    return HttpResponseRedirect(("../../site_config"))
 


def admin_delete_draft(request):
    id = request.GET.get('id')
    Post.objects.filter(id=id).delete()
    messages.success(request, 'Post Has Been Deleted')
    return HttpResponseRedirect(("pending"))


def admin_approve_draft(request):
    id = request.GET.get('id')
    Post.objects.filter(id=id).update(status='0')
    messages.success(request, 'Post Has Been approved')
    return HttpResponseRedirect(("pending"))

def admin_rejected_draft(request):
    id = request.GET.get('id')
    Post.objects.filter(id=id).update(status='4')
    messages.success(request, 'Post Has Been Rejected')
    return HttpResponseRedirect(("pending"))

def admin_delete_subscriber(request):
    id = request.GET.get('id')
    Email_Subscription.objects.filter(id=id).delete()
    messages.success(request, 'Email Subscription Has Been Deleted')
    return HttpResponseRedirect(("subscriber"))

def site_pages(request):
    id = '1'
    fetch = SiteConfig.objects.filter(id=id)
    count_pending = Post.objects.filter(status='1').count()
    count_subscriber = Email_Subscription.objects.all().count()
    return render(request,"siteadmin/site_pages.html",{
        "fetch":fetch,
        "count_pending":count_pending,
        "count_subscriber":count_subscriber
        })

def admin_update_privacy(request):
    id = '1'
    content_privacy = request.POST['content_privacy']
    SiteConfig.objects.filter(id=id).update(privacy=content_privacy)
    messages.success(request, 'Privacy Policy Has Been Updated')
    return HttpResponseRedirect(("../site_pages"))

def admin_update_about_us(request):
    id = '1'
    content_about_us = request.POST['content_about_us']
    SiteConfig.objects.filter(id=id).update(aboutus=content_about_us)
    messages.success(request, 'About Us Has Been Updated')
    return HttpResponseRedirect(("../site_pages"))