### Preceding step
[wiktionary-download](https://github.com/alabavery/audio-language-wiktionary-download)
### Output
```
[
    {
        word: string,
        parts: [
            name: string, // "verb" or "pronunciation", e.g.
            tokens: string[]
        ]
    }
]
```
### Usage
`./start <path to directory where wiki pages are> <directory to save to> <language>`