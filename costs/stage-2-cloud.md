# Stage 2: the cooperative's own cloud server

*Part of [What it would cost](../COSTS.md). Prices seen on 23 October 2026.*

The same stack the pilot runs today, moved from Ben's computers to one rented
cloud server that the cooperative's board controls together:

- **The chat:** SillyTavern, with the relay to OpenRouter, voice, and the
  pages for usage, invitations and ID.
- **The companions' Mastodon.**
- **A git forge** where members propose changes.

The AI is still bought by the reply through OpenRouter, so the server needs no
GPU. Members pay their own AI use at cost, plus a small monthly share of the
fixed costs.

This is the stage the cooperative could stay in for a long time. Stages
[3](stage-3-cloud-gpus.md) and [4](stage-4-own-hardware.md) only pay off with
far more members, so the numbers here are the ones that matter most.

## How the board runs it

- **The forge is where the cooperative is run.** Members raise issues and
  discuss them there, in the open, and the companions can open issues too.
- **Changes go in only when three directors agree.** Every change to the code,
  and to the server's own setup, is a merge request on the cooperative's forge.
  It's merged only when at least three directors have approved it.
- **The technical advisory board recommends.** Its members review merge
  requests and mark the ones they think are ready, so the directors know what's
  safe to approve. Their reviews show on the merge request but don't count
  towards the three.
- **Nobody holds the keys alone.** The cloud account belongs to the
  cooperative. Each director has their own login with two-factor
  authentication, and no one person keeps sole control of the server. A rule on
  the forge only holds if nobody can quietly go around it on the server.

**This changes one piece of the stack.** The pilot's forge is GitLab, and the
free edition of GitLab can't enforce "three directors must approve": its
approvals are optional. Required approvals, limited to chosen people, are in
GitLab Premium. Premium costs $29 a month for every account on it, members
included, which is $1,450 a month at 50 members. [Forgejo](https://forgejo.org/),
a free and open-source forge, has the rule built in at no cost:

- a required number of approvals;
- counting only approvals from a chosen team, such as the directors;
- clearing approvals when the change is edited;
- applying the rule to administrators too.

It also needs much less memory (about 0.1 GB, measured). So stage 2 would run
Forgejo. A preview of it, with these rules, runs for the pilot's members at
code.opencompanions.org. Sign-in moves
too: the pilot signs people in through blaha.io, Ben's own service, and the
cooperative needs its own.

## What it costs to run

Two versions of the same list: **lean**, the least it could responsibly be run
for, and **comfortable**, with room to spare and fuller insurance.

| Per month | Lean | Comfortable | Notes |
|---|---|---|---|
| Server, up to ~100 members | $90 | $160 | Lean: 16 GB, shared processors. Comfortable: 8 dedicated processors, 16 GB. Sizes are worked out below |
| Backups | $18 | $32 | About 20% of the server, at the big providers |
| Storage for Mastodon's pictures | $0 | $15 | Cloudflare R2: first 10 GB free, then $15 a terabyte |
| Email (Mastodon's and the forge's notices) | $0 | $15 | A free tier, or Postmark's 10,000 a month |
| Domain | $2 | $2 | opencompanions.org renews at about $19 a year |
| Shared passwords for the board | $20 | $32 | Bitwarden Teams, $4 a person: 5 directors, or 8 with advisers |
| Git forge | $0 | $0 | Forgejo |
| Bookkeeping | $0 | $38 | Wave's free plan, or QuickBooks Simple Start |
| Tax return, by an accountant | $63 | $104 | $750 to $1,250 a year |
| Insurance | $157 | $306 | Lean: directors' and officers', and cyber. Comfortable: adds professional liability |
| Registered agent | $0 | $15 | $0 when a director in Texas serves |
| **Total** | **~$350** | **~$720** | |

With more members the server grows, and so do the totals:

| Members | Server, lean / comfortable | Total a month, lean / comfortable |
|---|---|---|
| Up to ~100 | 16 GB: $90 / $160 | ~$350 / ~$720 |
| ~250 | 16 GB / 32 GB: $96 / $250 | ~$360 / ~$830 |
| ~1,000 | 64 GB: $320 / $500 | ~$625 / ~$1,130 |

### How big a server: measured on the pilot

The pilot measured what each piece uses, on 23 October 2026:

| | Memory |
|---|---|
| Voice (Kokoro, which reads replies aloud) | 2.1 GB |
| Mastodon, with its database | 0.6 GB |
| The forge (Forgejo) | 0.1 GB |
| Everything else: sign-in, the relay to the AI, the pages | 0.2 GB |
| **The server's own share, before any member is signed in** | **about 4 GB**, with the system itself |

Then there's SillyTavern, the chat program. It's made for one person and isn't
safe to share between people, so every member has their own copy. A copy runs
only while its member is using it: it stops after 30 minutes without use, and
starts again in about 4 seconds when they come back. Within half an hour of the
pilot switching this on, eight of its nine copies had stopped. While a copy is
running it uses:

- **about 0.12 GB**, measured;
- **about 0.7 to 0.9 GB** once it has loaded the two small AI models SillyTavern
  runs for itself, for the companion's moods (the pictures that change with
  their feelings) and for its long memory (finding earlier messages like the
  latest ones). Measured: 0.68 GB on a member's copy in use, and 0.87 GB on a
  fresh copy with both loaded.

So it matters where those two models run. In every copy, as the pilot runs them
today, each member using the chat costs most of a gigabyte. In one shared
service for everyone, a copy costs a tenth of that. The model itself takes
about 1 GB once. SillyTavern can already get its long memory from a shared
service. Moods can come from one too, or from the chat model.

How many copies run at once is the part not yet measured. Assuming 15% of
members use it in the same half hour at the busiest time of day:

| Members | Copies running | Models in every copy (as now) | Models shared (planned) |
|---|---|---|---|
| 50 | 8 | ~12 GB: 16 GB server | ~7 GB: 16 GB server |
| 100 | 15 | ~19 GB: 32 GB server | ~9 GB: 16 GB server |
| 250 | 38 | ~41 GB: 64 GB server | ~13 GB: 16 to 32 GB server |
| 1,000 | 150 | ~149 GB: three 64 GB servers | ~33 GB: 64 GB server |

The sizes include 20% headroom. **Sharing the models is worth doing before stage
2:** at 250 members it's the difference between a $96 to $250 server and a $320
to $500 one, and at 1,000 members, between one server and three. The tables
above assume it's done. The pilot will measure how many copies really run at
once, which is the number this most depends on.

**Insurance is the biggest line**, larger than the server. The figures are
brokers' published averages, not quotes; a real quote is one of the founding
board's first jobs.

**Servers have got dearer.** Hetzner, long the cheap choice, roughly tripled
its US cloud prices on 15 June 2026. The table uses DigitalOcean, Linode, Vultr
and Amazon Lightsail, which are close to each other. OVHcloud's US servers are
much cheaper ($23 a month for 8 processors and 24 GB), but that price appears
to need a year paid up front.

## What a member pays

Each member pays for their own AI use, plus OpenRouter's 5.5% fee, plus a share
of the fixed costs, plus card fees (about 4.4% when topping up $20 at a time).
The kinds of user are defined in [the overview](../COSTS.md#what-one-person-uses).

| Members | Fixed costs each, lean / comfortable | Typical member on Kimi K2.6 | Typical member on DeepSeek V4.1 Flash | Light member |
|---|---|---|---|---|
| 25 | $14 / $29 | $23 / $39 | $20 / $35 | $16 / $32 |
| 50 | $7 / $14 | $16 / $24 | $12 / $20 | $9 / $17 |
| 100 | $3.50 / $7.20 | $12 / $16 | $8.70 / $12.50 | $5.20 / $9.10 |
| 250 | $1.45 / $3.30 | $10 / $12 | $6.50 / $8.50 | $3.05 / $5 |
| 1,000 | $0.65 / $1.15 | $9.20 / $9.70 | $5.70 / $6.20 | $2.20 / $2.75 |

For comparison, Replika's Plus plan is about $6.67 a month, billed yearly.

**Past about 250 members, the AI is nearly the whole bill.** Fixed costs fall
to about $3 a member or less, and what's left is each person's own replies and pictures.
That's the only part stages 3 and 4 could make cheaper.

## How break-even is worked out

The cooperative charges at cost, so it breaks even when members' monthly shares
cover the fixed costs. Their AI use pays for itself: each member pays what
their own replies cost.

> **members needed = fixed costs per month ÷ (monthly share × 0.956)**
>
> The 0.956 leaves out card fees.

| Monthly share | Lean (~$350, more past 250 members) | Comfortable (~$720 to $1,130) |
|---|---|---|
| $2 | ~190 members | ~590 |
| $3 | ~125 | ~395 |
| $5 | ~75 | ~175 |
| $8 | ~45 | ~95 |

So **with about 125 members paying $3 a month on top of their own use, a lean
stage 2 pays for itself.** A comfortable one needs about 395 at that share, or
about 175 at $5. Both assume the models are shared (above); with a copy of
them in every member's SillyTavern, the comfortable server alone costs $250 more
a month at 250 members.

## One-time costs at the start

Not monthly, so not in the tables:
- moving the pilot over;
- the lawyer;
- paying back what Ben spent in [stage 1](stage-1-ben-pays.md), if the board
  agrees.

These are what members' one-time shares are for. A share is a member's stake in
the cooperative, not payment for the service: 100 members buying a $25 share
would raise $2,500.

## What this leaves out

- **Paid staff.** Running it is volunteer work until the board decides
  otherwise.
- **Support, age and ID checks, chargebacks, and sales tax.** Texas may tax
  most of a charge for an online service; that's one of the lawyer's
  questions.
- **Adult accounts.** Stripe doesn't process payments for AI sexual content.
  Adult accounts would need another payment processor, or members paying
  OpenRouter themselves.

## Sources

Prices seen on the vendors' own pages on 23 October 2026 unless noted.

- Memory: measured on the pilot (paul and nelnet), 23 October 2026: each
  service with `docker stats`, and a member's SillyTavern idle, in use, and on
  a fresh copy with its two local models loaded.
- Servers:
  - [DigitalOcean](https://www.digitalocean.com/pricing/droplets)
  - [Linode](https://www.linode.com/pricing/)
  - [Vultr](https://api.vultr.com/v2/plans)
  - [Amazon Lightsail](https://aws.amazon.com/lightsail/pricing/)
  - [OVHcloud US](https://us.ovhcloud.com/vps/)
  - Hetzner's [price adjustment](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/)
- GitLab:
  - [merge request approvals](https://docs.gitlab.com/user/project/merge_requests/approvals/), optional in the free edition
  - [pricing](https://about.gitlab.com/pricing/)
  - [which users are billable](https://docs.gitlab.com/subscriptions/manage_users_and_seats/)
- Forgejo's branch protection settings, from its source on Codeberg (22 October
  2026); the same options are documented by
  [Gitea](https://docs.gitea.com/usage/access-control/protected-branches), which
  Forgejo grew from.
- Storage and email: [Cloudflare R2](https://developers.cloudflare.com/r2/pricing/),
  [Postmark](https://postmarkapp.com/pricing).
- [Bitwarden](https://bitwarden.com/pricing/business/).
- Bookkeeping: [Wave](https://www.waveapps.com/pricing),
  [QuickBooks](https://quickbooks.intuit.com/pricing/).
- Accountant's fee for a corporate return: National Society of Accountants,
  2024 fee survey.
- Insurance, as brokers' averages:
  - [Insureon on D&O](https://www.insureon.com/small-business-insurance/directors-officers/cost)
  - [Insureon on cyber](https://www.insureon.com/small-business-insurance/cyber-liability/cost)
  - [Nonprofits Insurance Alliance](https://insurancefornonprofits.org/nonprofit-insurance-cost/); whether it covers a cooperative is unconfirmed
- Domain renewal: Namecheap's .org renewal price from price trackers (Namecheap's
  own page couldn't be read).
- [Stripe](https://stripe.com/pricing); Replika, as in [the overview](../COSTS.md#sources).
