# Store the User class in one module, and store the Privileges and Admin classes in a separate module.
# In a separate file, create an Admin instance and call show_privileges() to show that everything is working properly.
from practice_privilege_admin import Privileges, Admin

admin = Admin('user', 'admin', 'AdminAdmin', 'admin@email.com', 555-963-6549)
admin.privileges.show_privileges()