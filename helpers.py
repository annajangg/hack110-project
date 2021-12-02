def find_animal(music: str) -> str:
    if music == 'jazz':
        return 'Morris'
    elif music == 'rap':
        return 'Abu'
    elif music == 'folk':
        return 'Sven'
    else:
        return 'Fire Spirit'

class user:
    id: int
    first_name: str
    last_name: str
    animal: str

    def __init__(self, id: int, fname: str, lname: str, animal: str):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.animal = animal