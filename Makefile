# Makefile for generating SVG files from text files
# Usage: make [LINE_WIDTH=25]

# Configuration
LINE_WIDTH ?= 25
TEMPLATE_FILE = templates/text.svg
SCRIPTS_DIR = scripts
OUTPUT_DIR = deploy
PYTHON_SCRIPT = generate_svg.py

# Find all .txt files in scripts directory
TXT_FILES := $(wildcard $(SCRIPTS_DIR)/*.txt)
SVG_FILES := $(patsubst $(SCRIPTS_DIR)/%.txt,$(OUTPUT_DIR)/%.svg,$(TXT_FILES))

# Default target
.PHONY: all
all: $(SVG_FILES)

# Rule to generate SVG files
$(OUTPUT_DIR)/%.svg: $(SCRIPTS_DIR)/%.txt $(TEMPLATE_FILE) $(PYTHON_SCRIPT)
	@echo "Generating SVG files with line width $(LINE_WIDTH)..."
	python3 $(PYTHON_SCRIPT) --line-width $(LINE_WIDTH) --template $(TEMPLATE_FILE) --scripts-dir $(SCRIPTS_DIR) --output-dir $(OUTPUT_DIR)

# Create output directory if it doesn't exist
$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

# Clean generated files
.PHONY: clean
clean:
	rm -rf $(OUTPUT_DIR)

# Display help
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  all     - Generate all SVG files (default)"
	@echo "  clean   - Remove generated files"
	@echo "  help    - Show this help message"
	@echo ""
	@echo "Configuration:"
	@echo "  LINE_WIDTH - Maximum line width for text wrapping (default: 25)"
	@echo ""
	@echo "Examples:"
	@echo "  make                    # Generate with default line width (25)"
	@echo "  make LINE_WIDTH=30      # Generate with line width 30"
	@echo "  make clean              # Clean generated files"

# Show current configuration
.PHONY: config
config:
	@echo "Current configuration:"
	@echo "  LINE_WIDTH: $(LINE_WIDTH)"
	@echo "  TEMPLATE_FILE: $(TEMPLATE_FILE)"
	@echo "  SCRIPTS_DIR: $(SCRIPTS_DIR)"
	@echo "  OUTPUT_DIR: $(OUTPUT_DIR)"
	@echo "  PYTHON_SCRIPT: $(PYTHON_SCRIPT)"
	@echo ""
	@echo "Found text files:"
	@for file in $(TXT_FILES); do echo "  $$file"; done

# Force rebuild of all files
.PHONY: rebuild
rebuild: clean all