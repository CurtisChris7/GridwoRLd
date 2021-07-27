from absgridworld import AbsGridworld


class MazeGridWorld(AbsGridworld):

    def __init__(self, schema: list, actions: list) -> None:
        super().__init__(schema, actions)
