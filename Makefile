# Default target
all: install-pdflatex

# Install pdflatex for Ubuntu/Debian
install-pdflatex:
	@echo "Installing pdflatex..."
	sudo apt update
	sudo apt install -y texlive-latex-extra
	@echo "pdflatex installed successfully."

# Install Python dependencies
install-requirements:
	@echo "Installing Python dependencies..."
	pip install -r requirements.txt
	@echo "Python dependencies installed successfully."

# Clean up generated files
clean:
	@echo "Cleaning up generated files..."
	rm -f *.aux *.log *.tex *.pdf
	@echo "Cleanup complete."

# Generate PDF (example usage: make generate TAG=Divisibility)
generate:
	@echo "Generating PDF for tag: $(TAG)..."
	python3 tag_selector.py $(TAG)
	@echo "PDF generation complete."

# Phony targets
.PHONY: all install-pdflatex install-requirements clean generate
