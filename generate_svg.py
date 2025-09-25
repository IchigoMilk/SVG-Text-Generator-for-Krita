#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import glob
import argparse

def get_text_width(text):
    """
    Calculate the character count of text (not visual width).
    Each character counts as 1, regardless of whether it's multibyte or not.
    """
    return len(text)

def wrap_text(text, max_width):
    """
    Wrap text to specified width, counting each character as 1.
    Each line will not exceed max_width in character count.
    """
    lines = text.split('\n')
    wrapped_lines = []
    
    for line in lines:
        if not line.strip():  # Empty line
            wrapped_lines.append('')
            continue
            
        current_line = ''
        words = line.split()
        
        for word in words:
            # Check if adding this word would exceed the limit
            test_line = current_line + (' ' if current_line else '') + word
            
            if len(test_line) <= max_width:
                current_line = test_line
            else:
                # If current_line is not empty, save it and start new line
                if current_line:
                    wrapped_lines.append(current_line)
                    current_line = word
                else:
                    # Single word is too long, need to break it
                    char_line = ''
                    for char in word:
                        test_char_line = char_line + char
                        if len(test_char_line) <= max_width:
                            char_line = test_char_line
                        else:
                            if char_line:
                                wrapped_lines.append(char_line)
                            char_line = char
                    if char_line:
                        current_line = char_line
        
        # Add any remaining text in current_line
        if current_line:
            wrapped_lines.append(current_line)
    
    return '\n'.join(wrapped_lines)

def read_template(template_path):
    """Read the SVG template file."""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Template file not found: {template_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading template: {e}", file=sys.stderr)
        sys.exit(1)

def read_text_file(text_path):
    """Read a text file and return its content."""
    try:
        with open(text_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        print(f"Error reading text file {text_path}: {e}", file=sys.stderr)
        return ""

def generate_svg(template_content, text_content):
    """Generate SVG by replacing (TEXT HERE) with the provided text."""
    return template_content.replace('(TEXT HERE)', text_content)

def main():
    parser = argparse.ArgumentParser(description='Generate SVG files from text files using template')
    parser.add_argument('--line-width', type=int, default=25, 
                       help='Maximum line width for text wrapping (default: 25)')
    parser.add_argument('--template', default='templates/text.svg',
                       help='Path to SVG template file (default: templates/text.svg)')
    parser.add_argument('--scripts-dir', default='scripts',
                       help='Directory containing text files (default: scripts)')
    parser.add_argument('--output-dir', default='deploy',
                       help='Output directory for SVG files (default: deploy)')
    
    args = parser.parse_args()
    
    # Read template
    template_content = read_template(args.template)
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Find all .txt files in scripts directory
    txt_pattern = os.path.join(args.scripts_dir, '*.txt')
    txt_files = glob.glob(txt_pattern)
    
    if not txt_files:
        print(f"No .txt files found in {args.scripts_dir}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Processing {len(txt_files)} text files with line width {args.line_width}...")
    
    # Process each text file
    for txt_file in sorted(txt_files):
        # Get base filename without extension
        base_name = os.path.splitext(os.path.basename(txt_file))[0]
        output_file = os.path.join(args.output_dir, f"{base_name}.svg")
        
        print(f"Processing: {txt_file} -> {output_file}")
        
        # Read and process text content
        text_content = read_text_file(txt_file)
        if not text_content:
            print(f"Warning: Empty or unreadable file: {txt_file}")
            continue
        
        # Apply text wrapping
        wrapped_text = wrap_text(text_content, args.line_width)
        
        # Generate SVG
        svg_content = generate_svg(template_content, wrapped_text)
        
        # Write output file
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            print(f"Generated: {output_file}")
        except Exception as e:
            print(f"Error writing {output_file}: {e}", file=sys.stderr)
    
    print("Done")

if __name__ == '__main__':
    main()