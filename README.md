# Network-Programmability-ACCA5029-Team-Kichuk-Paris
This is the repository of team Kichuk Paris for assessment 1 of Network Programmability ACCA5029. This a Flask based weather app showing the current weather conditions for the searched location including some historical events for that location plus some interesting stats for the city and country the user is looking for...

Installation

Linux and 


Windows 10 and 11

1: Download the latest version of Python installer from https://www.python.org/downloads/ for your version of Windows
2: Install Python using the default settings which include 'pip' and make sure python.exe is added to PATH
3: Open Command Prompt as Administrator and check python and pip versions by executing the following command:

python --version

pip --version

Both command should return the versions accordingly which means both programs are installed correctly
4: Install virtual environment by executing the below command:

pip install virtualenv

5: Create a folder where the application files will be unpacked, got that folder and execute the below commands to create a virtual python environment and activate it:

virtualenv venv

venv\Scripts\Activate

6: In order to install Flask in the folder above execute the below command:

pip install Flask requests

7: Clone the GitHub repository or unpack the already downloaded archive in the above folder and execute the below:

python app.py

Now the development server is started and the application can be access from any browser at http://127.0.0.1:5000 or http://localhost:5000


Linux - Debian/Ubuntu, CentOS/RHEL/Fedora

1: Open a terminal and execute the below command for Debian/Ubuntu to install virtual environment

sudo apt install python-virtualenv

1: Open a terminal and execute the below command for CentOS/RHEL/Fedora to install virtual environment

sudo yum install python-virtualenv

or

sudo dnf install python-virtualenv

2: Create a folder where the application files will be unpacked, got that folder and execute the below commands to create a virtual python environment and activate it:

python3 -m venv venv

venv/bin/activate

3: In order to install Flask in the folder above execute the below command:

pip install Flask requests

4: Clone the GitHub repository or unpack the already downloaded archive in the above folder and execute the below:

python app.py

Now the development server is started and the application can be access from any browser at http://127.0.0.1:5000 or http://localhost:5000

If any errors during the process, please check the log files and refer to Linux distribution documentation