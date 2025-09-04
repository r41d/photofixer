
import os
import sys
import hashlib

# pip install rclone-python
from rclone_python import rclone
from rclone_python.hash_types import HashTypes


class Uploader:
    def __init__(self, REMOTE_NAME, REMOTE_DIR):
        if not rclone.check_remote_existing(REMOTE_NAME):
            print(f"rclone remote {REMOTE_NAME} does not exist, exiting...")
            exit(1)
        self.REMOTE = f"{REMOTE_NAME}:{REMOTE_DIR}"
        self.sha1remote = rclone.hash(HashTypes.sha1, self.REMOTE)

    @staticmethod
    def base_ext(file_path):
        folder, file = os.path.split(file_path)
        base, ext = os.path.splitext(file)
        ext = ext.lstrip('.').lower()
        return base, ext

    @staticmethod
    def sha1sum(file_path):
        with open(file_path, 'rb', buffering=0) as f:
            return hashlib.file_digest(f, 'sha1').hexdigest()

    def is_file_hash_present(self, file_path):
        return self.sha1sum(file_path) in self.sha1remote.values()

    def upload(self, src, dst):
        try:
            rclone.copyto(src, os.path.join(self.REMOTE, dst), ignore_existing=True, show_progress=False, args=[])
        except KeyError as ke:
            print(f"KeyError on {src}:", ke)
        except rclone.RcloneException as rce:
            print(f"rclone fail on {src}:", rce)
        else:
            print(f"Upload success {src} → {dst}")
        sys.stdout.flush()
