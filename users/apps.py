from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

# to ensure automatic signal registration for profile to be added to new users without the User model and Profile model being tightly coupled
    # Override the ready method to perform initialization tasks
    def ready(self):
        # Importing the signals module to register signal handlers
        import users.signals
        # Ensures that the signals are imported and registered when the app is ready
        print("Users app is ready and signals are registered.")
        
