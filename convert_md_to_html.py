#!/usr/bin/env python3
"""
Простой конвертер Markdown в HTML для статического сайта
"""

import os
import re
from pathlib import Path

def markdown_to_html(md_content):
    """Простая конвертация Markdown в HTML"""

    # Заголовки
    md_content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', md_content, flags=re.MULTILINE)

    # Жирный текст
    md_content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', md_content)

    # Курсив
    md_content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', md_content)

    # Ссылки
    md_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', md_content)

    # Списки
    lines = md_content.split('\n')
    in_list = False
    result_lines = []

    for line in lines:
        if line.strip().startswith('- '):
            if not in_list:
                result_lines.append('<ul>')
                in_list = True
            result_lines.append(f'  <li>{line.strip()[2:]}</li>')
        else:
            if in_list:
                result_lines.append('</ul>')
                in_list = False
            result_lines.append(line)

    if in_list:
        result_lines.append('</ul>')

    md_content = '\n'.join(result_lines)

    # Параграфы
    md_content = re.sub(r'\n\n', '</p><p>', md_content)
    md_content = f'<p>{md_content}</p>'

    return md_content

def create_html_wrapper(title, content):
    """Создает HTML обертку для контента"""
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #f8f9fa;
        }}
        .container {{
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        h1, h2, h3, h4 {{
            color: #667eea;
            margin-top: 30px;
            margin-bottom: 15px;
        }}
        h1 {{
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}
        a {{
            color: #667eea;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        ul, ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 5px 0;
        }}
        .back-link {{
            display: inline-block;
            margin-bottom: 20px;
            color: #666;
            text-decoration: none;
            font-size: 14px;
        }}
        .back-link:hover {{
            color: #667eea;
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="../index.html" class="back-link">← Назад к главной</a>
        {content}
    </div>
</body>
</html>"""

def convert_markdown_files():
    """Конвертирует все Markdown файлы в HTML"""
    www_dir = Path(__file__).parent
    doc_dir = www_dir / 'doc'

    if not doc_dir.exists():
        print("Папка doc не найдена")
        return

    # Находим все .md файлы
    md_files = list(doc_dir.rglob('*.md'))

    for md_file in md_files:
        print(f"Конвертирую: {md_file}")

        # Читаем Markdown
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Конвертируем в HTML
        html_content = markdown_to_html(md_content)

        # Создаем HTML файл
        html_file = md_file.with_suffix('.html')
        title = md_file.stem.replace('_', ' ').title()

        full_html = create_html_wrapper(title, html_content)

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(full_html)

        print(f"Создан: {html_file}")

if __name__ == "__main__":
    convert_markdown_files()
    print("Конвертация завершена!")
