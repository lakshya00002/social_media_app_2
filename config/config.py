from flask import Flask
from shared.utils.db_utils import db
from shared.utils.db_utils import migrate

# Initialize the Flask App
app = Flask(__name__)

# Initialization configuration
# (later move this configuration to config/config.py)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%40Rbodhasu10@localhost/social_media_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)
app.config["DEBUG"] = True


from shared.models import user_model
from shared.models import post_model
from shared.models import comment_model
from shared.models import messages_model
from shared.models import like_model
from shared.models import notification_model