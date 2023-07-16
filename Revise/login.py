import cgi
import os

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

# Perform login authentication logic here
# Replace the following code with your actual authentication logic
if username == 'student' and password == 'student123':
    role = 'student'
    authenticated = True
elif username == 'teacher' and password == 'teacher123':
    role = 'teacher'
    authenticated = True
elif username == 'admin' and password == 'admin123':
    role = 'admin'
    authenticated = True
else:
    authenticated = False

# Redirect to appropriate page based on user role
if authenticated:
    if role == 'student':
        print("Content-Type: text/html")
        print("Location: student_dashboard.html")
        print()
    elif role == 'teacher':
        print("Content-Type: text/html")
        print("Location: teacher_dashboard.html")
        print()
    elif role == 'admin':
        print("Content-Type: text/html")
        print("Location: admin_dashboard.html")
        print()
else:
    print("Content-Type: text/html")
    print("Location: login.html")
    print()
