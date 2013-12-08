import os

app_home_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(app_home_dir, "templates")

settings = {
    "debug": True,
    "template_path": template_dir
}

settings_app = {
    "app_py_dir": os.path.join(app_home_dir, "py"),
    "app_lib_dir": os.path.join(app_home_dir, "lib"),
    "static_file_dir": os.path.join(app_home_dir, "media"),
    "db_url": "mongodb://localhost:27017",
    "index_page": "index.html",
    "page_size": 20,
    "db_name": "crm"
}
