==================================
Proposed Layout for Pinax Settings
==================================

The current settings layout for Pinax projects is based off the standard
``settings.py`` that comes with Django. It adds to it importing ``local_settings.py``
to allow you to override settings based on your environment.

I believe that the current layout has a couple flaws, of which are:

* All Settings exist in one file. This makes for a long file which can be
    difficult to tell why a particular setting is being set, and who is setting it.
* You cannot refer to the baseline settings inside of ``local_settings.py``. In
    practice this means that if you want to add an application to only your local
    environment you need to either modify ``settings.py`` and be careful to not
    commit your changed, or copy the ``INSTALLED_APPS`` from settings.py into
    ``local_settings.py`` and make sure that you keep this list synchronized with
    the one in ``settings.py``.
* If you do split out settings into multiple files, they all pollute the
    project directory.

I believe that a solution to this problem is settings as a module. I have included
an example of this within this repository. The individual settings files and
arrangement are not set in stone, but the general idea is well expressed I think.

------------
Key Concepts
------------

The basic idea with settings as a module is to import a module called ``settings``
instead of a file called ``settings.py``. Inside of the module you have various
settings files each serving various purposes. I have included an example that
has the following:

1. ``project.settings.base`` - This file contains only the most basic settings
    that all the other settings might require. In my example it is only the ``DEBUG``
    and ``TEMPLATE_DEBUG`` settings.
2. ``project.settings.paths`` - This file contains the various ``PROJECT_DIR``
    and ``PINAX_ROOT`` variables. This could be merged in with ``project.settings.base``.
3. ``project.settings.django`` - This file contains Django specific settings
    that deals with Django and Django Contrib Apps settings.
4. ``project.settings.pinax`` - This file contains any settings that comes
    from Pinax or a Pinax installed application. It might also change any Django
    related setting that is a Pinax requirement.
5. ``project.settings.project`` - This file contains project overrides and
    any settings for the project. In general most people will be modifying this
    file and from here they can import any of the files 1-4.
6. ``project.settings.local`` - This file is the replacement for ``local_settings.py``,
    however unlike the current solution, you can reference values from any of the
    other settings files in it. For example::

        from project.settings.base import DEBUG
        from project.settings.project import INSTALLED_APPS

        if DEBUG:
            INSTALLED_APPS += ["devserver"]

The bulk of the work comes from project/settings/__init__.py, This is a simple
file that merely imports all the other files in my example it looks like::

    # Base Settings
    from pinax_settings.settings.base import *

    # Django Settings; Things that deal directly with Django and it's apps
    from pinax_settings.settings.django import *

    # Pinax Settings (anything Pinax Overrides or Sets by Default)
    from pinax_settings.settings.pinax import *

    # Project Settings (Anything Specific to this Project)
    from pinax_settings.settings.project import *

    # settings/local.py can be used to override environment-specific settings
    # like database and email that differ between development and production.
    try:
        from pinax_settings.settings.local import *
    except ImportError:
        pass

If you wanted to customize the order, or if you wanted to automatically load a
different file based on an environment variable, machine name, or any other
method either Pinax, or the end developers could customize this file in order
to provide that logic. For example you might load a different module besides
``project.settings.local`` based on an environment variable (maybe ``PINAX_ENVIRONMENT_NAME``).

----------
Advantages
----------

This solves all of the points I've raised with the existing layout. Specifically it:

* Allows you to organize your settings amongst multiple files, allowing you
    to organize it by what level of framework the setting comes from.
* Keeps the project directory from getting a lot of settings files in it to
    support multiple settings files.
* Allows you to refer to variables from other settings files without causing
    a circular import.

Additionally, it does not conceptually move the location of the settings. So as far
as Python, Django, and Pinax (or any other tool) is concerned the settings still
exist at ``project.settings``. I believe it also makes sense for a new programming
coming in. "I'm looking for where this project is loading it's settings, oh a folder
called settings".

-------------
Disadvantages
-------------

The only real disadvantage I can think of is that you have to adjust ``PROJECT_DIR``
to reflect the fact that settings now exist one level below the project directory.
This would also effect any other tool that is trying to determine the project
directory from the location of ``project.settings.__file__``.