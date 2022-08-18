# PVOutput uploader extension #

A [WeeWX](http://weewx.com/ "WeeWX - Open source software for your weather station") RESTful service to upload solar PV power generation data to [PVOutput](http://pvoutput.org/ "PVOutput.org").


## Description ##

The *PVOutput uploader* extension allows uploading of solar PV power generation data to PVOutput using the [PVOutput API](https://pvoutput.org/help.html#overview).

The *PVOutput uploader* extension consists of:
- a RESTful service for posting data to PVOutput, and
- a utility for bulk uploading of solar PV generation data to PVOutput should Internet access be lost for some period of time.

## Pre-Requisites ##

The *PVOutput uploader* extension requires:

- WeeWX v3.7.0 or greater
- a PVOutput account with system ID and API access key
- a WeeWX system using a WeeWX archive to record solar PV power generation data using the [Aurora driver](https://github.com/gjr80/weewx-pvoutput/tree/master/driver) custom schema

## Installation ##

The *PVOutput uploader* extension can be installed manually or automatically using the [*wee_extension* utility](http://weewx.com/docs/utilities.htm#wee_extension_utility). The preferred method of installation is through the use of *wee_extension*.

**Note:** Symbolic names are used below to refer to some file location on the WeeWX system. These symbolic names allow a common name to be used to refer to a directory that may be different from system to system. The following symbolic names are used below:

-   *$DOWNLOAD_ROOT*. The path to the directory containing the downloaded *PVOutput uploader* extension.
-   *$BIN_ROOT*. The path to the directory where WeeWX executables are located. This directory varies depending on WeeWX installation method. Refer to [where to find things](http://weewx.com/docs/usersguide.htm#Where_to_find_things "where to find things") in the [WeeWX User's Guide](http://weewx.com/docs/usersguide.htm "User's Guide to the WeeWX Weather System") for further information.

### Installation using the wee_extension utility ###

1.  Download the latest *PVOutput uploader* extension from the *PVOutput uploader* extension [releases page](https://github.com/gjr80/weewx-pvoutput/releases) into a directory accessible from the WeeWX machine.

        $ wget -P $DOWNLOAD_ROOT https://github.com/gjr80/weewx-pvoutput/releases/download/v0.4.1/pvoutput-0.4.1.tar.gz

    where *$DOWNLOAD_ROOT* is the path to the directory where the *PVOutput uploader* extension is to be downloaded.

1.  Stop WeeWX:

        $ sudo /etc/init.d/weewx stop

    or

        $ sudo service weewx stop

1.  Install the *PVOutput uploader* extension downloaded at step 1 using the *wee_extension* utility:

        $ wee_extension --install=$DOWNLOAD_ROOT/pvoutput-0.4.1.tar.gz

    This will result in output similar to the following:

        Request to install '/var/tmp/pvoutput-0.4.1.tar.gz'
        Extracting from tar archive /var/tmp/pvoutput-0.4.1.tar.gz
        Saving installer file to /home/weewx/bin/user/installer/Aurora
        Saved configuration dictionary. Backup copy at /home/weewx/weewx.conf.20180201124410
        Finished installing extension '/var/tmp/pvoutput-0.4.1.tar.gz'

1.  Edit *weewx.conf*:

        $ vi weewx.conf

1.  In *weewx.conf* under *[StdRESTful]* *[[PVOutput]]* check to ensure the *enable* configuration option is set to *True* and the *system_id* and *api_key* configuration options are set for the PVOutput system and API key to be used:

        [[PVOutput]]
            # This section is for configuring posts to PVOutput.

            # If you wish to do this, set the option 'enable' to true,
            # and specify a station and password.
            enable = true
            system_id = ENTER_PVOUTPUT_SYSTEM_ID_HERE
            api_key = ENTER_PVOUTPUT_API_KEY_HERE

    **Note:** The *enable* configuration option is set to *False* by default during the *PVOutput uploader* extension installation.

1.  Save *weewx.conf*.

1.  Start WeeWX:

        $ sudo /etc/init.d/weewx start

    or

        $ sudo service weewx start

1.  The WeeWX log should be monitored to verify data is being posted to PVOutput at the end of each archive period. Setting *debug = 1* or *debug = 2* in *weewx.conf* will provide additional information in the log. Using *debug = 2* will generate significant amounts of log output and should only be used for verification of operation or testing.

### Manual installation ###

1.  Download the latest *PVOutput uploader* extension from the *PVOutput uploader* extension [releases page](https://github.com/gjr80/weewx-pvoutput/releases) into a directory accessible from the WeeWX machine.

        $ wget -P $DOWNLOAD_ROOT https://github.com/gjr80/weewx-pvoutput/releases/download/v0.4.1/pvoutput-0.4.1.tar.gz

    where *$DOWNLOAD_ROOT* is the path to the directory where the *PVOutput uploader* extension is to be downloaded.

1.  Stop WeeWX:

        $ sudo /etc/init.d/weewx stop

    or

        $ sudo service weewx stop

1.  Unpack the extension as follows:

        $ tar xvfz pvoutput-0.4.1.tar.gz

1.  Copy files from within the resulting directory as follows:

        $ cp pvoutput/bin/user/*.py $BIN_ROOT/user

	  replacing the symbolic name *$BIN_ROOT* with the nominal locations for your installation.

1.  Edit *weewx.conf*:

        $ vi weewx.conf

1.  In *weewx.conf* under *[StdRESTful]* add a *[[PVOutput]]* stanza as follows ensuring the *system_id* and *api_key* configuration options are set for the PVOutput system and API key to be used:

        [[PVOutput]]
            # This section is for configuring posts to PVOutput.

            # If you wish to do this, set the option 'enable' to true,
            # and specify a station and password.
            enable = true
            system_id = ENTER_PVOUTPUT_SYSTEM_ID_HERE
            api_key = ENTER_PVOUTPUT_API_KEY_HERE

1.  In *weewx.conf* under *[Services]* add *user.pvoutput.StdPVOutput* to the list of *restful_services*:

        [Services]
            ....
            restful_services = user.pvoutput.StdPVOutput
            ....

1.  Save *weewx.conf*.

1.  Start WeeWX:

        $ sudo /etc/init.d/weewx start

    or

        $ sudo service weewx start

1.  The WeeWX log should be monitored to verify data is being posted to PVOutput at the end of each archive period. Setting *debug = 1* or *debug = 2* in *weewx.conf* will provide additional information in the log. Using *debug = 2* will generate significant amounts of log output and should only be used for verification of operation or testing.

## Support ##

General support issues may be raised in the Google Groups [weewx-user forum](https://groups.google.com/group/weewx-user). Specific bugs in the *PVOutput uploader*r extension code should be the subject of a new issue raised via the [*PVOutput uploader* extension issues page](https://github.com/gjr80/weewx-pvoutput/issues).

## Licensing ##

The *PVOutput uploader* extension is licensed under the [GNU Public License v3](https://github.com/gjr80/weewx-pvoutput/blob/master/LICENSE).

