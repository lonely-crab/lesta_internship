import os


def locate_root_folder(file: str) -> str:
    return os.path.dirname(os.path.abspath(file))


def locate_template_folder(root_folder: str, templates_folder: str) -> str:
    return os.path.join(root_folder, templates_folder)