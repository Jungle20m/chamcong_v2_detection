import os

from starlette.config import Config


config = Config(".env-dev")

# **DATABASE
DATABASE_URL: str = config("DB_CONNECTION")
POOL_RECYCLE = 3600

# **
REGISTRY_API: str = config("REGISTRY_API")

# **
DETECTION_ALIGN = os.path.join(os.getcwd(), "app/services/face_detection/align")
