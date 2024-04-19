JavaScriptLinters = ['ESLint' , 'JSHint', 'Prettier', 'Clinton']
JavaLinter = ['PMD', 'Checkstyle']
GoLinter = ['GoLint', 'GoMetaLinter']
PythonLinter = ['Black', 'Flake8', 'PyLint', 'PyCodeStyle']

ESLint = {  'Python': 
                PythonLinter,
            'Java':
                JavaLinter,
            'Go':
                GoLinter
        }
JSHint = {  'Python': 
                PythonLinter,
            'Java':
                JavaLinter,
            'Go':
                GoLinter
        }
Prettier= { 'Python': 
                PythonLinter,
            'Java':
                JavaLinter,
            'Go':
                GoLinter
        }
Clinton= {  'Python': 
                PythonLinter,
            'Java':
                JavaLinter,
            'Go':
                GoLinter
        }
PMD = {  'Python': 
                PythonLinter,
            'JavaScript':
                JavaScriptLinters,
            'Go':
                GoLinter
        }
Checkstyle= {   'Python': 
                    PythonLinter,
                'JavaScript':
                    JavaScriptLinters,
                'Go':
                    GoLinter
        }
GoLint= {  'Python': 
                PythonLinter,
            'Java':
                JavaLinter,
            'JavaScript':
                JavaScriptLinters
        }
GoMetaLint= {  'Python': 
                PythonLinter,
            'Java':
                JavaLinter,
            'JavaScript':
                JavaScriptLinters
        }
Black = {   'JavaScript': 
                JavaScriptLinters,
            'Java':
                JavaLinter,
            'Go':
                GoLinter
        }
Flake8= {   'JavaScript': 
                JavaScriptLinters,
            'Java':
                JavaLinter,
            'Go':
                GoLinter
        }
PyLint= {   'JavaScript': 
                JavaScriptLinters,
            'Java':
                JavaLinter,
            'Go':
                GoLinter
        }
PyCodeStyle={   'JavaScript': 
                JavaScriptLinters,
            'Java':
                JavaLinter,
            'Go':
                GoLinter
        }


def recommend_linter_from_database_with_linter(language, linter):
    recommended_linter = []

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
    
    return recommended_linter

def recommend_linter_from_database(language):
    recommended_linter = []

    if language == 'JavaScript':
        recommended_linter = JavaScriptLinters
    if language == 'Java':
        recommended_linter = JavaLinter
    if language == 'Go':
        recommended_linter = GoLinter
    if language == 'Python':
        recommended_linter = PythonLinter
    
    return recommended_linter