
clean:
	python3 setup.py clean
sdist: clean
	python3 setup.py sdist

bdist_wheel: clean
	python3 setup.py bdist_wheel

install:
	python3 setup.py install

upload: sdist bdist_wheel
	twine upload dist/*

	

