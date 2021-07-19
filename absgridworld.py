from ienivornment import IEnvironment
from gridworld_constants import UNUSED


class AbsGridworld(IEnvironment):
    """Abstract class used for gridworld problems."""

    def __init__(self, schema: list) -> None:
        """
        Description
        ----------
        Constructor used for processing the schema into the internal gridworld
        representation that all concrete gridworld implementations would use.

        Parameters
        ----------
        schema : list
            The schema used
        """
        super().__init__()

        # We construct a gridworld from the schema
        gridworld = []
        for row in schema:
            gridRow = []
            for item in row:
                tileType = item[0]
                count = item[1]

                for i in range(count):
                    gridRow.append(tileType)

            gridworld.append(gridRow)

        # We define our gridworld representation in this assignment
        self.gridworld = gridworld
        self.rowCount = len(gridworld)
        self.colCount = len(gridworld[0])

    def displayEnvironment(self):
        for row in self.gridworld:
            row_str = ""
            for item in row:
                if item == UNUSED:
                    row_str += ' '
                else:
                    row_str += item
            print(row_str)
