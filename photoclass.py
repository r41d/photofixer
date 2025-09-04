import os
import os.path
import datetime
from dataclasses import dataclass

import photofixerconfig


@dataclass
class Photo:
    """Class for keeping track of properties of a photo."""
    directory: str
    filename: str

    model: str = ""
    make: str = ""
    dt: datetime.datetime = 0

    newname: str = ""

    @property
    def base(self) -> str:
        return os.path.splitext(self.filename)[0]

    @property
    def ext(self) -> str:
        return os.path.splitext(self.filename)[1].lstrip('.').lower()

    @property
    def filepath(self) -> str:
        return os.path.join(self.directory, self.filename)

    def sanitize_model(self):
        # Trim make from model
        if photofixerconfig.TRIM_MAKE_FROM_MODEL:
            self.model = self.model.replace(self.make, "").strip()

        # Rename model according to config
        for k, v in photofixerconfig.MODEL_RENAMINGS.items():
            if k in self.model:
                self.model = self.model.replace(k, v)
                continue  # only apply 1 renamimg rule at maximum

        # Don't risk unnecessary subfolders because of potential slashes in camera model under any circumstances
        self.model = self.model.replace('/', '_')
