from __future__ import print_function
from setuptools import setup, find_packages, Command
from setuptools.command.egg_info import egg_info
from subprocess import check_call
import os
import sys
import platform

here = os.path.abspath(os.path.dirname(__file__))

LONG_DESCRIPTION = """
CesiumWidget
====

A Cesiumjs widget for the Ipython notebook, forked from https://github.com/petrushy/CesiumWidget.

.. _CesiumWidget: https://github.com/epifanio/CesiumWidget
.. _Cesiumjs: http://cesiumjs.org/

"""

try:
    from shutil import which
except ImportError:
    # The which() function is copied from Python 3.4.3
    # PSF license version 2 (Python Software Foundation License Version 2)
    def which(cmd, mode=os.F_OK | os.X_OK, path=None):
        """Given a command, mode, and a PATH string, return the path which
        conforms to the given mode on the PATH, or None if there is no such
        file.
        `mode` defaults to os.F_OK | os.X_OK. `path` defaults to the result
        of os.environ.get("PATH"), or can be overridden with a custom search
        path.
        """
        # Check that a given file can be accessed with the correct mode.
        # Additionally check that `file` is not a directory, as on Windows
        # directories pass the os.access check.
        def _access_check(fn, mode):
            return (os.path.exists(fn) and os.access(fn, mode)
                    and not os.path.isdir(fn))

        # If we're given a path with a directory part, look it up directly rather
        # than referring to PATH directories. This includes checking relative to the
        # current directory, e.g. ./script
        if os.path.dirname(cmd):
            if _access_check(cmd, mode):
                return cmd
            return None

        if path is None:
            path = os.environ.get("PATH", os.defpath)
        if not path:
            return None
        path = path.split(os.pathsep)

        if sys.platform == "win32":
            # The current directory takes precedence on Windows.
            if not os.curdir in path:
                path.insert(0, os.curdir)

            # PATHEXT is necessary to check on Windows.
            pathext = os.environ.get("PATHEXT", "").split(os.pathsep)
            # See if the given file matches any of the expected path extensions.
            # This will allow us to short circuit when given "python.exe".
            # If it does match, only test that one, otherwise we have to try
            # others.
            if any(cmd.lower().endswith(ext.lower()) for ext in pathext):
                files = [cmd]
            else:
                files = [cmd + ext for ext in pathext]
        else:
            # On other platforms you don't have things like PATHEXT to tell you
            # what file suffixes are executable, so just pass on cmd as-is.
            files = [cmd]

        seen = set()
        for dir in path:
            normdir = os.path.normcase(dir)
            if not normdir in seen:
                seen.add(normdir)
                for thefile in files:
                    name = os.path.join(dir, thefile)
                    if _access_check(name, mode):
                        return name
        return None


version_ns = {}
with open(os.path.join(here, 'CesiumWidget', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

setup_args = {
    'name': 'CesiumWidget',
    'version': version_ns['__version__'],
    'description': 'A Cesiumjs widget for the IPython notebook.',
    'long_description': LONG_DESCRIPTION,
    'License': 'Apache',
    'include_package_data': True,
    'install_requires': ['ipywidgets', 'czml'],
    'packages': find_packages(),
    'zip_safe': False,
    'author': 'Petrus Hyvonen <petrus.hyvonen@gmail.com>, Massimo Di Stefano <epiesasha@me.com>',
    'author_email': 'petrus.hyvonen@gmail.com, epiesasha@me.com',
    'url': 'https://github.com/epifanio/CesiumWidget',
    'keywords': [
        'ipython',
        'jupyter',
        'widgets',
        'graphics',
        'plotting',
        'cesiumjs',
    ],
    'classifiers': [
        'Development Status :: 1 - Alfa',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Multimedia :: Graphics',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
}

setup(**setup_args)