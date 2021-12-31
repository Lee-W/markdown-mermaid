# md_mermaid

mermaid extension for Python-Markdown to add support for mermaid graph inside markdown file

## Installation

For `pip` installation (only python version >=3.x) :

```shell
pip install markdown
pip install git+https://github.com/Lee-W/md_mermaid#egg=md_mermaid
```

## Usage

In your python script :

```python
import markdown

text = """
# Title

Some text.

​```mermaid
graph TB
A --> B
B --> C
​```

Some other text.

​```mermaid
graph TB
D --> E
E --> F
​```
"""

html = markdown.markdown(text, extensions=['md_mermaid'])

print(html)
```

Output will result in :

```html
<h1>Title</h1>
<p>Some text.</p>
<div class="mermaid">
graph TB
A --> B
B --> C
</div>

<p>Some other text.</p>
<div class="mermaid">
graph TB
D --> E
E --> F
</div>

<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true});</script>
```

The `<script>...</script>` line appears only once even if there are several graphs in the file.

## How to use it with pelican

Add the following `md_mermaid: {}` to `MARKDOWN["extension_configs"]` in your `pelicanconf.py`

```python
MARKDOWN = {
    "extension_configs": {
        "md_mermaid": {},
    },
}
```
