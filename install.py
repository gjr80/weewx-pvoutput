"""
This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details.

                 Installer for PVOutput Uploader extension

Version: 0.4.1                                        Date: 18 August 2022

Revision History
    18 August 2022      v0.4.1
        - installer config is now presented as a triple quote string
        - minor formatting changes
    8 March 2020        v0.4.0
        - version number change only
    3 February 2018     v0.3.1
        - minor comment reworking
    1 February 2018     v0.3.0
        - initial implementation as an extension
"""

# python imports
import configobj

from distutils.version import StrictVersion
from setup import ExtensionInstaller

# import StringIO, use six.moves due to python2/python3 differences
from six.moves import StringIO

# WeeWX imports
import weewx


REQUIRED_VERSION = "3.7.0"
PVOUTPUT_VERSION = "0.4.1"
# define our config as a multiline string so we can preserve comments
pvoutput_config = """
[StdRESTful]

    [[PVOutput]]
        # This section is for the PVOutput.org RESTful uploader.
        
        # the PVOutput system ID
        system_id = ENTER_PVOUTPUT_SYSTEM_ID_HERE
        
        # the PVOutput API key to be used
        api_key = ENTER_PVOUTPUT_API_KEY_HERE
        
        # enable the uploader
        enable = false
"""

# construct our config dict
pvoutput_dict = configobj.ConfigObj(StringIO(pvoutput_config))


def loader():
    return PVOutputInstaller()


class PVOutputInstaller(ExtensionInstaller):
    def __init__(self):
        if StrictVersion(weewx.__version__) < StrictVersion(REQUIRED_VERSION):
            msg = "%s requires WeeWX %s or greater, found %s" % ('PVOutput ' + PVOUTPUT_VERSION,
                                                                 REQUIRED_VERSION,
                                                                 weewx.__version__)
            raise weewx.UnsupportedFeature(msg)
        super(PVOutputInstaller, self).__init__(
            version=PVOUTPUT_VERSION,
            name='PVOutput',
            description='WeeWX RESTful service for uploading data to PVOutput.org.',
            author="Gary Roderick",
            author_email="gjroderick@gmail.com",
            restful_services=['user.pvoutput.StdPVOutput'],
            config=pvoutput_dict,
            files=[('bin/user', ['bin/user/pvoutput.py'])]
        )
