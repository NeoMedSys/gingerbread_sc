import nox
import os

@nox.session()
def tests(session):
    session.run('poetry', 'install')
    session.run('poetry', 'add', 'coverage')
    session.run('poetry', 'run', 'pytest', './tests_rest', '--junitxml=./junit.xml')
    # coverage
    session.run('poetry', 'run', 'coverage', 'run', '--source=.', '--data-file', './.coverage', '-m', 'pytest', './tests')
    session.run('poetry', 'run', 'coverage', 'xml')
    
@nox.session()
def lint(session):
    session.install('flake8')
    session.run('flake8', '.' ,'--exit-zero', '--format=html', '--statistics', '--tee', '--output-file', 'flake8.txt')