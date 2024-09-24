**Path Planning Algorithm**
- This project implements a basic Path Planning Algorithm using the A* routing algorithm. The architecture is designed with flexibility in mind, allowing for easy integration of additional algorithms through a plug-and-play approach. The project utilizes strategy and factory design patterns to ensure scalability, maintainability, and a structured solution for pathfinding problems.

**Tools Required**
- Python 3.11+

**Design Architecture**
- The project follows a structured design using the Strategy and Factory design patterns to manage algorithm logic. This architecture allows for future algorithms to be easily introduced and integrated while maintaining consistency across the project.

**Directory Structure**
- src: 
    **algo**
    - The algo directory consists of routing algorithm files/classes
        **routings**
        - This is where the routing algorithms are stored, currently a_star.py is the first simple algorithm that uses the PathRoutingBase Protocol (Strategy Pattern).
        - When other algorithms are introduced, we inherit the PauthRoutingBase Protocol
        
        **files in main directory**
        - Files in algo directory are helpers, utilities files.

    **algo_exceptions**
    - This directory consists of customs exceptions needed for the path routing algorithms

    **algo_types**
    - This directionry consists of custom types, dataclasses, etc.
    - This keeps the code more understandable using types and structural

    **base**
    - This directory consists of base protocol abstract classes that can be inherit to maintain a structural design protocol.

    **tester**
    - This is where the messy fun is done, we create playground code, test files, etc.

**How to Use**
Clone the repository.
Ensure you have Python 3.11+ installed.
Implement additional routing algorithms by inheriting from PathRoutingBase in the base directory.
Use the tester directory to write and execute test cases for the algorithms

For visuals, you will have to run **python3 visuals/main.py** to execute your algorithms in a pygame visuals.
you would need to alter the **visualization_manager.py** to get the specifics of routing.