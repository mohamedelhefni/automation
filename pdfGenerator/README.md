# Pdf Generator
a python scripts that  download video lectures from drive folder , it uses ffmpeg to extract a frame each 60 seconds and after extracting frames it uses conver all png frames to one pdf file

### Requirments

```
sudo apt-get install ffmpeg
sudo apt-get install imagemagick
```

```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

Authorization credentials for a desktop application. To learn how to create credentials for a desktop application, refer to Create [credentials](https://developers.google.com/workspace/guides/create-credentials).

to fix convert security issue
```
 sudo vim /etc/ImageMagick-6/policy.xml
```
and remove
```
<!-- disable ghostscript format types -->
<policy domain="coder" rights="none" pattern="PS" />
<policy domain="coder" rights="none" pattern="PS2" />
<policy domain="coder" rights="none" pattern="PS3" />
<policy domain="coder" rights="none" pattern="EPS" />
<policy domain="coder" rights="none" pattern="PDF" />
<policy domain="coder" rights="none" pattern="XPS" />
```
