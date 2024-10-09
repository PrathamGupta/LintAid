import argparse
import sys
from .linter_database import recommend_linter_from_database, recommend_linter_from_database_with_linter
from .lintaid_helper import check_linter, ask_linter, ask_language, recommended_linter
from .add_linter import  install_linter

BANNER = """

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

$$\       $$\            $$\      $$$$$$\  $$\       $$\ 
$$ |      \__|           $$ |    $$  __$$\ \__|      $$ |
$$ |      $$\ $$$$$$$\ $$$$$$\   $$ /  $$ |$$\  $$$$$$$ |
$$ |      $$ |$$  __$$\\\_$$  _|  $$$$$$$$ |$$ |$$  __$$ |
$$ |      $$ |$$ |  $$ | $$ |    $$  __$$ |$$ |$$ /  $$ |
$$ |      $$ |$$ |  $$ | $$ |$$\ $$ |  $$ |$$ |$$ |  $$ |
$$$$$$$$\ $$ |$$ |  $$ | \$$$$  |$$ |  $$ |$$ |\$$$$$$$ |
\________|\__|\__|  \__|  \____/ \__|  \__|\__| \_______|

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                          
                                                         
                    
LintAid: Seamless linter integration for your projects.


----------------------------------------------------------

"""


def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="LintAid: Seamless linter integration for your projects.")
    parser.add_argument("--version", action="store_true", help="Show the version of LintAid")
    args = parser.parse_args()

    # This argument tells the version of LintAid present
    if args.version:
        print("LintAid version 1.0.0")
        print("\n\n----------------------------------------------------------")
        sys.exit()

    #This is where the main function starts
    linter_present = ''

    #First we check if there is a linter present in the repository or not
    if check_linter() :

        #If linter is present then ask what linter it is
        linter_present = ask_linter()

    #Ask what language they want to add a linter for
    language_required = ask_language()

    linter_recommended = []

    #We get linter recommendation from the system based on linter present or not
    if linter_present != '':
        linter_recommended = recommend_linter_from_database_with_linter(language_required, linter_present)
    else:
        linter_recommended = recommend_linter_from_database(language_required)
    
    #Ask the user for their preference on the recommended linters
    linter_chosen = recommended_linter(linter_recommended)

    #Install the Linter
    if linter_chosen[0]:

        print(f'\nLinter {linter_chosen[1]} has been added to your project')
        install_linter(linter_chosen[1])
        
    print("\n\n----------------------------------------------------------")


if __name__ == "__main__":
    main()
