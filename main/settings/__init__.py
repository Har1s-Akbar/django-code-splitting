from split_settings.tools import include
from decouple import config
import os

if 'dev' == config('PROJ_STATE'):
    include('development.py')
elif 'stag' == config('PROJ_STATE'):
    include('staging.py')