import json
from menu import Menu
import logging


def main():

    logging.basicConfig(filename='log_file.log', level=logging.DEBUG)

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

    menu_options = {
        "Option 1": my_function_01,
        "Option 2": my_function_02,
        "Option 2": my_function_03,
        "Exit": ""
    }
    header_msg = ["Welcome to the menu!", "Select an option below:", "Use the up arrow ↑ and down arrow ↓ keys to select an option:",
                  "Press ENTER to select an option:"]
    log_file = "log_file.log"
    menu = Menu(menu_options, header_msg, log_file)
    menu.show()


if __name__ == '__main__':
    main()
