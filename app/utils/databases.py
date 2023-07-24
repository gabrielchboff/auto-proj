from dataclasses import dataclass

from config import DATABASE_IMAGES


@dataclass
class DBInstance:
    name: str
    host: str
    port: int
    user: str
    password: str
    image: str

    def to_instance(self):
        db_file = f"""
          {self.image}:
            image: {DATABASE_IMAGES[self.image]}
            container_name: {self.image}_db
            ports:
              - "{self.port}:{self.port}"
            environment:
              POSTGRES_DB: {self.name}
              POSTGRES_USER: {self.user}
              POSTGRES_PASSWORD: {self.password}
              POSTGRES_HOST: {self.host}
              POSTGRES_PORT: {self.port}
        """
        return db_file
