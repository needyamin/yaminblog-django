from django.contrib import admin

from .models import User, Post, contactus, SiteConfig, Email_Subscription, BlogComment
admin.site.register(User)
admin.site.register(Post)
admin.site.register(contactus)
admin.site.register(SiteConfig)
admin.site.register(Email_Subscription)
admin.site.register(BlogComment)