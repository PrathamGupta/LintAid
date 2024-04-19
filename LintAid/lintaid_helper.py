import inquirer

def check_linter():
    '''
    
    '''
    
    check_linter = inquirer.prompt([
        inquirer.Confirm('Linter', message="Do you have a Linter present in your reporsitory?", default=True),
    ])
    return check_linter['Linter']

def ask_linter():
    '''
    
    '''

    ask_linter = inquirer.prompt([
        inquirer.List('Name',
            message="What Linter is present?",
            choices=['ESLint', 'JSHint', 'Prettier', 'Clinton', 'GoLint', 'GoMetaLinter', 'PMD', 'Checkstyle', 'Black', 'Flake8', 'PyLint', 'PyCodeStyle'],
        ),
    ])
    return ask_linter['Name']

def ask_language():
    '''
    
    '''

    ask_language = inquirer.prompt([
        inquirer.List('Name',
            message="What language linter do you want?",
            choices=['JavaScript', 'Java', 'Go', 'Python'],
        ),
    ])
    return ask_language['Name']

def recommended_linter(linter_recommended):
    '''
    
    '''

    linter_chosen = [False, '']
    for i in range(len(linter_recommended)):
        print(f'You have been recommended the linter: {linter_recommended[i]}\n')
        confirmed_linter = inquirer.prompt([
            inquirer.Confirm('Confirmed Linter', message=f"Do you want to add {linter_recommended[i]} to your project?", default=True),
        ])
        if confirmed_linter['Confirmed Linter'] : 
            linter_chosen[0] = True
            linter_chosen[1] = linter_recommended[i]
            break
    return linter_chosen

def install_linter():
    return 