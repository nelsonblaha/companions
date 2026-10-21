# What it would cost

A first estimate of what the service would cost to run, how many people one
server can carry, and how many members it would take to cover it. **Nothing here
is measured yet.** Every assumption is listed below so it can be argued with: if
you know better, [open an issue](https://github.com/nelsonblaha/companions/issues).

## The short version

- **About $1,700 a month** before anyone signs up: one GPU server running all day,
  plus the small stuff.
- **One server carries roughly 250 heavy users, or about 1,000 typical ones.**
- **A few hundred paying members would cover it**, at well under what people pay
  companion apps now. At 1,000 members, an at-cost price works out to around
  **$2 a month**.

## Before anyone signs up

| | Per month |
|---|---|
| One GPU server (AWS g6e.xlarge, NVIDIA L40S 48 GB), on demand, 24/7 | $1,359 |
| Small app server, database, storage, backups | $100 |
| Insurance, bookkeeping, email, domain | $250 |
| **Total** | **$1,709** |

A one-year reservation brings the server down to about $856 a month, but it commits
to paying for the whole year.

## What one person costs

The server runs an open 12B-class model of the kind companion apps commonly use,
plus an image model for pictures.

| Kind of user | Replies a day | Pictures a day | Users per server | Server cost per user |
|---|---|---|---|---|
| Heavy | 150 | 10 | ~250 | ~$5.50/month |
| Typical | 40 | 2 | ~1,000 | ~$1.30/month |
| Light | 10 | 0 | ~6,000 | ~$0.20/month |

## How many members cover it

Measured against what people already pay Replika, as a yardstick:

| If members paid… | Members to break even | Of whom paying |
|---|---|---|
| What a heavy Replika spender pays (~$27.50/month) | ~65 | ~65 |
| Replika's Plus plan ($79.99/year) | ~265 | ~265 |
| A mix: 10% heavy, 30% Plus, 60% free | ~375 | ~150 |
| A worse mix: 3% heavy, 12% Plus, 85% free | ~1,100 | ~165 |

Or the other way round: what an **at-cost** price would be if everyone paid the
same, for typical usage, billed yearly.

| Members | Servers | Cost per month | At-cost price |
|---|---|---|---|
| 250 | 1 | $1,709 | ~$7/month |
| 500 | 1 | $1,709 | ~$3.55/month |
| 1,000 | 1 | $1,709 | ~$1.80/month |
| 2,500 | 3 | $4,426 | ~$1.85/month |

Heavy users cost about four times what typical ones do, so a real price list
would probably charge by usage rather than one flat fee.

## What's assumed

- **The server's capacity is estimated, not measured.** ~800 tokens (about 600 words)
  of output per second across ~32 conversations at once, worked out from the GPU's memory
  bandwidth. If the real figure is half, every "users per server" number halves.
  The first job is to rent one for an hour and measure it.
- **Usage is a guess.** Nobody outside the companies publishes how much people
  talk to their companions. The replies and pictures per day above are the
  numbers most worth correcting.
- Each reply re-reads about 8,000 tokens of character, memories and recent
  conversation, and writes about 200. Most of the re-read is cached.
- The server is sized for the busiest hour (10% of a day's traffic) at 70% load,
  so replies don't queue.
- Card payments at Stripe's standard 2.9% + $0.30, sold on the web. Selling
  through an app store would cost 15–30% of every sale.

## Not included

Legal formation, paid staff if the board ever hires any, voice and video, a
mobile app, age and ID checks, support, chargebacks, and tax on any surplus.

## Sources

- AWS g6e.xlarge pricing, us-east-1: [instances.vantage.sh](https://instances.vantage.sh/aws/ec2/g6e.xlarge), October 2026.
- Replika Plus and Max prices (US, annual only), seen in the app on 30 September
  2026: [mysoftly.ai](https://mysoftly.ai/guides/is-replika-worth-it). Replika
  doesn't publish prices on its website. Third-party, not official.
- Replika gem packs ($0.99–$19.99), App Store snapshot March 2026:
  [apppricinglab.com](https://apppricinglab.com/iap/apple/1158555867).
  Third-party. The "heavy spender" buying one $19.99 pack a month on top of the
  top plan is our assumption.
- Stripe's US card rate: [stripe.com/pricing](https://stripe.com/pricing).
