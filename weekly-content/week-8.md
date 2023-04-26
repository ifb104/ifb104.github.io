---
layout: default
title: Week 8 - How to Find Things
nav_order: 8
permalink: /weekly-content/week-8
---

# Week 8 - How to Find Things
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

## Regular Expressions

Some regular expression primitives:

| Primitive | Description |
| --- | ----------- |
| a | Matches the specified character |
| ab | Matches the specified characters in order |
| [abc] | Matches a single character from the specified set of characters |
| . | Matches any single character except newline characters |
| [b-m] | Matches any single character from the specified range of characters |
| [^xy] | Matches any single character not in the specified set of characters |
| ^ | Matches the starting position within the string |
| $ | Matches the ending position of the string |
| \b | Matches a word boundary (end or beginning of word) |
| \d | Matches any decimal digit |
| \D | Matches any non-decimal digit |
| \s | Matches a whitespace character |
| \S | Matches a non-whitespace character |
| \n | Matches a newline character |

Some regular expression operators:

| Operator | Description |
| --- | ----------- |
| P* | Matches zero or more occurrences of the preceding expression |
| P+ | Matches one or more occurrences of the preceding expression |
| P? | Matches zero or one occurrence of the preceding expression |
| P{N} | Matches exactly N occurrences of the preceding expression |
| P{N,} | Matches at least N occurrences of the preceding expression |
| P{N,M} | Matches at least N and at most M occurrences of the preceding expression |
| P{,M} | Matches at most M occurrences of the preceding expression |
| P \| Q | Matches either P or Q |
| (P) | Matches P and stores the match |
| (?:Q) | Matches Q and does not store the match |

## Regular Expressions in Python

### `re.findall()`

Example: Find all tags in a HTML document

```python
from re import findall

string = """
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <h1>This is a Heading</h1>
            <p>This is a paragraph.</p>
        </body>
    </html>
"""
pattern = r"<.*?>"
result = findall(pattern, string)

print(result)
# Output: ['<html>', '<head>', '<title>', '</title>', '</head>', '<body>', '<h1>', '</h1>', '<p>', '</p>', '</body>', '</html>']
```

### Grouping

Example: Find content of each paragraph in a HTML document, excluding the tags

```python
from re import findall

string = """
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <h1>This is a Heading</h1>
            <p>This is a paragraph.</p>
            <p>This is another paragraph.</p>
        </body>
    </html>
"""

pattern = r"<p>(.*?)</p>"
result = findall(pattern, string)

print(result)
# Output: ['This is a paragraph.', 'This is another paragraph.']
```

### Greedy vs Non-Greedy

Greedy: `.*` - find all characters until the last occurrence of the next character or line break

Non-Greedy: `.*?` - find all characters until the first occurrence of the next character or line break

Example: Find content of each paragraph in a trimmed HTML document

```python
from re import findall

string = "<html><head><title>Page Title</title></head><body><h1>This is a Heading</h1><p>This is a paragraph.</p><p>This is another paragraph.</p></body></html>"

# Greedy
result = findall(r"<p>(.*)</p>", string)
print(result)
# Output: ['This is a paragraph.</p><p>This is another paragraph.']

# Non-Greedy
result = findall(r"<p>(.*?)</p>", string)
print(result)
# Output: ['This is a paragraph.</p><p>This is another paragraph.</p>']
```