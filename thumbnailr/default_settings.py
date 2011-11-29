'''default settings for app.'''

import os

DEBUG = True

#where in filesystem images are stored.
IMG_DIR = os.path.abspath('./imgs')

#original image will be  <img path>/original.<ext>
PREFIX_ORIGINAL = 'original'

#used in file upload form <input type="file" name="{{ PARAM_FILE }}">
PARAM_FILE='file'

#database url
DATABASE = os.path.abspath('./thumbnailr.db')

#path to schema.sql to load for initial database setup.
DATABASE_SCHEMA = os.path.abspath('./schema.sql')
