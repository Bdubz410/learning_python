# Start with your work from page 173. Store the classes User, Privileges, and Admin classes in a separate module.
# In a separate file, create an Admin instance and call show_privileges() to show that everything is working correctly.
from privileges import User, Privileges, Admin

admin = Admin('user', 'admin', 'AdminAdmin', 'admin@email.com', 555-452-9523)
admin.privileges.show_privileges()