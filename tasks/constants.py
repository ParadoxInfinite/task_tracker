# Non-Django file to store the constants like choices for ChoiceFields.
# Ex: Status of the task OR Permission Groups/Roles for admins to change[Yet to be impletemented].

# TODO: Permissions for the entire app, superuser, staff, user etc.

task_status_choices = (
    ('idea', 'Idea'),
    ('todo', 'TODO'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed')
)

task_priority_choices = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    ('critical', 'Critical')
)