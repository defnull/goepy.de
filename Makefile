.PHONY: clean new

build: venv
	. venv/bin/activate; pelican -vs blog-conf.py -o htdocs/blog/ blog-src/
	chmod -R +rX htdocs

preview: build
	python -m webbrowser htdocs/blog/index.html

deploy: build
	rsync -r htdocs/ marc@goepy.de:goepy.de/htdocs/

clean:
	rm -rfv output

new:
	bash make_post.sh

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate
