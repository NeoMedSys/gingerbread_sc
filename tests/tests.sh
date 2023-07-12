pip install nox
pip install genbadge[tests]
pip install genbadge[coverage]
pip install genbadge[flake8]
nox
genbadge tests -t 99 -i - < junit.xml
genbadge coverage -i - < coverage.xml
genbadge flake8 -i - < flake8.txt
rm junit.xml coverage.xml flake8.txt