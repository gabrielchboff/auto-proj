import subprocess
from dataclasses import dataclass

from utils.decorators import thrower


@dataclass
class RepoMaker:
    url: str
    path: str

    @staticmethod
    def __alert():
        print("[!] Please provide a valid URL")

    @thrower
    def __build_version(self):
        result = subprocess.run(
            f"{self.path} git init", shell=True, capture_output=True, text=True
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            # Handle any errors or exceptions
            return f"Error: {result.stderr.strip()}"

    @thrower
    def __make_remote(self):
        result = subprocess.run(
            f"{self.path} git remote add origin {self.url}",
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            # Handle any errors or exceptions
            return f"Error: {result.stderr.strip()}"

    @thrower
    def __add_origin(self):
        start_info = subprocess.run(
            "touch checkpoint.txt", shell=True, capture_output=True, text=True
        )
        result = subprocess.run(
            f"{self.path} git add .",
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0 and start_info.returncode == 0:
            return result.stdout.strip()
        else:
            # Handle any errors or exceptions
            return f"Error: {result.stderr.strip()}"

    @thrower
    def __add_commit(self):
        result = subprocess.run(
            f"{self.path} git commit -m 'Initial commit'",
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            # Handle any errors or exceptions
            return f"Error: {result.stderr.strip()}"

    @thrower
    def __push(self):
        result = subprocess.run(
            f"{self.path} git push -u origin master",
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            # Handle any errors or exceptions
            return f"Error: {result.stderr.strip()}"

    def create_version_control(self):
        self.__alert()
        version = self.__build_version()
        remote = self.__make_remote()
        origin = self.__add_origin()
        commit = self.__add_commit()
        push = self.__push()
        print(
            f"""
        version: {version}, 
        remote: {remote}, 
        origin: {origin}, 
        commit: {commit}, 
        push: {push}"""
        )
