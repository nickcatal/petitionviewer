#!/usr/bin/env python
"""Management file for We the People Petition Viewer"""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whresponse.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
