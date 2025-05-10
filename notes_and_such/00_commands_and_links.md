# Commands and Links

## Commands

### Git Commands
- `git init`: Initialize a new Git repository.
- `git clone <repository_url>`: Clone a remote repository to your local machine.
- `git add <file>`: Stage changes for commit.
- `git add .`: Stage all changes in the current directory.
- `git commit -m "<commit_message>"`: Commit staged changes with a message.
- `git status`: Show the status of the working directory and staging area.
- `git log`: Show the commit history.
- `git branch`: List all branches in the repository.
- `git branch <branch_name>`: Create a new branch.
- `git checkout <branch_name>`: Switch to a different branch.
- `git checkout -b <branch_name>`: Create and switch to a new branch.
- `git merge <branch_name>`: Merge changes from one branch into the current branch.
- `git pull`: Fetch and merge changes from the remote repository.
- `git push`: Push local changes to the remote repository.
- `git remote add <name> <repository_url>`: Add a new remote repository.
- `git remote -v`: Show the remote repositories associated with the local repository.
- `git fetch`: Fetch changes from the remote repository without merging.
- `git reset --hard HEAD`: Discard all local changes and reset to the last commit.
- `git reset HEAD~1`: Undo the last commit but keep the changes in the working directory.
- `git stash`: Stash changes in the working directory.
- `git stash pop`: Apply the stashed changes back to the working directory.
- `git cherry-pick <commit_hash>`: Apply changes from a specific commit to the current branch.
- `git rebase <branch_name>`: Reapply commits on top of another base branch.
- `git tag <tag_name>`: Create a new tag for a specific commit.
- `git show <tag_name>`: Show details of a specific tag.
- `git diff`: Show changes between the working directory and the last commit.
- `git diff <commit_hash>`: Show changes between the working directory and a specific commit.
- `git diff --cached`: Show changes between the staging area and the last commit.
- `git rm <file>`: Remove a file from the working directory and stage the removal for commit.
- `git mv <old_file> <new_file>`: Rename a file and stage the change for commit.
- `git config --global user.name "<name>"`: Set the global username for Git commits.
- `git config --global user.email "<email>"`: Set the global email for Git commits.
- `git config --global core.editor "<editor>"`: Set the default editor for Git commit messages.
- `git config --global alias.<alias_name> <command>`: Create a Git alias for a command.
- `git config --list`: List all Git configuration settings.
- `git reflog`: Show a log of all actions taken in the repository, including commits and checkouts.

### Django Commands
- `python manage.py drf_create_token <username>`: Create a token for a user.
- `python manage.py runserver`: Start the development server.
- `python manage.py makemigrations`: Create new migrations based on the changes you have made to your models.
- `python manage.py migrate`: Apply the migrations to the database.
- `python manage.py createsuperuser`: Create a superuser account for the admin interface.
- `python manage.py shell`: Open a Python shell with Django context.
- `python manage.py collectstatic`: Collect static files into the STATIC_ROOT directory.
- `python manage.py dumpdata`: Output the contents of the database as JSON.
- `python manage.py loaddata`: Load data from a JSON file into the database.
- `python manage.py test`: Run the tests for your Django application.
- `python manage.py startapp <app_name>`: Create a new Django app.
- `python manage.py startproject <project_name>`: Create a new Django project.
- `python manage.py createsuperuser --email admin@email.app --username admin`: Create a superuser account with email and username.
- `python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp`: Create a superuser account with email and username.
- `python manage.py changepassword <username>`: Change the password for a user.

## Links

### Localhost
- [http://LOCALHOST:8000/](http://LOCALHOST:8000/): Access the main page of the application.
- [http://LOCALHOST:8000/admin/](http://LOCALHOST:8000/admin/): Access the Django admin interface.
- [http://LOCALHOST:8000/notes/](http://LOCALHOST:8000/notes/):
- [http://LOCALHOST:8000/api/](http://LOCALHOST:8000/api/):

### Django Admin
- [Django Admin](http://LOCALHOST:8000/admin/): Access the Django admin interface.
- [Django Admin - Superuser](http://LOCALHOST:8000/admin/auth/user/): Access the user management section of the Django admin interface.
- [Django Admin - Groups](http://LOCALHOST:8000/admin/auth/group/): Access the groups management section of the Django admin interface.
- [Django Admin - Permissions](http://LOCALHOST:8000/admin/auth/permission/): Access the permissions management section of the Django admin interface.
- [Django Admin - Sessions](http://LOCALHOST:8000/admin/sessions/session/): Access the sessions management section of the Django admin interface.
- [Django Admin - Sites](http://LOCALHOST:8000/admin/sites/site/): Access the sites management section of the Django admin interface.

### Resources

- [How to deploy Django](https://docs.djangoproject.com/en/5.2/howto/deployment/)

## Commands and Results

### `python manage.py check --deploy`
This command checks the Django project for common deployment issues. It is important to run this command before deploying your Django application to ensure that it is secure and properly configured.

```ps
PS C:\Users\FlynntKnapp\Programming\django-base-app-example> python manage.py check --deploy 
System check identified some issues:

WARNINGS:
?: (security.W004) You have not set a value for the SECURE_HSTS_SECONDS setting. If your entire site is served only over SSL, you may want to consider setting a value and enabling HTTP Strict Transport Security. Be sure to read the documentation first; enabling HSTS carelessly can cause serious, irreversible problems.
?: (security.W008) Your SECURE_SSL_REDIRECT setting is not set to True. Unless your site should be available over both SSL and non-SSL connections, you may want to either set this setting True or configure a load balancer or reverse-proxy server to redirect all connections to HTTPS.
?: (security.W009) Your SECRET_KEY has less than 50 characters, less than 5 unique characters, or it's prefixed with 'django-insecure-' indicating that it was generated automatically by Django. Please generate a long and random value, otherwise many of Django's security-critical features will be vulnerable to attack.
?: (security.W012) SESSION_COOKIE_SECURE is not set to True. Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
?: (security.W016) You have 'django.middleware.csrf.CsrfViewMiddleware' in your MIDDLEWARE, but you have not set CSRF_COOKIE_SECURE to True. Using a secure-only CSRF cookie makes it more difficult for network traffic sniffers to steal the CSRF token.
?: (security.W018) You should not have DEBUG set to True in deployment.
?: (security.W020) ALLOWED_HOSTS must not be empty in deployment.

System check identified 7 issues (0 silenced).
PS C:\Users\FlynntKnapp\Programming\django-base-app-example>
```