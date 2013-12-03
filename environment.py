import sys
import os

import settings

_app_python_dir = [
        settings.settings_app["app_py_dir"],
        settings.settings_app["app_lib_dir"]
]

_app_egg_dir = [os.path.join(settings.settings_app["app_lib_dir"], egg) 
        for egg in os.listdir(settings.settings_app["app_lib_dir"]) 
        if len(egg) > 4 and egg[len(egg) - 4:] == ".egg" 
        and os.path.isfile(os.path.join(settings.settings_app["app_lib_dir"], egg))]

sys.path.extend(_app_python_dir)
sys.path.extend(_app_egg_dir)
