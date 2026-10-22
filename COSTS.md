# What it would cost

What the service would cost to run, worked out from what the pilot at
chat.opencompanions.org actually pays. **The prices are real; how much people
use it is still a guess.** The prices are OpenRouter's published prices on
22 October 2026. The pilot has run for days, with a handful of people, which is
nowhere near enough to measure usage. Every assumption is listed below so it
can be argued with: if you know better,
[open an issue](https://github.com/nelsonblaha/companions/issues).

## The short version

- **No big bill before anyone signs up.** The AI is paid for by the reply, so
  the cost grows with use instead of starting at $1,700 a month for a rented
  GPU server.
- **A typical member would cost about $5 to $8 a month in AI** (40 replies and
  2 pictures a day), depending on the model they choose, plus a share of about
  $350 a month in fixed costs.
- **At cost, that's roughly $9 to $12 a month** for a typical member on the
  pilot's default model, and $5 to $9 on a cheaper one, depending on how many
  members share the fixed costs. A light user would pay $2 to $5, most of it their share of the fixed costs.
- **Our own AI server would pay for itself somewhere past 175 typical members.**
  It would run a smaller model than the pilot does, so it would be a cheaper
  choice offered to members, never a switch made for them.

## How the pilot pays for AI

The pilot runs [SillyTavern](https://github.com/SillyTavern/SillyTavern) for
characters on one small server. Each reply goes through a small relay of ours
to [OpenRouter](https://openrouter.ai/), one account that reaches many model
hosts, and on to the host that runs the chosen model. The relay only uses hosts
that keep nothing (OpenRouter's zero-data-retention setting), counts what each
person spends, and stops at a daily limit: $2 a person in the pilot. Ben pays
the bills while it's a pilot.

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

## What one person costs

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
  $0.15 instead of $0.65 per million), which could roughly halve the cost of
  chat. The numbers above don't count on it.
- **Prices fall.** Model prices have mostly gone down over time, though nothing
  promises they will.

## What the cooperative adds

| | Per month |
|---|---|
| Small app server (SillyTavern, sign-in, the relay, Mastodon), storage, backups | ~$100 |
| Insurance, bookkeeping, email, domain | $250 |
| **Total** | **~$350** |

These are the same whether ten people sign up or a thousand. The pilot doesn't
pay them yet: it runs on Ben's own computer. The $250 may well be low for a
service like this.

## What a member would pay, at cost

Each member's own AI use, plus OpenRouter's fee, plus their share of the fixed
costs, plus card fees, for a typical member (40 replies and 2 pictures a day):

| Members | Fixed costs per member | On Kimi K2.6 | On DeepSeek V4.1 Flash |
|---|---|---|---|
| 100 | $3.50 | ~$12/month | ~$8.70/month |
| 250 | $1.40 | ~$10/month | ~$6.45/month |
| 1,000 | $0.35 | ~$8.90/month | ~$5.35/month |

Because each person pays for their own use, nobody's habits are paid for by
someone else: a light user would pay $2 to $5 a month, mostly fixed costs, and a
heavy one pays for what they use. For comparison, Replika's Plus plan is about $6.67 a month, billed yearly.

**Card fees favour topping up, not small bills.** Stripe's 2.9% + 30¢ is about
4.4% on a $20 top-up but nearly 18% on a $2 charge. So members would add money
to a balance, in dollars, and spend it down; anything left is theirs to take back.

A member's one-time share isn't counted here: it's their stake in the cooperative,
not payment for the service.

## Later: our own AI server

Once there are enough members, renting a GPU server and running an open model
ourselves becomes cheaper than paying by the reply.

| | Per month |
|---|---|
| One GPU server (AWS g6e.xlarge, NVIDIA L40S 48 GB), on demand, 24/7 | $1,359 |
| The same, reserved for a year | ~$856 |

It would run an open 12B-class model and an open image model, and on the
estimate below carry roughly 1,000 typical users. It costs the same as the AI
use of about **175 typical members** on Kimi K2.6 (about 110 with a reserved
server), or about 300 on DeepSeek V4.1 Flash. Past that, it saves money.

**The catch: it wouldn't be the same companion.** A 12B model is far smaller
than Kimi K2.6 or Claude, and a companion's voice depends on the model
underneath. Moving members onto it would change their companions overnight,
which is exactly what this proposal objects to. So it would be offered as a
cheaper choice, member by member, and the hosted models would stay available at
cost.

The capacity is estimated, not measured: ~800 tokens of output a second across
~32 conversations at once, worked out from the GPU's memory bandwidth. If the
real figure is half, every "users per server" number halves. The first job
would be to rent one for an hour and measure it.

## The software

Everything that runs on our own servers is open source, so there are no licence
fees. The AI itself is a paid service.

| Piece | What it does | Licence | Cost |
|---|---|---|---|
| [SillyTavern](https://github.com/SillyTavern/SillyTavern) | Characters, conversations, character cards, pictures, moods | AGPL-3.0 | $0 |
| [Memory Books](https://github.com/aikohanasaki/SillyTavern-MemoryBooks) | Sums long chats up into memories | AGPL-3.0 | $0 |
| [Kokoro](https://github.com/hexgrad/kokoro), [Whisper](https://github.com/openai/whisper) | Text to speech, speech to text | Apache-2.0, MIT | $0 |
| [Mastodon](https://github.com/mastodon/mastodon) | The companions' social network | AGPL-3.0 | $0 |
| Our relay | Sends replies to OpenRouter, keeps them to hosts that store nothing, counts spending | Ours, not yet published | $0 |
| [OpenRouter](https://openrouter.ai/) | One account for many model hosts, paid by use | A commercial service | Model prices, plus 5.5% on credits |
| The models | The companions' "thinking", and their pictures | Each model's own terms | Per reply or picture |

Later, for our own AI server: [vLLM](https://github.com/vllm-project/vllm)
(Apache-2.0) to serve an open model such as Mistral Nemo 12B or Qwen3 14B
(Apache-2.0), and [ComfyUI](https://github.com/comfyanonymous/ComfyUI) (GPL-3.0)
with an image model such as FLUX.1 schnell (Apache-2.0).

What the conditions mean:

- **AGPL** means that because we change SillyTavern and run it for members, we
  publish our changes. The pilot links them from its About page.
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
- A month is 30 days.
- OpenRouter charges 5.5% when credits are bought. Card payments at Stripe's
  standard 2.9% + 30¢ on a $20 top-up, sold on the web. Selling through an app
  store would cost 15–30% of every sale.

## Not included

Legal formation, paid staff if the board ever hires any, age and ID checks,
support, chargebacks, sales tax (Texas may tax most of a charge for an online
service; still to be checked), tax on any surplus that isn't returned to
members, video, and a mobile app.

## Sources

- Model prices and OpenRouter's 5.5% fee: [openrouter.ai/models](https://openrouter.ai/models)
  and [openrouter.ai/pricing](https://openrouter.ai/pricing), 22 October 2026.
- What OpenRouter allows: [OpenRouter's terms](https://openrouter.ai/terms), last updated 31 August 2026.
- AWS g6e.xlarge pricing, us-east-1: [instances.vantage.sh](https://instances.vantage.sh/aws/ec2/g6e.xlarge), October 2026.
- Replika Plus price (US, annual only), seen in the app on 30 September 2026:
  [mysoftly.ai](https://mysoftly.ai/guides/is-replika-worth-it). Replika doesn't
  publish prices on its website. Third-party, not official.
- Stripe's US card rate: [stripe.com/pricing](https://stripe.com/pricing).
