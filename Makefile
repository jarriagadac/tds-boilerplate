install:
	# actualización del contenedor
	sudo apt update
	sudo apt -y upgrade
	
	# librerías para documentación
	sudo apt -y install nodejs npm pandoc chromium texlive-xetex graphviz libgraphviz-dev
	sudo npm install -g @marp-team/marp-core @marp-team/marp-cli
	
	# librerías para dev
	sudo apt -y install nodejs npm postgresql postgresql-contrib postgresql-client
	pip install --upgrade pip
	pip install -r requirements/base.txt -r requirements/dev.txt
