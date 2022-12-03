compile:
	mkdir -p ./build/
	pdflatex -output-directory=build -jobname=latex main.tex

clean:
	rm -rf ./build/
