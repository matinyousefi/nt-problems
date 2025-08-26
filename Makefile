# Default target
all: install-pdflatex

# Install pdflatex for Ubuntu/Debian
install-pdflatex:
	@echo "Installing pdflatex..."
	sudo apt update
	sudo apt install -y texlive-latex-extra
	@echo "pdflatex installed successfully."

# Install xelatex for Ubuntu/Debian
install-xelatex:
	@echo "Installing xelatex..."
	sudo apt update
	sudo apt install -y texlive-xetex texlive-fonts-recommended texlive-lang-arabic texlive-lang-other
	@echo "xelatex installed successfully."

# Install Python dependencies
install-requirements:
	@echo "Installing Python dependencies..."
	pip install -r requirements.txt
	@echo "Python dependencies installed successfully."

# Clean up generated files
clean:
	@echo "Cleaning up generated files..."
	rm -f *.aux *.log *.tex *.pdf *.out
	@echo "Cleanup complete."

# Generate PDF (example usage: make generate TAG="Divisibility")
generate:
	@echo "Generating PDF for tag: $(TAG)..."
	python3 ./tools/tag_selector.py "$(TAG)"
	@echo "PDF generation complete."

generate-fr:
	@echo "Generating PDF with translation for tag: $(TAG)..."
	python3 ./tools/tag_selector.fr.py "$(TAG)"
	@echo "PDF generation complete."

# Phony targets
.PHONY: all install-pdflatex install-xelatex install-requirements clean generate generate-fr
