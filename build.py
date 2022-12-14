#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.integrationtest")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

name = "sece"
default_task = "publish"


@init
def set_properties(project):
    project.set_property("distutils_console_scripts", ["sece = main:main"])
    project.set_property("integrationtest_inherit_environment", True)
