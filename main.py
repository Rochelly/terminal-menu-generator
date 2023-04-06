from menu import Menu
import logging


def main():
    """
    The main function of the program.

    This function sets up the logging system by configuring the log file and log level.
    It defines three functions that perform some tasks and optionally log their results.
    It then creates a menu with these functions and displays it to the user.

    Args:
        None

    Returns:
        None
    """
    # Configure the logging system
    logging.basicConfig(filename='log_file.log', level=logging.DEBUG)

    # Define the functions
    def my_function_01():
        logging.debug('Starting my_function')
        # Do some work here...
        logging.info('Finished my_function')

    def my_function_02():
        # does something and then logs it (or not)
        pass

    def my_function_03():
        # does something and then logs it (or not)
        pass

    # Define the menu options
    menu_options = {
        "Option 1": my_function_01,
        "Option 2": my_function_02,
        "Option 3": my_function_03,
        "Exit": ""
    }

    # Define the header message and log file
    header_msg = ["Welcome to the menu!", "Select an option below:", "Use the up arrow ↑ and down arrow ↓ keys to select an option:",
                  "Press ENTER to select an option:"]
    log_file = "log_file.log"

    # Create the menu and show it to the user
    menu = Menu(menu_options, header_msg, log_file)
    menu.show()


if __name__ == '__main__':
    main()
