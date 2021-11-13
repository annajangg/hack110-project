def assign_name(name: str) -> str:
    return name

class user:
    id: int
    my_assignment: str

    def __init__(self, id: int, assignment: str, name: str):
        self.id = id
        self.my_assignment = assignment