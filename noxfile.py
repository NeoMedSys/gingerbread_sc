import nox


@nox.session()
def clean(session):
    session.run(
        'rm',
        '-rf',
        'badges/*.svg reports/junit/*.xml reports/flake8/*.txt reports/coverage/.coverage reports/coverage/coverage.xml reports/coverage/htmlcov/',
        external=True,
    )


@nox.session()
def tests(session):
    session.run(
        'mkdir',
        './badges',
        external=True,
    )
    session.run(
        'mkdir',
        './reports',
        external=True,
    )
    session.run(
        'mkdir',
        './reports/junit',
        external=True,
    )
    session.run(
        'mkdir',
        './reports/flake8',
        external=True,
    )
    session.run(
        'mkdir',
        './reports/coverage',
        external=True,
    )
    session.run(
        'poetry',
        'install',
        '--with',
        'dev',
        external=True,
    )
    session.run(
        'poetry',
        'run',
        'pytest',
        './tests',
        '--junitxml=./reports/junit/junit.xml',
        external=True,
    )
    # coverage
    session.run(
        'poetry',
        'run',
        'coverage',
        'run',
        '--source=.',
        '--data-file',
        './.coverage',
        '-m',
        'pytest',
        './tests',
        external=True,
    )
    session.run(
        'poetry',
        'run',
        'coverage',
        'report',
        external=True,
    )
    session.run(
        'poetry',
        'run',
        'coverage',
        'xml',
        external=True,
    )
    session.run(
        'poetry',
        'run',
        'coverage',
        'html',
        external=True,
    )
    session.run(
        'mv',
        '.coverage',
        './reports/coverage',
        external=True,
    )
    session.run(
        'mv',
        'coverage.xml',
        './reports/coverage',
        external=True,
    )
    session.run(
        'cp',
        '-R',
        'htmlcov/',
        './reports/coverage',
        external=True,
    )
    session.run(
        'rm',
        '-R',
        'htmlcov/',
        external=True,
    )


@nox.session()
def lint(session):
    session.install('flake8')
    session.run(
        'flake8',
        '.',
        '--max-line-length=180',
        '--exit-zero',
        '--format=%(path)s::%(row)d,%(col)d::%(code)s::%(text)s',
        '--statistics',
        '--tee',
        '--output-file',
        './reports/flake8/flake8.txt',
    )


@nox.session()
def gen_badge(session):
    session.install('genbadge[tests,coverage,flake8]')

    session.run(
        'genbadge',
        'tests',
        '-i',
        './reports/junit/junit.xml',
        '-o',
        './badges/rt-tests-badge.svg',
    )
    session.run(
        'genbadge',
        'coverage',
        '-i',
        './reports/coverage/coverage.xml',
        '-o',
        './badges/rt-coverage-badge.svg',
    )
    session.run(
        'genbadge',
        'flake8',
        '-i',
        './reports/flake8/flake8.txt',
        '-o',
        './badges/rt-flake8-badge.svg',
    )