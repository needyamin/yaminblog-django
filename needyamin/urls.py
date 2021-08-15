from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:user>/<str:slug>", views.slugs, name="slug"),
    path("<str:user>/", views.user_name, name="user_name"),
    path("dashboard/user_profile/", views.user_profile, name="user_profile"),
    path("dashboard/user_profile/passwords/", auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('user_profile'))),
    path("dashboard/user_profile/email/", views.user_profile_email, name="user_profile_email"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("dashboard/deletedraft/", views.delete_draft, name="delete_draft"),
    path("dashboard/deletepending/", views.delete_pending, name="delete_pending"),
    path("dashboard/siteadmin/", views.siteadmin, name="siteadmin"),
    path("add_post", views.add_post, name="add_post"),
    path("active_post", views.active_post, name="active_post"),
    path("pending_post", views.pending_post, name="pending_post"),
    path("draft", views.draft, name="draft"),
    path("draft/edit/", views.draft_edit, name="draft_edit"),
    path("contact_us", views.contactus_page, name="contactus"),
    path("privacy", views.privacy_info, name="privacy"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("sitemap", views.site_map, name="sitemap"),
    path("search", views.search, name="search"),
    path("dashboard/siteadmin/pending", views.admin_pending, name="admin_pending"),
    path("dashboard/siteadmin/admin_delete_draft", views.admin_delete_draft, name="admin_delete_draft"), #admin delete
    path("dashboard/siteadmin/admin_approve_draft", views.admin_approve_draft, name="admin_approve_draft"), #admin approve
    path("dashboard/siteadmin/admin_rejected_draft", views.admin_rejected_draft, name="admin_rejected_draft"), #admin reject
    path("dashboard/siteadmin/admin_delete_subscriber", views.admin_delete_subscriber, name="admin_delete_subscriber"),
    path("dashboard/siteadmin/subscriber", views.admin_subscriber, name="admin_subscriber"),
    path("dashboard/siteadmin/site_config", views.site_config, name="site_config"),
    path("dashboard/siteadmin/site_pages", views.site_pages, name="site_pages"), #site_pages
    path("dashboard/siteadmin/site_pages/privacyupdate", views.admin_update_privacy, name="admin_update_privacy"), #admin_update_privacy
    path("dashboard/siteadmin/site_pages/aboutusupdate", views.admin_update_about_us, name="admin_update_about_us"), #admin_update_about_us
    path("dashboard/siteadmin/site_config/admin_favicon/", views.admin_favicon, name="admin_favicon"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
