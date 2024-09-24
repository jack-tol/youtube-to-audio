import os

class Utils:
    @staticmethod
    def cleanup_file(file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
