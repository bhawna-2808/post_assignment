Part 1: Coding and Framework Understanding
Question 1: Models and QuerySets
● Objective: Create a Post model and retrieve specific entries using Django ORM. ● Task:
● Define a Django model named Post with specified fields.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)


● Write a queryset to retrieve all posts authored by "admin" and are
published.
ans. 
from django.db.models import Q

admin_posts = Post.objects.filter(
    Q(author__is_admin=True) & Q(author__email='admin') & Q(published=True)
)


Question 2: Forms and Validation
● Objective: Implement a Django form with custom validation. 
● Task:
● Create a Django form for the Post model.
ans. - 
in forms.py - 

from django import forms
from .models import *
from datetime import timezone
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'published_date']

    def clean_published_date(self):
        published_date = self.cleaned_data.get('published_date')
        if published_date and published_date > timezone.now():
            raise forms.ValidationError("Published date cannot be in the future.")
        return published_date
    
    views.py - 
    def createform(request, pk=None, is_delete=0):
        form = PostForm(request.POST or None)
        message = "Post Added Successfully !!"
        if pk is not None and is_delete == 0:
            createid_ins = CreateId.objects.get(pk=pk)
            form = PostForm(
                request.POST or None, instance=createid_ins
            )
            message = "Post Updated Successfully !!"
        elif pk is not None and is_delete != 0:
            Post.objects.filter(pk=pk).delete()
            message = "Post Deleted Successfully !!"
            # messages.success(request, message)
            return redirect("post-list")
        if form.is_valid():
            form.save()
            # messages.success(request, message)
            return redirect("post-list")

    context = {
        "form": form,
    }
    return render(request, "post/add_post.html", context)  
    
Part 2: Deployment Skills

Question 3: Django Application Deployment
● Objective: Describe the deployment process for a Django application using Gunicorn and Nginx.
aNS. -     
1.Prepare Application: Make sure your Django app is ready for deployment, including database setup and static files handling.
2. Install Gunicorn and Nginx: Use package managers to install Gunicorn, Nginx, and other dependencies.
3. Configure Gunicorn: Create a systemd service file for Gunicorn to manage your Django app.
4. Start Gunicorn Service: Start and enable the Gunicorn service to run your Django app.
5. Configure Nginx: Set up an Nginx server block to proxy requests to Gunicorn.
6. Enable Nginx Server Block: Link the Nginx server block configuration and test the Nginx configuration.
7. Restart Nginx: Restart Nginx to apply the changes.
8. Adjust Django Settings: Update Django settings like ALLOWED_HOSTS to work with the new environment.

● Task:
● Outline the step-by-step process required to deploy a Django application
on a Linux server.

Ans. - AWS- 1 cd downloads then chmod 400 bb.pem and ssh cmd copy from aws connect
2. sudo apt update
3. sudo apt install python3-pip python3-dev nginx
4. sudo pip3 install virtualenv 
5. sudo apt install python3-virtualenv
6. sudo apt install postgresql postgresql-contrib
7. sudo -i -u postgres
8. psql 
9. \q
10. create user venn with encrypted password 'venn!2024';
11. create database venn;
12. GRANT ALL PRIVILEGES ON database venn to venn;


