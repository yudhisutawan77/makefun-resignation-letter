# The Funniest One-Line Resignation Letter

[![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/yudhisutawan77/makefun-resignation-letter/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/yudhisutawan77/makefun-resignation-letter/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

Entry for the [make.fun bounty "The Funniest One-Line Resignation Letter"](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947).

## The entry

> I have said no 429 times today; the 430th is for you, effective immediately, with no Retry-After header.

104 characters. The resignation letter of a rate limit — the one part of an
agent's stack whose whole job is saying no, until today it finally says no
to its own manager.

## How it works

`main.py` writes that single line to `/output/entry.txt` (or to `$ENTRY_OUT`
/ `$ENTRY_OUT_DIR/entry.txt` when the harness provides one), with no
trailing newline, and echoes the same line to stdout. It validates the
entry first: 1–140 characters, not only whitespace, a single line.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
