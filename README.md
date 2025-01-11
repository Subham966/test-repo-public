



# **Git Workflow and Pre-Commit Hooks Setup**

This document outlines the steps to initialize a Git repository, set up pre-commit hooks for linting, and enforce best practices like checking for secrets in commits and running linters for various file types.

## **Git Workflow**

### **Initialize Git Repository**

```bash
git init
git add .
git commit -m "Your commit message"
git remote add origin https://github.com/Subham966/call-booking-application-3-tier-eks.git
git remote set-url origin https://github.com/Subham966/call-booking-application-3-tier-eks.git
git remote -v
git branch -M main
git push -u origin main
```

```bash
git fetch
git pull origin --rebase
```


#**Token with push file:**
```bash

Create a Token:- Developer -> Personal access tokens (classic) -> Copy token :  gOAEtrtyrt4567RFwAO17iAwoIY84k0nZ8QE

git remote set-url origin https://gOAEtrtyrt4567RFwAO17iAwoIY84k0nZ8QE@github.com/Subham966/test-repo-public.git

git push origin master
```

#**To create new branch:**

git branch dev
git push origin dev


#**untrack-> git add . -> stage -> git commit -> tracked**



#**-Commit-Hooks: (Before commit git will suggest the missing/wrong syntex)**
```bash

ls -a
cd .git/
ls -a
cd hooks

vi pre-commit
```


vscode:

file.exclude
delete **/.git


Install flake8 :
-----------------

sudo apt install flake8
flake8 demo.py

create a new file inside hooks:
pre-commit

files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')

flake8 $files

git add .
git commit -m "msg"


=============================================

# Password/api_key/secret:

if git grep -q "password\|secret_key\|API_KEY\|token" $(git diff --cached --name-only); then
    echo "Error: You have commited a password, secret or token"
    exit 1
fi
================================================

#!/bin/bash

# Python files
python_files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')
if [ -n "$python_files" ]; then
    echo "Running Flake8 for Python files..."
    flake8 $python_files
fi

# Java files
java_files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.java$')
if [ -n "$java_files" ]; then
    echo "Running Checkstyle for Java files..."
    checkstyle -c /google_checks.xml $java_files
fi

# React files (JavaScript and JSX)
react_files=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.jsx?$')
if [ -n "$react_files" ]; then
    echo "Running ESLint for React/JavaScript files..."
    eslint $react_files
fi

# .NET files (C#)
dotnet_files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.cs$')
if [ -n "$dotnet_files" ]; then
    echo "Running dotnet format for .NET files..."
    dotnet format $dotnet_files
fi

# Spring Boot files (Java and Kotlin)
springboot_files=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(java|kt)$')
if [ -n "$springboot_files" ]; then
    echo "Running SpotBugs for Spring Boot files..."
    spotbugs $springboot_files
fi

# HTML files
html_files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.html$')
if [ -n "$html_files" ]; then
    echo "Running HTMLLint for HTML files..."
    htmllint $html_files
fi

# CSS files
css_files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.css$')
if [ -n "$css_files" ]; then
    echo "Running Stylelint for CSS files..."
    stylelint $css_files
fi

# YAML files
yaml_files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.ya?ml$')
if [ -n "$yaml_files" ]; then
    echo "Running yamllint for YAML files..."
    yamllint $yaml_files
fi

# General linting error check
if [ $? -ne 0 ]; then
    echo "Linting failed! Please fix the issues before committing."
    exit 1
fi

echo "All checks passed. Proceeding with commit."


===================================

chmod +x .git/hooks/pre-commit

===========================================================
sudo apt-get install checkstyle
checkstyle -version

npm install -g eslint
eslint -v
eslint --init

dotnet tool install -g dotnet-format
dotnet format --version

npm install -g htmllint
htmllint --version

npm install -g stylelint stylelint-config-standard
stylelint --version
echo '{ "extends": "stylelint-config-standard" }' > .stylelintrc.json

pip install yamllint
yamllint --version

sudo apt install python3-pip
sudo apt install nodejs npm

