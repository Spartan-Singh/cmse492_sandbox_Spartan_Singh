# 1) One-sentence description of project

 This project's goal was to learn how to setup a python virtual enviorment and how to recreate that same enviormnet's setting within other enviroments.


# 2a) Setup (venv) section

## 1. Create the virtual environment

 From the terminal type the following:
 python -m venv .venv


## 2. Activate the virtual environment

 From the terminal type the following on macOS:
 source .venv/bin/activate

## 3. Install required packages

 From the terminal type the following:
 python -m pip install --upgrade pip
 python -m pip install numpy pandas matplotlib

## 4. Verify the installation

 From the terminal type the following:
 python -c "import numpy, pandas, matplotlib; print('packages OK')"


# 2b) Setup (conda) section

## 1. Create the conda environment

 From the terminal, navigate to the project folder that contains `environment.yml`, then type the following:
 conda env create -f environment.yml


## 2. Activate the conda environment

 From the terminal type the following:
 conda activate day03-conda-env


## 3. Verify the installation

 From the terminal type the following:
 python --version
 python -c "import numpy, pandas, matplotlib; print('All packages OK.')"


## 4. Run the analysis

 Make sure the conda environment is activated, then run the following command from the project root:
 python src/simple_analysis.py


## 5. Deactivate the conda environment

 When finished, deactivate the environment by typing:
 conda deactivate


## Updating the conda environment

 If `environment.yml` is modified in the future, update the existing conda environment with:
 conda env update -f environment.yml --prune


# 3) Analysis section

## Path For Each folder:

cmse492_sandbox : /Users/anmol/Documents/Uni_Code/CMSE492/cmse492_sandbox
day02_venv_demo : /Users/anmol/Documents/Uni_Code/CMSE492/cmse492_sandbox/day02_venv_demo
.venv : /Users/anmol/Documents/Uni_Code/CMSE492/cmse492_sandbox/day02_venv_demo/.venv
data : /Users/anmol/Documents/Uni_Code/CMSE492/cmse492_sandbox/day02_venv_demo/data
notebooks : /Users/anmol/Documents/Uni_Code/CMSE492/cmse492_sandbox/day02_venv_demo/notebooks
src : /Users/anmol/Documents/Uni_Code/CMSE492/cmse492_sandbox/day02_venv_demo/src
.gitignore : /Users/anmol/Documents/Uni_Code/CMSE492/cmse492_sandbox/day02_venv_demo/.gitignore
README.md : /Users/anmol/Documents/Uni_Code/CMSE492/cmse492_sandbox/day02_venv_demo/README.md
requirements.txt : /Users/anmol/Documents/Uni_Code/CMSE492/cmse492_sandbox/day02_venv_demo/requirements.txt
Notes : /Users/anmol/Documents/Uni_Code/CMSE492/cmse492_sandbox/Notes

## Analysis P2

The analysis for this assignment is a Python script located at:

/Users/anmol/Documents/Uni_Code/CMSE492/cmse492_sandbox/day02_venv_demo/src/simple_analysis.py

The script creates a small dataset using pandas. It then calculates the average score from the data and visualizes the results using a simple line plot with matplotlib.

To run the analysis, make sure the virtual environment is activated, then run the following command from the terminal:

python src/simple_analysis.py
