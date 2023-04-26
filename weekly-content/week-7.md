---
layout: default
title: Week 7 - How to access online document
nav_order: 7
permalink: /weekly-content/week-7
---

# Week 7 - How to access online document
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

## HTML - The Hypertext Markup Language

HTML is the standard markup language for creating Web pages.

### HTML Elements

HTML elements are the building blocks of HTML pages.

HTML elements are represented by tags. The tags usually come in pairs like `<p>` and `</p>`.

| Tag | Description |
| --- | ----------- |
| `<html>` | Defines an HTML document |
| `<head>` | Contains metadata/information for the document |
| `<title>` | Defines a title for the document |
| `<body>` | Defines the document's body |
| `<h1>` to `<h6>` | Defines HTML headings |
| `<p>` | Defines a paragraph |
| `<br>` | Inserts a single line break |
| `<hr>` | Defines a thematic change in the content |
| `<a>` | Defines a hyperlink |
| `<img>` | Defines an image |
| `<table>` | Defines a table |
| `<tr>` | Defines a table row |
| `<th>` | Defines a table header |
| `<td>` | Defines a table cell |
| `<ul>` | Defines an unordered list |
| `<ol>` | Defines an ordered list |
| `<li>` | Defines a list item |
| `<div>` | Defines a section in a document |
| `<span>` | Defines a section in a document |
| `<input>` | Defines an input control |

### HTML Attributes

HTML attributes provide additional information about HTML elements.

HTML attributes are always specified in the start tag.

HTML attributes usually come in name/value pairs like: `name="value"`

| Attribute | Description |
| --------- | ----------- |
| `href` | Specifies the URL of the page the link goes to |
| `src` | Specifies the URL of the image |
| `alt` | Specifies an alternate text for an image |
| `width` | Specifies the width of an image |
| `height` | Specifies the height of an image |
| `style` | Specifies an inline style for an element |
| `class` | Specifies one or more class names for an element (refers to a class in a style sheet) |
| `id` | Specifies a unique id for an element (refers to a style in a style sheet) |

## CSS - Cascading Style Sheets

CSS describes how HTML elements are to be displayed on screen, paper, or in other media.

### CSS Syntax

A CSS rule-set consists of a selector and a declaration block:

```css
selector {
  property: value;
}
```

## Manipulating Web Documents Using Python

### Accessing Web Documents

The `urllib` module provides functions for accessing web documents.

The `urllib.request` module provides functions for accessing web documents.

The `urllib.request.urlopen()` function opens a web document and returns a file-like object.

```python
# Get the urllib.request functions
from urllib.request import *

# Open a web document
web_page = urlopen("https://www.google.com")

# Read the web document
web_page_content = web_page.read()

# Convert to unicode string
web_page_content = web_page_content.decode("UTF-8")

# Print the web document
print(web_page_content)
```

### Writing Text to a File

The `open()` function opens a file and returns a file-like object.

The `open()` function takes two arguments:

- The name of the file to open
- The mode to open the file in ('r' for read, 'w' for write, 'a' for append)

```python
# Open a file for writing
my_file = open("my_file.txt", "w")

# Write some text to the file
my_file.write("Hello World!")

# Close the file
my_file.close()
```


