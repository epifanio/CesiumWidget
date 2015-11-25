# -*- coding: utf-8 -*-
"""
CesiumWidget
====

A Cesiumjs widget for the Ipython notebook, forked from https://github.com/petrushy/CesiumWidget.

.. _CesiumWidget: https://github.com/epifanio/CesiumWidget
.. _Cesiumjs: http://cesiumjs.org/
"""

from distutils.core import setup
import os
import sys
import subprocess
from jupyter_core.paths import jupyter_config_dir, jupyter_data_dir
import shutil

from os.path import expanduser

if sys.version_info[:2] < (2, 6) or (3, 0) <= sys.version_info[0:2] < (3, 2):
    raise RuntimeError("Python version 2.6, 2.7 or >= 3.2 required.")

if sys.version_info[0] >= 3:
    import builtins
else:
    import __builtin__ as builtins


def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f),
                                    os.path.join(dest, f),
                                    ignore)
    else:
        shutil.copyfile(src, dest)


if len(sys.argv) == 2 and sys.argv[1] == "install":
    print("Installing Jupyter notebook extensions in the user home as default")
    destdir=os.path.join(jupyter_config_dir(),'nbextensions','CesiumWidget')
    print("The CesiumWidget will be in the user directory %s " % destdir)
    recursive_overwrite(src='./CesiumWidget/', dest=destdir)

if "all" in sys.argv:
    destdir='/usr/local/share/jupyter/nbextensions/'
    print("The CesiumWidget will be installed for all users in %s needs root access" % destdir)
    recursive_overwrite(src='./CesiumWidget/', dest=destdir)
    sys.argv.remove("all")

if "user" in sys.argv:
    home = expanduser("~")
    destdir=os.path.join(jupyter_data_dir(),'nbextensions','CesiumWidget')
    print("The CesiumWidget will be in the user directory %s " % destdir)
    recursive_overwrite(src='./CesiumWidget/', dest=destdir)
    sys.argv.remove("user")





CLASSIFIERS = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Topic :: Software Development
Topic :: Scientific/Engineering
Operating System :: Unix
Operating System :: MacOS
"""
AUTHOR = 'epinux'
MAJOR = 0
MINOR = 1
MICRO = 0
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)


sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))


def git_version():
    def _minimal_ext_cmd(cmd):
        # construct minimal environment
        env = {}
        for k in ['SYSTEMROOT', 'PATH']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(cmd, stdout = subprocess.PIPE, env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(['git', 'rev-parse', 'HEAD'])
        GIT_REVISION = out.strip().decode('ascii')
    except OSError:
        GIT_REVISION = "Unknown"
    #print(GIT_REVISION)
    return GIT_REVISION

GIT_REVISION = git_version()

# BEFORE importing distutils, remove MANIFEST. distutils doesn't properly
# update it when the contents of directories change.
if os.path.exists('MANIFEST'): os.remove('MANIFEST')

def get_version_info():
    # Adding the git rev number needs to be done inside write_version_py(),
    # otherwise the import of numpy.version messes up the build under Python 3.
    FULLVERSION = VERSION
    #if os.path.exists('.git'):
    GIT_REVISION = git_version()
    if not ISRELEASED:
        FULLVERSION += '.dev-' + GIT_REVISION[:7]

    return FULLVERSION, GIT_REVISION


def write_version_py(filename='CesiumWidget/version.py'):
    cnt = """
# THIS FILE IS GENERATED FROM CesiumWidget SETUP.PY
short_version = '%(version)s'
version = '%(version)s'
full_version = '%(full_version)s'
git_revision = '%(git_revision)s'
release = %(isrelease)s

if not release:
    version = full_version
"""
    FULLVERSION, GIT_REVISION = get_version_info()

    a = open(filename, 'w')
    try:
        a.write(cnt % {'author' : AUTHOR,
                       'version': VERSION,
                       'full_version' : FULLVERSION,
                       'git_revision' : GIT_REVISION,
                       'isrelease': str(ISRELEASED)})
    finally:
        a.close()


#with open('README.md') as file:
#    long_description = file.read()


write_version_py()

    
setup(
    name = 'CesiumWidget',
    version = '0.1.0',
    description = 'A Cesiumjs widget for the IPython notebook',
    #long_description=long_description,
    author = 'Massimo Di Stefano, Petrus Hyvonen',
    #author_unixid = 'epinux',
    author_email = 'epiesasha@me.com, petrus.hyvonen@gmail.com',
    url = 'https://github.com/epifanio/CesiumWidget',
    packages = ['CesiumWidget'],
    #package_dir = {'': 'lib'},
    license = 'Apache',
    platforms = ["Linux", "Mac OS-X", "Unix"],
    classifiers = [
        'Development Status :: 1 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Operating System :: UNIX based systems',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
)
