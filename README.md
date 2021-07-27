# JenkinsBuildScript
* Bash shell script was written on 5/22/2018
* Porting into Python since 6/23/2021


# TODOs
- [ ] Configuration for platform each, i.e. ios or android
- [ ] Configuration must have distribution path for web site
- [ ] iOS must assign ``workspace``, ``scheme``, and ``DSTROOT``
- [ ] iOS must have ``ExportOptions.plist``
- [ ] Configuration must have output file name, maybe remote server via sftp
- [ ] Find out output files size for xxx.ipa or xxx.apk
- [ ] Can send result via slack (webhook but need authentication), and teams (webhook) as JSON format
- [ ] Can get ``git`` last log in ``workspace`` as --pretty-format
- [ ] Output file must be formatted like [gapp3_3.3.0(527)_210723.json](https://raw.githubusercontent.com/neoroman/JenkinsBuildScript/main/python/gapp3_3.3.0(527)_210723.json)
- [ ] Android must find out application version from ``workspace/app/version.properties``
- [ ] iOS must find out application version from ``Info.plist`` with ``/usr/libexec/PlistBuddy``
- [ ] Can use ``apksigner`` for Android application signing
- [ ] Can send email to specific receipients in ``oz_cd.cfg``
