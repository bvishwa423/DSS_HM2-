from setuptools import setup, find_packages

setup(
    name="math_quiz",  # Replace with your project's name
    version="0.1",
    packages=find_packages(),  # This will automatically include all packages and subpackages
    install_requires=[],  # Add any required dependencies, e.g., ['numpy', 'flask']
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:main',  # This assumes you have a 'main' function in math_quiz.py
        ],
    },
    author="Your Name",  # Replace with your name
    author_email="your_email@example.com",  # Replace with your email
    description="A simple math quiz CLI",  # Short description of your project
    long_description=open('README.md').read(),  # Content of your README.md
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/yourrepository",  # Replace with your repo's URL
)
