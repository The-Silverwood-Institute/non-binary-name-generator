# non-binary-name-generator
Procedurally generates non-binary people's names

Choose from an exciting selection such as:

```
Kaw   Xay   Eai   Lax   Wem   Hef   Gai
Ges   Xam   Taz   Yur   Una   Ich   Jai
Nhi   Lya   Kib   Yun   Vev   Cia   Jat
```

Combine with a [Deed Poll generator](https://deedpoll.lgbt/) to change your name today!

## Requirements

- Python 3.6 (or higher)

A list of `names.txt`. You can fetch some from [here](http://www.nancy.cc/3-letter-baby-names/) like so:
```js
Array.from(document.querySelectorAll('a[href^="http://www.nancy.cc/baby-name/"]'))
  .map(element => element.textContent)
  .filter(name => name.length == 3)
  .join('\n');
```
