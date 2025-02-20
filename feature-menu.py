# this will be used for the feature terminal menu code
import time
import sys

class Menu:
    def __init__(self, name, uuid, apps):
        """Initialization of the menu class

        Args:
            name (Str): Name of the user
            uuid (int): Unique user identifier
            apps (dict[App name: inst]): List of instances of all apps on the phone #FIXME make so the instances are made once the user starts them not before
        """

        self._name = name
        self._uuid = uuid
        self._apps = apps

    @property
    def name(self):
        return self._name

    @staticmethod
    def fancy_type(text, delay=0.05):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def display(self):
        """Display and choice making part of the menu

        Returns:
            int: Number corasponding to app they want to open
        """
        self.fancy_type('Hello ' + str(self.name))
        self.fancy_type(f'Which app do you want to use?')
        app_names = list(self._apps.keys())
        for i in range(1, len(app_names)+1):
            self.fancy_type(f'{i}. {app_names[i-1]}')
        choice = input()
        return choice
    
app_dict = {
    'calc': 'Calc inst',
    'contacts': 'Contact inst'
}
display = Menu('Jason',1, app_dict)
display.display()
