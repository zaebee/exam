from django.conf import settings
import os


APP_PATH = os.path.abspath(os.path.dirname(__file__))

CONFIG_FILE = getattr(settings, 'DYNAMIC_CONFIG_FILE', os.path.join(APP_PATH, "config.xml"))
MAX_LENGHT_CHAR = getattr(settings, 'DYNAMIC_MAX_LENGHT_CHAR', 80)
MAX_LENGHT_INT = getattr(settings, 'DYNAMIC_MAX_LENGHT_INT', 5)
