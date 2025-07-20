install:
	# actualización del contenedor
	sudo apt update
	sudo apt -y upgrade
	# librerías para documentación
	sudo apt -y install nodejs npm pandoc chromium texlive-xetex
	sudo npm install -g @marp-team/marp-core @marp-team/marp-cli
	# librerías para python
	pip install --upgrade pip
	pip install -r requirements.txt
