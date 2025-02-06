Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML``   # Robotic Arm PD Control Simulation  This project simulates the movement of a robotic arm using a PD (Proportional-Derivative) controller. The system aims to reach a target position (in degrees) by adjusting the arm's angle over time. The simulation includes an animation showing the arm's movement and the error over time.  ## Requirements  - Python 3.x  - NumPy  - Matplotlib  You can install the necessary dependencies using `pip`:  ```bash  pip install numpy matplotlib   ``

Overview
--------

The robotic arm's motion is controlled by a PD controller, which adjusts the torque applied to the arm based on the error (difference between the target and current position) and the derivative of the error (rate of change of the error). The system's dynamics are simulated in discrete time steps.

### Key Components:

1.  **PD Controller**:
    
    *   kp: Proportional gain
        
    *   kd: Derivative gain
        
    *   The controller adjusts the torque (tau) to reduce the error between the target and the arm's current position.
        
2.  **Simulation Parameters**:
    
    *   time\_step: Time step for each simulation iteration.
        
    *   sim\_time: Total simulation duration.
        
    *   The arm's initial position, velocity, and target position are defined.
        
    *   The system's inertia is considered when calculating angular acceleration.
        
3.  **Robotic Arm Model**:
    
    *   The arm length (arm\_length) is defined, which determines the arm's size.
        
    *   The arm's movement is calculated using the angle (theta) and angular velocity (theta\_dot).
        
4.  **Animation**:
    
    *   The movement of the arm is visualized using Matplotlib.
        
    *   The path taken by the arm and the target position are displayed in the animation.
        
    *   A second plot visualizes the error between the target and actual position over time.
        

How to Use
----------

1.  Clone this repository or download the code.
    
2.  Run the script in a Python environment.
    
3.  The first animation shows the movement of the robotic arm, while the second plot visualizes the error over time.
    

Code Explanation
----------------

*   **Initialization**: Variables such as arm length, initial position, velocity, and target position are set.
    
*   **Simulation Loop**: The arm's position and velocity are updated at each time step based on the PD control law.
    
*   **PD Control**: The PD controller calculates the required torque to minimize the error between the arm's current position and the target.
    
*   **Animation**: The robotic arm's movement and the path it follows are displayed using FuncAnimation from Matplotlib.
    
*   **Error Plot**: A plot of the error over time is generated after the simulation, showing how the error decreases as the arm approaches the target position.
    

Example Output
--------------

The simulation produces:

1.  An animation showing the robotic arm's movement from the start to the target position.
    
2.  A plot of the error over time, showing how the error decreases as the arm approaches the target position.
    

Customization
-------------

You can adjust the following parameters to modify the simulation:

*   **PD gains**: Change kp and kd to experiment with the control performance. Increasing kp makes the controller more responsive, while increasing kd reduces oscillations by adding damping.
    
*   **Simulation duration**: Modify sim\_time to extend or shorten the simulation.
    
*   **Arm length**: Adjust the arm\_length to scale the arm's size. Larger arms will move slower due to increased inertia.
    

License
-------

This project is open-source and available under the MIT License.
