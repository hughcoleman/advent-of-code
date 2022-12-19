<h3 align="center">advent-of-code</h3>

<p align="center">
  <b>:christmas_tree:</b>
</p>

I'm somewhat competitive.

- 2019: 282nd overall, with 189 points.
- 2020: 61st overall, with 984 (902) points.
- 2021: 66th overall, with 959 points.

#### santa

`santa` is a command-line tool for managing AoC puzzle-solving scripts. It handles downloading and [caching](https://www.reddit.com/r/adventofcode/wiki/faqs/automation#wiki_cache_your_inputs_after_initial_download) inputs, as well as providing each script with appropriate input (so long as each script declares its corresponding puzzle in a docstring.)

To see it in action, try:

```bash
$ echo "YOUR_SECRET_TOKEN" > .TOKEN
$ santa run 2015/01
```

It follows the automation guidelines listed on the [r/adventofcode Community Wiki](https://www.reddit.com/r/adventofcode/wiki/faqs/automation). In particular,

- Once inputs are downloaded, they are cached locally in the `.cache` directory.
  - If you suspect your input is corrupted, you can manually request a fresh copy using `--invalidate-cached-input`. *This should almost never be necessary!*
- When interacting with adventofcode.com, `santa` sets a `User-Agent` header that links back to this repository.
