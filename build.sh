cd C:/Users/josep/Desktop/Proyectos Personales/Portfolio
venv/Scripts/activate
cd C:/Users/josep/Desktop/Proyectos Personales/Portfolio/venv/Scripts/python.exe
-m pip install --upgrade pip
cd C:/Users/josep/Desktop/Proyectos Personales/Portfolio
pip install -r requirements.txt
reflex init
reflex export --frontend-only
rm -fr public
unzip frontend.zip -d public
rm -f frontend.zip
venv/Scripts/deactivate