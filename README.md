# SVG Text Generator for Krita

[English](#english) | [日本語](#日本語)

---

## English

### Overview

This project generates SVG files from text files using a template, with proper UTF-8 multibyte character support for Japanese text. The tool is specifically designed to create SVG text elements for use in Krita, allowing you to easily add formatted text to your artwork.

### Background & Purpose

This tool is designed to create SVG text elements for use in Krita. Krita allows pasting SVG files as vector layers, which is particularly useful for adding formatted text to artwork. By generating SVG files from plain text files, you can:

- Prepare text content with consistent formatting for digital artwork
- Apply automatic line wrapping to ensure text fits within designated areas
- Maintain proper Unicode support for Japanese and other multibyte characters
- Control text layout with custom line width settings
- Support for indentation using full-width spaces (　)

Note: You will need to manually paste the generated SVG files into Krita as vector layers and adjust their position as needed.

### Features

- **Automatic Line Wrapping**: Wraps text at specified character width
- **Japanese Text Support**: Proper handling of Japanese characters and punctuation
- **Indentation Support**: Leading full-width spaces (　) are converted to proper indentation in SVG
- **Customizable Templates**: Use your own SVG templates with custom fonts and styling
- **Batch Processing**: Process multiple text files at once
- **Vertical Text Layout**: Default template supports Japanese vertical writing (can be customized)

### Requirements

- Python 3.x
- Make (for using Makefile commands)
- Krita (for using the generated SVG files)

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

### Python Script Usage

You can also run the Python script directly for more control:

```bash
python3 generate_svg.py --line-width 25 --template templates/text.svg --scripts-dir scripts --output-dir deploy
```

Options:
- `--line-width`: Maximum line width for text wrapping (default: 25)
- `--template`: Path to SVG template file (default: templates/text.svg)
- `--scripts-dir`: Directory containing text files (default: scripts)
- `--output-dir`: Output directory for SVG files (default: deploy)

### Example

Input file `scripts/01-p1-1.txt`:
```
充電器のケーブルが落ちる物音で目が覚めた。
```

With `LINE_WIDTH=15`, generates `deploy/01-p1-1.svg` with wrapped text:
```
充電器のケーブルが落ちる物音で
目が覚めた。
```

### Using in Krita

1. Generate SVG files using this tool
2. Open Krita
3. Drag and drop the SVG file into your canvas, or use **File > Import > Import as Vector Layer**
4. Adjust the position and size of the text layer as needed
5. The text will remain as editable vector data

### Customizing the Template

You can customize the SVG template (`templates/text.svg`) to change:
- Font family
- Font size
- Text color (fill)
- Writing mode (horizontal/vertical)
- Letter spacing
- Line height

The template must contain `(TEXT HERE)` placeholder where the text will be inserted.

### Troubleshooting

**Problem**: Generated SVG files are empty
- **Solution**: Make sure your text files are in UTF-8 encoding and contain text

**Problem**: Text doesn't wrap correctly
- **Solution**: Adjust the `LINE_WIDTH` parameter to a smaller value

**Problem**: Japanese punctuation appears at line start
- **Solution**: The script automatically handles this by keeping punctuation with the previous line

**Problem**: Font not found in Krita
- **Solution**: Make sure the font specified in the template is installed on your system

---

## 日本語

### 概要

このプロジェクトは、テンプレートを使用してテキストファイルからSVGファイルを生成するツールです。日本語テキストのUTF-8マルチバイト文字を適切にサポートしています。Kritaでベクターレイヤーとして使用できるSVGテキスト要素を作成することを目的としています。

### 背景と目的

このツールは、Kritaで使用するSVGテキスト要素を作成するために設計されています。KritaではSVGファイルをベクターレイヤーとして貼り付けることができ、これはアートワークにフォーマットされたテキストを追加するのに特に便利です。プレーンテキストファイルからSVGファイルを生成することで、以下のことができます：

- デジタルアートワーク用に一貫したフォーマットでテキストコンテンツを準備
- 指定されたエリア内にテキストが収まるように自動的に行を折り返し
- 日本語やその他のマルチバイト文字のUnicodeサポートを維持
- カスタム行幅設定でテキストレイアウトを制御
- 全角スペース（　）を使用したインデント対応

注意：生成されたSVGファイルは、手動でKritaにベクターレイヤーとして貼り付け、必要に応じて位置を調整する必要があります。

### 特徴

- **自動行折り返し**: 指定された文字幅でテキストを折り返します
- **日本語テキストサポート**: 日本語文字と句読点の適切な処理
- **字下げサポート**: 先頭の全角スペース（　）はSVG内で適切なインデントに変換されます
- **カスタマイズ可能なテンプレート**: 独自のフォントやスタイリングでSVGテンプレートを使用可能
- **バッチ処理**: 複数のテキストファイルを一度に処理
- **縦書きレイアウト**: デフォルトテンプレートは日本語縦書きに対応（カスタマイズ可能）

### 動作について

日本語での動作確認のみ行っています。日本語では文字数で折り返し、英語（単語単位で半角スペースを設ける言語）では文字数を超えない単語単位での折り返し動作をします。

### 必要なもの

- Python 3.x
- Make（Makefileコマンドを使用する場合）
- Krita（生成されたSVGファイルを使用する場合）

### ファイル構成

- `generate_svg.py` - メインスクリプト
- `templates/text.svg` - `(TEXT HERE)`プレースホルダーを含むSVGテンプレート（デフォルトテンプレートは日本語縦書きレイアウト用に設定されています）
- `scripts/*.txt` - SVGに埋め込まれるテキストファイル
- `deploy/` - 生成されたSVGファイルの出力ディレクトリ（自動的に作成されます）

### 使い方

#### 基本的な使い方

デフォルト設定（25文字の行幅）でSVGファイルを生成：
```bash
make
```

#### カスタム行幅

カスタム行幅でSVGファイルを生成：
```bash
make LINE_WIDTH=30
```

#### その他のコマンド

```bash
make help       # ヘルプメッセージを表示
make config     # 現在の設定を表示
make clean      # 生成されたファイルを削除
make rebuild    # クリーンして全ファイルを再ビルド
```

#### Pythonスクリプトの直接実行

より詳細な制御が必要な場合は、Pythonスクリプトを直接実行できます：

```bash
python3 generate_svg.py --line-width 25 --template templates/text.svg --scripts-dir scripts --output-dir deploy
```

オプション：
- `--line-width`: テキスト折り返しの最大行幅（デフォルト: 25）
- `--template`: SVGテンプレートファイルのパス（デフォルト: templates/text.svg）
- `--scripts-dir`: テキストファイルを含むディレクトリ（デフォルト: scripts）
- `--output-dir`: SVGファイルの出力ディレクトリ（デフォルト: deploy）

### 使用例

入力ファイル `scripts/sample.txt`:
```
充電器のケーブルが落ちる物音で目が覚めた。
```

`LINE_WIDTH=15`の場合、折り返されたテキストで`deploy/sample.svg`を生成：
```
充電器のケーブルが落ちる物音で
目が覚めた。
```

### Kritaでの使用方法

1. このツールを使用してSVGファイルを生成
2. Kritaを開く
3. SVGファイルをキャンバスにドラッグ＆ドロップ、または**ファイル > インポート > ベクターレイヤーとしてインポート**を使用
4. 必要に応じてテキストレイヤーの位置とサイズを調整
5. テキストは編集可能なベクターデータとして保持されます

### テンプレートのカスタマイズ

SVGテンプレート（`templates/text.svg`）をカスタマイズして以下を変更できます：
- フォントファミリー
- フォントサイズ
- テキスト色（fill）
- 書字方向（横書き/縦書き）
- 文字間隔
- 行の高さ

テンプレートには、テキストが挿入される場所に`(TEXT HERE)`プレースホルダーを含める必要があります。

### トラブルシューティング

**問題**: 生成されたSVGファイルが空
- **解決策**: テキストファイルがUTF-8エンコーディングでテキストが含まれていることを確認してください

**問題**: テキストが正しく折り返されない
- **解決策**: `LINE_WIDTH`パラメータをより小さい値に調整してください

**問題**: 日本語の句読点が行頭に表示される
- **解決策**: スクリプトは自動的にこれを処理し、句読点を前の行に保持します

**問題**: Kritaでフォントが見つからない
- **解決策**: テンプレートで指定されたフォントがシステムにインストールされていることを確認してください

### ライセンス

MIT License - 詳細は[LICENSE](LICENSE)ファイルを参照してください。
