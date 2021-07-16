#!/usr/bin/bash

VERSION="10.0.0-canary.c5e18b020.0"
# VERSION="latest"
# VERSION="8.0.0"

echo "Removing old files"
mv material-components-web.min.css material-components-web.min.css.old
mv material-components-web.min.js material-components-web.min.js.old
mv material-components-web.min.css material-components-web.css.old
mv material-components-web.min.js material-components-web.js.old
echo "Downloading new files"
wget https://unpkg.com/material-components-web@$VERSION/dist/material-components-web.min.css
wget https://unpkg.com/material-components-web@$VERSION/dist/material-components-web.min.js
wget https://unpkg.com/material-components-web@$VERSION/dist/material-components-web.css
wget https://unpkg.com/material-components-web@$VERSION/dist/material-components-web.js
echo "Done"
