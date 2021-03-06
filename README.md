# Non-binary Name Generator
Procedurally generates non-binary people's names

Choose from an exciting selection such as:

```
Kaw   Xay   Eai   Lax   Wem   Hef   Gai
Ges   Xam   Taz   Yur   Una   Ich   Jai
Nhi   Lya   Kib   Yun   Vev   Cia   Jat
```

Combine with a [Deed Poll generator](https://deedpoll.lgbt/) to change your name today!

There's also [a branch](https://github.com/The-Silverwood-Institute/non-binary-name-generator/tree/fb_dump) that uses the Facebook names dump, but it produces terrible output

## Requirements

- Python 3.6 (or higher)

A file containing a list of names. You can fetch some from [here](http://www.nancy.cc/3-letter-baby-names/) like so:
```js
Array.from(document.querySelectorAll('a[href^="http://www.nancy.cc/baby-name/"]'))
  .map(element => element.textContent)
  .filter(name => name.length == 3)
  .join('\n');
```

## Usage

`python generate.py <path_to_names>`
