# SVG Text Generator for Krita

This project generates SVG files from text files using a template, with proper UTF-8 multibyte character support for Japanese text.

日本語での動作確認しかしていません。日本語では文字数で折り返し、英語(単語単位で半角スペースを設ける言語)では文字数を超えない単語単位での折り返し動作をします。

## Background & Purpose

This tool is designed to create SVG text elements for use in Krita. Krita allows pasting SVG files as vector layers, which is particularly useful for adding formatted text to artwork. By generating SVG files from plain text files, you can:

- Prepare text content with consistent formatting for digital artwork
- Apply line wrapping to ensure text fits within designated areas
- Maintain proper Unicode support for Japanese and other multibyte characters

Note: You will need to manually paste the generated SVG files into Krita as vector layers and adjust their position as needed.

## Files

- `generate_svg.py` - Main script
- `templates/text.svg` - SVG template with `(TEXT HERE)` placeholder (default template is configured for vertical Japanese text layout)
- `scripts/*.txt` - Text files to be embedded into SVG
- `deploy/` - Output directory for generated SVG files (created automatically)

## Usage

### Basic Usage

Generate SVG files with default settings (25 character line width):
```bash
make
```

### Custom Line Width

Generate SVG files with custom line width:
```bash
make LINE_WIDTH=30
```

### Other Commands

```bash
make help       # Show help message
make config     # Show current configuration
make clean      # Remove generated files
make rebuild    # Clean and rebuild all files
```

## Example

Input file `scripts/01-p1-1.txt`:
```
充電器のケーブルが落ちる物音で目が覚めた。
```

With `LINE_WIDTH=15`, generates `deploy/01-p1-1.svg` with wrapped text:
```
充電器のケーブルが落ちる物音で
目が覚めた。
```
