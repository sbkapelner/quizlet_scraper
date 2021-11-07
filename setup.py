from setuptools import setup
from setuptools import find_packages

with open('requirements.txt', 'r' ) as requirements:
    reqs = [line.strip('\n') for line in requirements]

setup(name='Quizlet Scraper CLI',
      version='1.0.0',
      description='Quizlet Scraper',
      author='Sarah Kapelner',
      author_email='sbkapelner@gmail.com',
      packages=find_packages(),
      install_requires=reqs,
      entry_points={
          'console_scripts': ['quizlet-scraper = quizlet_scraper.quizlet_scraper:main']
      }
     )