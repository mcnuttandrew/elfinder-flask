from flask_sqlalchemy import SQLAlchemy
import time

NUM_ATTEMPTS = 15

for i in range(NUM_ATTEMPTS):
    try:
        db = SQLAlchemy()
    except:
        time.sleep(5)        

db = SQLAlchemy()

class User(db.Model):

    id = db.Column(db.String(256), unique=True, primary_key=True)

    # OAuth2 token items
    access_token = db.Column(db.String(256))
    refresh_token = db.Column(db.String(256))
    # Maybe expiration time?

class File(db.Model):

    rand_id = db.Column(db.String(256), primary_key=True)
    user_id = db.Column(db.String(256), db.ForeignKey(
        User.id), primary_key=True)    

    id = db.Column(db.String(256), primary_key=True) # ID from API
    name = db.Column(db.UnicodeText)
    path = db.Column(db.UnicodeText)
    path_hash = db.Column(db.UnicodeText)
    parent_id = db.Column(db.String())
    parent_hash = db.Column(db.String())

    file_type = db.Column(db.String(256))
    file_extension = db.Column(db.String(256))
    
    size = db.Column(db.BigInteger, default=0)
    last_modified = db.Column(db.String(256)) # Might want to modify to the Unix time
    mime_type = db.Column(db.String(128)) # Drive mimeType, not elFinder

    is_shared = db.Column(db.Boolean, default=False)
    is_gdoc = db.Column(db.Boolean, default=False)
    access_type = db.Column(db.String(256)) # owner, editor, etc.

    media_info = db.Column(db.String(1024)) # For images / video on Drive

    error=db.Column(db.Boolean, default=False)

class Folder(db.Model):

    rand_id = db.Column(db.String(256), primary_key=True)
    user_id = db.Column(db.String(256), db.ForeignKey(
        User.id), primary_key=True)    

    id = db.Column(db.String(256), primary_key=True) # ID from API
    name = db.Column(db.UnicodeText)
    path = db.Column(db.UnicodeText)
    path_hash = db.Column(db.UnicodeText)
    parent_id = db.Column(db.String())
    parent_hash = db.Column(db.String())
    
    mime_type = db.Column(db.String(128)) # Drive mimeType, not elFinder

    is_shared = db.Column(db.Boolean, default=False)

    error=db.Column(db.Boolean, default=False)

    
    

    
    
