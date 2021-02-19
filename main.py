from tenue.command_line import *
import os.path
from tenue.init_db import main as create_database

# by healeyj

# TODO: reformat 'design specs' section of the readme


def main():
    if not os.path.exists(db_name):
        create_database()
    db.connect()
    print("Connected to " + db_name)
    Shell().cmdloop()
    db.close()


main()
