import argparse
import sys
from .linter_database import recommend_linter_from_database, recommend_linter_from_database_with_linter
from .lintaid_helper import check_linter, ask_linter, ask_language, recommended_linter, install_linter

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

    if args.version:
        print("LintAid version 1.0.0")
        print("\n\n----------------------------------------------------------")
        sys.exit()

    linter_present = ''
    if check_linter() :
        linter_present = ask_linter()

    language_required = ask_language()

    linter_recommended = []
    if linter_present != '':
        linter_recommended = recommend_linter_from_database_with_linter(language_required, linter_present)
    else:
        linter_recommended = recommend_linter_from_database(language_required)
    

    linter_chosen = recommended_linter(linter_recommended)

    if linter_chosen[0]:
        install_linter()
        print(f'\nLinter {linter_chosen[1]} has been added to your project')
        
    print("\n\n----------------------------------------------------------")


if __name__ == "__main__":
    main()
