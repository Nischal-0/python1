import cgi

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')
role = form.getvalue('role')

# Perform sign-up logic here
# Replace the following code with your actual sign-up logic
# You may need to store the username, password, and role in a database
# and perform appropriate validations and checks
# Here, we assume a successful sign-up and redirect to the login page

print("Content-Type: text/html")
print("Location: login.html")
print()
