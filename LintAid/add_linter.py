import os
from .lintaid_helper import ask_repository

def install_linter(linter):

    repository_name = ask_repository()

    if linter == 'ESLint':
        recommended_linter = ESLint[language]
    if linter == 'JHSLint':
        recommended_linter = JSHint[language]
    if linter == 'Prettier':
        recommended_linter = Prettier[language]
    if linter == 'Clinton':
        recommended_linter = Clinton[language]
    if linter == 'PMD':
        recommended_linter = PMD[language]
    if linter == 'Checkstyle':
        recommended_linter = Checkstyle[language]
    if linter == 'GoLint':
        recommended_linter = GoLint[language]
    if linter == 'GoMetaLinter':
        recommended_linter = GoMetaLint[language]
    if linter == 'Black':
        recommended_linter = Black[language]
    if linter == 'Flake8':
        recommended_linter = Flake8[language]
    if linter == 'PyLint':
        recommended_linter = PyLint[language]
    if linter == 'PyCodeStyle':
        recommended_linter = PyCodeStyle[language]

    return 

