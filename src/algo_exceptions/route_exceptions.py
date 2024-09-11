class PathNotFoundException(Exception):
    """
    PathNotFoundException is a custom exception that is raised when a path cannot 
    be found between two nodes in a pathfinding algorithm.
    """

    def __init__(self, message: str) -> None:
        """
        Initializes the PathNotFoundException with a descriptive error message.

        Args:
            message (str): A message explaining why the path could not be found.
        """
        self.message = message
        super().__init__(self.message)
