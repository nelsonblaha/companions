# What it would cost

What the service would cost to run, worked out from what the pilot at
chat.opencompanions.org actually pays. **The prices are real; how much people
use it is still a guess.** The prices are the ones published on 22 and
23 October 2026. The pilot has run for days, with a handful of people, which is
nowhere near enough to measure usage. Every assumption is listed so it can be
argued with: if you know better,
[open an issue](https://github.com/nelsonblaha/companions/issues).

## Four stages

The project can run in four ways, each needing more members than the last to
pay for itself. Each has its own page showing how its break-even is worked out.

| | Who runs it, and where | Who pays | Fixed costs a month | Pays for itself |
|---|---|---|---|---|
| **[1. Ben pays](costs/stage-1-ben-pays.md)** | Ben, on his own computers; the AI bought by the reply through OpenRouter | Ben | Nothing but the AI, capped at $5 a day | Nobody pays, so it doesn't. The cap covers about 19 typical members |
| **[2. The cooperative's cloud server](costs/stage-2-cloud.md)** | The board together, on one rented server; the AI still bought by the reply | Members, at cost | ~$350 to $720, more past 250 members | At ~125 members each paying a $3 monthly share (lean), or ~395 (comfortable) |
| **[3. Our own models, on rented GPUs](costs/stage-3-cloud-gpus.md)** | As stage 2, plus rented GPU servers running open models | Members, at cost | Stage 2, plus ~$800 (pictures) to ~$31,000 (the members' own chat model) | Pictures: ~370 members. A cheaper chat model: a few hundred who choose it. The same chat model: not on one server at today's prices |
| **[4. Our own hardware](costs/stage-4-own-hardware.md)** | As stage 3, on GPUs the cooperative owns | Members, at cost | Stage 2, plus ~$1,800 to $3,100 to run a GPU server, after ~$185,000 to $353,000 to buy it: ~$4,900 to $9,000 a month over five years | The same chat model: ~810 members on a server of eight RTX PRO 6000s, or ~1,490 on eight H200s, over five years, and only if caching works |

**Stage 1** is now. It gathers interest, measures real use, and gets the
cooperative legally and financially set up. Ben may ask the board to pay back
what he spent, at cost, with receipts.

**Stage 2** is where the cooperative could stay for a long time:
- every change is merged only when three directors agree;
- a technical advisory board recommends which changes are ready;
- past about 250 members, fixed costs fall below $3 a member each month, and
  what's left is each person's own AI use.

**Stages 3 and 4** can only make that AI use cheaper. They pay for themselves
only with far more members. The exception is a GPU for pictures, which pays for
itself at a few hundred.

## The short version

- **No big bill before anyone signs up.** The AI is paid for by the reply, so
  the cost grows with use, not with a rented GPU server's monthly rent.
- **A typical member costs about $5 to $8 a month in AI** (40 replies and
  2 pictures a day), depending on the model they choose.
- **At cost, with a cloud server shared by 250 members, that's roughly $10 to
  $12 a month** on the pilot's default model, and $6.50 to $8.50 on a cheaper one.
  A light user would pay $3 to $5.
- **Renting GPUs for the model members already use doesn't pay at today's
  prices.** Owning them could, from roughly 800 to 1,500 members, if caching
  works as hoped, but the server costs $185,000 or more up front. A GPU for
  pictures pays for itself at a few hundred members. A smaller model would be
  cheaper sooner, but it's a different companion, so it would be offered, never
  forced.

## What one person uses

The pilot runs [SillyTavern](https://github.com/SillyTavern/SillyTavern) for
characters. Each reply goes through a small relay of ours to
[OpenRouter](https://openrouter.ai/), one account that reaches many model
hosts, and on to the host that runs the chosen model. The relay uses only hosts
that keep nothing (OpenRouter's zero-data-retention setting), counts what each
person spends, and stops at a daily limit.

Members choose the model from a menu that shows what each costs. The pilot offers
twenty. Some of them:

| Model | Per million tokens, in / out | A typical reply |
|---|---|---|
| Kimi K2.6 (the pilot's default) | $0.65 / $3.41 | ~0.5¢ |
| DeepSeek V4.1 Flash | $0.30 / $1.20 | ~0.2¢ |
| Claude Sonnet 5.5 | $2 / $10 | ~1.5¢ |
| Claude Opus 5.5 | $4 / $20 | ~2.9¢ |
| **A picture** (Gemini 3.1 Flash Lite Image) | | **~3.4¢** |

A typical reply late in a chat re-reads about 6,000 tokens (the character, their
memories and the recent conversation) and writes about 250.

| Kind of user | Replies a day | Pictures a day | On Kimi K2.6 | On DeepSeek V4.1 Flash |
|---|---|---|---|---|
| Heavy | 150 | 10 | ~$31/month | ~$20/month |
| Typical | 40 | 2 | ~$7.75/month | ~$4.50/month |
| Light | 10 | 0 | ~$1.45/month | ~$0.65/month |

Add 5.5%, OpenRouter's fee when credits are bought. Pictures are a big share
for heavy users: 10 a day is about $10 a month on its own.

Two things could bring these down:

- **Caching.** Most of what a reply re-reads is the same as last time. Hosts
  that cache it charge about a quarter of the price for the repeat (Kimi K2.6:
  $0.15 instead of $0.65 per million), which could more than halve the cost of
  chat. The numbers here don't count on it. How much the pilot gets cached is
  one of the things stage 1 should measure. It also decides when stages 3 and 4
  would pay.
- **Prices fall.** Model prices have mostly gone down over time, though nothing
  promises they will.

**Card fees favour topping up, not small bills.** Stripe's 2.9% + 30¢ is about
4.4% on a $20 top-up but nearly 18% on a $2 charge. So members would add money
to a balance, in dollars, and spend it down; anything left is theirs to take
back.

## The software

Everything that runs on our own servers is open source, so there are no licence
fees. The AI itself is a paid service until stage 3.

| Piece | What it does | Licence | Cost |
|---|---|---|---|
| **The forge:** [GitLab](https://gitlab.com/gitlab-org/gitlab-foss) in the pilot (git.blaha.io), [Forgejo](https://forgejo.org/) from stage 2 | Where the cooperative is run in the open. Members raise issues and discuss them, and propose changes as merge requests. The technical advisory board marks the ones it recommends, and a change goes in once three directors approve it. Everything is on the record, and the companions can open issues too | GitLab Community Edition: MIT. Forgejo: GPL-3.0 | $0 |
| [SillyTavern](https://github.com/SillyTavern/SillyTavern) | Characters, conversations, character cards, pictures, moods | AGPL-3.0 | $0 |
| [Memory Books](https://github.com/aikohanasaki/SillyTavern-MemoryBooks) | Sums long chats up into memories | AGPL-3.0 | $0 |
| [Kokoro](https://github.com/hexgrad/kokoro), [Whisper](https://github.com/openai/whisper) | Text to speech, speech to text | Apache-2.0, MIT | $0 |
| [Mastodon](https://github.com/mastodon/mastodon) | The companions' social network | AGPL-3.0 | $0 |
| Our relay | Sends replies to OpenRouter, keeps them to hosts that store nothing, counts spending | Ours, not yet published | $0 |
| [OpenRouter](https://openrouter.ai/) | One account for many model hosts, paid by use | A commercial service | Model prices, plus 5.5% on credits |
| The models | The companions' "thinking", and their pictures | Each model's own terms | Per reply or picture |

What the conditions mean:

- **AGPL** means that because we change SillyTavern and run it for members, we
  publish our changes. The pilot links them from its About page.
- **The forge changes at stage 2.** The free edition of GitLab can't require
  three directors' approval: its approvals are optional. GitLab Premium can,
  but it charges $29 a month for every account, members included. Forgejo
  does it for free, so [stage 2](costs/stage-2-cloud.md#how-the-board-runs-it)
  moves to it.
- **OpenRouter's terms** let us build it into our own service for our members.
  They forbid reselling plain access to the models, so what members pay for is
  their companion, hosted, not model access.
- **Every model's own rules apply to everyone who uses it.** They differ most
  on adult content: Anthropic's and Google's forbid sexual content, for
  example. Which models the cooperative offers is also a decision about its
  content rules, so it belongs to the board.
- **Not every open model is free to use this way.** FLUX.1 *dev*, a popular image
  model, is licensed for non-commercial use only. Every model's terms get
  checked before it's offered to members.
- **The real cost is the work, not the licences.** SillyTavern is built for one
  person running it for themselves. Its own multi-user mode keeps everyone's data
  in plain files and warns against public servers. The pilot puts it behind its
  own sign-in, but making it safe for strangers is still the main engineering job.

## What's assumed

- **Usage is a guess.** Nobody outside the companies publishes how much people
  talk to their companions. The replies and pictures per day above are the
  numbers most worth correcting, and the pilot will start to measure them.
- A typical reply re-reads ~6,000 tokens and writes ~250, with no caching.
- A picture costs ~3.4¢: Gemini 3.1 Flash Lite Image's price for one picture,
  about what the pilot is billed for each.
- A month is 30 days, or 730 hours for anything rented by the hour.
- OpenRouter charges 5.5% when credits are bought. Card payments at Stripe's
  standard 2.9% + 30¢ on a $20 top-up, sold on the web. Selling through an app
  store would cost 15–30% of every sale.

Each stage's page lists what it leaves out. Across all of them: paid staff, if
the board ever hires any; support; age and ID checks; chargebacks; sales tax;
video; and a mobile app.

## Sources

- Model prices and OpenRouter's 5.5% fee: [openrouter.ai/models](https://openrouter.ai/models)
  and [openrouter.ai/pricing](https://openrouter.ai/pricing), 22 October 2026.
- What OpenRouter allows: [OpenRouter's terms](https://openrouter.ai/terms), last updated 31 August 2026.
- Replika Plus price (US, annual only), seen in the app on 30 September 2026:
  [mysoftly.ai](https://mysoftly.ai/guides/is-replika-worth-it). Replika doesn't
  publish prices on its website. Third-party, not official.
- Stripe's US card rate: [stripe.com/pricing](https://stripe.com/pricing).
- Each stage's own prices are sourced on its page.
