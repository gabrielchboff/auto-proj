from dataclasses import dataclass

from app.utils.databases import DBInstance
from app.utils.repositories import RepoMaker


@dataclass
class Setup:
    repo: RepoMaker
    language: str
    project_name: str
    project_description: str
    project_type: str
    db: DBInstance
