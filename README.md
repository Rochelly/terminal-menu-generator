# Terminal Menu Generator

This project is a simple menu-based command line tool that allows users to perform different actions by selecting options from a menu. The tool is designed to be extensible and customizable by allowing users to define their own menu options and actions.

## Installation
Clone the project repository to your local machine.
Navigate to the project directory.
Install the required dependencies by running the command pip install -r requirements.txt.
## Usage
To run the menu tool, navigate to the project directory and run the command python main.py. This will display the menu options to the user, allowing them to select an option by using the up and down arrow keys and pressing ENTER.

Each menu option is associated with a function that performs a specific action. These functions can be customized by the user to perform any desired action. By default, the tool comes with three sample functions that perform some basic tasks.

The results of the functions can be optionally logged to a file by configuring the logging system. By default, the tool logs DEBUG level messages to a file named log_file.log in the project directory.

## Customization
The tool can be customized by defining new menu options and functions. To define a new menu option, add a new key-value pair to the menu_options dictionary in the main.py file, where the key is the option name and the value is the function that should be executed when the option is selected.

To define a new function, add a new function definition to the main.py file, and then add the function to the menu_options dictionary with a unique key.

To customize the logging system, modify the logging configuration in the main.py file. This can be done by adjusting the log level, changing the log file name, or modifying the log message format.



![image](https://user-images.githubusercontent.com/11949740/230423234-284e778e-dadb-4502-8fb9-84bee87ba7f9.png)
