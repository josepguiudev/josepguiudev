#cd C:/Users/josep/Desktop/Proyectos Personales/Portfolio
#venv/Scripts/activate
#cd C:/Users/josep/Desktop/Proyectos Personales/Portfolio/venv/Scripts/python.exe
#-m pip install --upgrade pip
#cd C:/Users/josep/Desktop/Proyectos Personales/Portfolio
#pip install -r requirements.txt
#reflex init
#reflex export --frontend-only
#rm -fr public
#unzip frontend.zip -d public
#rm -f frontend.zip
#venv/Scripts/deactivate

cd "C:/Users/josep/Desktop/Proyectos Personales/Portfolio"
venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install typer==0.9.0 click==8.1.3
reflex export --frontend-only
Remove-Item -Recurse -Force public
Expand-Archive -Path frontend.zip -DestinationPath public
Remove-Item frontend.zip
deactivate