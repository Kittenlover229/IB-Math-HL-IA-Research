publish:
	@make compile
	@make compile

compile:
	@mkdir -p ./build/
	@pdflatex -output-directory=build -jobname=doc main.tex

wordcount:
	@make publish
	@pdftotext ./build/doc.pdf && wc ./build/doc.txt --words 

clean:
	rm -rf ./build/
