# Stage 1: Ben pays

*Part of [What it would cost](../COSTS.md). Figures as of 23 October 2026.*

The pilot at chat.opencompanions.org, for a few invited friends, on Ben's own
computers, paid for by Ben. It has three jobs: show that it works, measure how
much people actually use it, and get the cooperative legally and financially
set up, starting with its five founding directors.

There's no break-even in this stage, because nobody pays. What matters is how
much Ben could be out of pocket, and when the pilot has to move on.

## What runs where

| Piece | Where | Cost to the pilot |
|---|---|---|
| The chat: SillyTavern, the relay to OpenRouter, voice, sign-in | paul, Ben's workstation at home | Nothing extra: it runs anyway |
| Mastodon (social.opencompanions.org) and the git forge (git.blaha.io) | nelnet, Ben's server at home | Nothing extra: it runs anyway |
| Reaching them from the internet | Cloudflare Tunnel, free plan | $0 |
| Signing in | blaha.io, Ben's own sign-in service | $0 |
| The AI: every reply and picture | OpenRouter, paid by use | See below |
| opencompanions.org | Namecheap, registered 22 October 2026 | About $9 the first year, then about $19 a year |

Measured on paul and nelnet on 23 October, the whole stack uses about 7 GB of
memory and almost no processor while idle. The git forge (about 2.8 GB) and
the voice service (about 2.6 GB) are most of it. The chat itself uses under
600 MB.

## What it has cost so far

| | |
|---|---|
| AI through the chat, 21 to 23 October (the relay's own count) | $3.95 |
| Everything billed to the OpenRouter account so far | $7.48 |
| Credits Ben has bought | $50 |

The difference between the first two lines is building the pilot: character
portraits and mood pictures made outside the chat, test conversations, and a
few cents for another of Ben's projects on the same account. The pilot has run
for days with a handful of people, so these numbers say almost nothing yet
about what a member uses. Measuring that is this stage's main job.

## How much Ben could be out of pocket

The relay stops for the day at a cap, so the AI bill can't run away:

| Cap | Today | Worst case per month |
|---|---|---|
| Everyone together | $5 a day | ~$158, with OpenRouter's 5.5% |
| One person | $2 a day | |
| Pictures | 80 a day | (inside the $5) |

A typical member, as [the overview](../COSTS.md#what-one-person-uses) defines
one, uses about 26¢ a day on the pilot's default model. **So the $5 cap covers
about 19 typical members.** Past that, the cap starts turning people away by
evening, and there are three ways out:

1. **Raise the cap.** Ben's choice, from Ben's pocket.
2. **Members pay OpenRouter themselves.** OpenRouter can link a member's own
   account to an app, and their replies are billed to their own credits. No
   money passes through Ben, so there's nothing to sell and no sales tax. The
   relay's rules (hosts that keep nothing, the age setting) would stay the same.
   Each member would need their own OpenRouter account, which requires being 18.
3. **Move to [stage 2](stage-2-cloud.md),** once the cooperative exists and can
   take payment.

## Setting up the cooperative

Costs that come with this stage, before there's a cooperative to pay them:

| | Cost | Notes |
|---|---|---|
| Certificate of formation, Texas Secretary of State | $25 | Texas Business Organizations Code, chapter 251 |
| Federal tax number (EIN) | $0 | |
| A lawyer, for the founding documents and the open questions | Unknown | Likely the largest cost of the stage |
| Registered agent | $0, or $100 to $250 a year | $0 if a director in Texas serves; otherwise a commercial agent |

The open questions for the lawyer: sales tax on an online service in Texas,
selling member shares to people outside Texas, and the content rules for adult
accounts.

## Paying Ben back

Ben may later ask the board to reimburse what he spent: OpenRouter, the domain,
the filing fee, the lawyer. How we'd suggest handling it, so it's never a way
for a founder to cash out:

- **Receipts only.** OpenRouter's billing history, Namecheap's invoice, the
  state's receipt. Ben's time isn't on the list.
- **At cost.** No interest and no markup.
- **The board decides, without Ben's vote** if he's a director, and records it.
- **Only when the cooperative can.** Paid from member shares or surplus, never
  ahead of running costs, so the cooperative never owes Ben in a way that
  steers it.

Whether a new cooperative can take on its founder's earlier costs this way is a
question for the lawyer.

## When stage 1 ends

When the cooperative exists, with its directors, a bank account and a way to
take payment, and enough people want to join to cover the fixed costs of
[stage 2](stage-2-cloud.md). That stage's page works out how many that is.

## Sources

- AI spending: the relay's own ledger, and OpenRouter's account totals, read on
  23 October 2026.
- Memory use: measured on paul and nelnet, 23 October 2026.
- Domain: Namecheap's .org prices from price trackers such as
  [domainoffer.net](https://domainoffer.net/tld/org/namecheap), since Namecheap's
  own page couldn't be read. The registration date is from the .org registry.
- Filing fee: Texas Secretary of State,
  [form 806](https://www.sos.texas.gov/corp/forms/806_boc.pdf), certificate of
  formation for a cooperative association.
- Registered agents: published prices of Harbor Compliance, ZenBusiness,
  Registered Agents Inc and LegalZoom, 23 October 2026.
