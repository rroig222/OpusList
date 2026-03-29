from dataclasses import dataclass



@dataclass
class User():

    id: int
    username: str
    email: str

@dataclass
class Composer():

    id: str
    name: str
    full_name: str
    epoch: str

@dataclass
class Work():

    id: int
    title: int
    composer_id: int
    openopus_id: int
    genre: int
    composer: Composer