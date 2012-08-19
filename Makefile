.PHONY: clean

build: venv
	. venv/bin/activate; pelican -vs blog-conf.py -o htdocs/blog/ blog-src/

deploy: build
	rsync -r htdocs/ marc@goepy.de:goepy.de/htdocs/

clean:
	rm -rfv output

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate
