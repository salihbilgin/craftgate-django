import os
import uuid


class Guid:
    @staticmethod
    def generate():
        if hasattr(os, "urandom"):
            return str(uuid.UUID(bytes=os.urandom(16)))
        else:
            return str(uuid.uuid4())
