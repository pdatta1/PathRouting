**Path Planning Algorithm**
This project implements a basic Path Planning Algorithm using the A* routing algorithm. The architecture is designed with flexibility in mind, allowing for easy integration of additional algorithms through a plug-and-play approach. The project utilizes strategy and factory design patterns to ensure scalability, maintainability, and a structured solution for pathfinding problems.

**Tools Required**
Python 3.11+
Design Architecture
The project follows a structured design using the Strategy and Factory design patterns to manage algorithm logic. This architecture allows for future algorithms to be easily introduced and integrated while maintaining consistency across the project.

**Directory Structure**
src/
    └── algo/
        ├── routings/
        │   └── a_star.py  # The first routing algorithm implemented using the PathRoutingBase Protocol (Strategy Pattern)
        ├── __init__.py    # Initialization of algo package
        └── utils.py       # Helper and utility files supporting the algorithms
    └── algo_exceptions/
        └── custom_exceptions.py  # Custom exceptions needed for path routing algorithms
    └── algo_types/
        └── types.py  # Custom types, dataclasses, and structures for enhanced code readability and maintainability
    └── base/
        └── protocols.py  # Base abstract classes (Protocols) for maintaining structured design patterns
    └── tester/
        └── test_cases.py  # Playground for experimenting and testing routing algorithms

**How to Use**
Clone the repository.
Ensure you have Python 3.11+ installed.
Implement additional routing algorithms by inheriting from PathRoutingBase in the base directory.
Use the tester directory to write and execute test cases for the algorithms