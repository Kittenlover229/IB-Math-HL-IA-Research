compile:
	mkdir -p ./build/
	pdflatex -output-directory=build -jobname=latex main.tex

publish:
	mkdir -p ./build/
	pdflatex -output-directory=build -jobname=doc main.tex

clean:
	rm -rf ./build/
