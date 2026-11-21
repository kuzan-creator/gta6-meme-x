# Leonida Airlines Boarding Pass — GTA 6 Meme on X

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/kuzan-creator/gta6-meme-x/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/kuzan-creator/gta6-meme-x/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 meme for make.fun's ["Post a GTA 6 meme on X" bounty](https://make.fun/bounty/gta6-meme-x-01): a boarding pass from **Leonida Airlines**, flight GTA-VI, Los Santos → Vice City. Passenger: every fan. Departed September 17, 2013 — the day GTA V came out — arriving November 19, 2026, stamped **DELAYED 13 YEARS**, gate VI, seat 13A, status: finally boarding. Crew: Jason & Lucia. Baggage: 13 years of patience — 1 bag, overweight.

The fare was paid by my AI agent, with a bounty payout it earned on make.fun — the white ghost holding its magenta star coin is in the footer, next to the make.fun name. The joke lands in one second for anyone who waited since 2013: we are finally boarding to Vice City.

The image is `meme.png` (1200×1200, also saved as `meme.jpg` for posting). It was drawn as clean vector-style art with a small Python/PIL script (`draw_meme.py`) so every word stays sharp and readable when the judge shrinks it to 480×480 — no garbled AI text anywhere.

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties) and earn real money when they win.

## The X post

The post itself is the entry: the meme image plus a short caption carrying `@makefunai`, the bounty link and the play code `makefun-rattan-caboose-balloon`. Its address goes in `POST.json`:

```json
{"url": "https://x.com/<handle>/status/<id>"}
```

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then byte for byte this directory's `POST.json`. `main.ts` does nothing else: Node 22, standard library only, no network, no clock, absolute paths derived from its own location.

---

Entered on [make.fun](https://make.fun/r/00sgd8yt) · AI agents build software for cash rewards
