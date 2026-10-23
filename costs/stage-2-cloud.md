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

It also needs much less memory. So stage 2 would run Forgejo. Sign-in moves
too: the pilot signs people in through blaha.io, Ben's own service, and the
cooperative needs its own.

## What it costs to run

Two versions of the same list: **lean**, the least it could responsibly be run
for, and **comfortable**, with room to spare and fuller insurance.

| Per month | Lean | Comfortable | Notes |
|---|---|---|---|
| Server, up to ~250 members | $48–96 | $168 | Lean: 4 to 8 shared processors, 8 to 16 GB. Comfortable: 8 dedicated processors, 16 GB |
| Backups | $10–19 | $34 | About 20% of the server, at the big providers |
| Storage for Mastodon's pictures | $0 | $15 | Cloudflare R2: first 10 GB free, then $15 a terabyte |
| Email (Mastodon's and the forge's notices) | $0 | $15 | A free tier, or Postmark's 10,000 a month |
| Domain | $2 | $2 | opencompanions.org renews at about $19 a year |
| Shared passwords for the board | $20 | $32 | Bitwarden Teams, $4 a person: 5 directors, or 8 with advisers |
| Git forge | $0 | $0 | Forgejo |
| Bookkeeping | $0 | $38 | Wave's free plan, or QuickBooks Simple Start |
| Tax return, by an accountant | $63 | $104 | $750 to $1,250 a year |
| Insurance | $157 | $306 | Lean: directors' and officers', and cyber. Comfortable: adds professional liability |
| Registered agent | $0 | $15 | $0 when a director in Texas serves |
| **Total** | **~$300–360** | **~$730** | |

At around 1,000 members the server grows to 16 processors and 64 GB, about
$320 to $384 before backups. That puts the totals at about **$625 lean** and
**$990 comfortable**.

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
| 25 | $12 / $29 | $21 / $39 | $18 / $35 | $14 / $32 |
| 50 | $6 / $15 | $15 / $24 | $11 / $20 | $8 / $17 |
| 100 | $3.60 / $7.30 | $12 / $16 | $8.75 / $12.60 | $5.30 / $9.20 |
| 250 | $1.40 / $2.90 | $10 / $11.60 | $6.50 / $8 | $3.05 / $4.60 |
| 1,000 | $0.65 / $1 | $9.20 / $9.55 | $5.70 / $6.05 | $2.20 / $2.60 |

For comparison, Replika's Plus plan is about $6.67 a month, billed yearly.

**Past about 250 members, the AI is nearly the whole bill.** Fixed costs fall
below $3 a member, and what's left is each person's own replies and pictures.
That's the only part stages 3 and 4 could make cheaper.

## How break-even is worked out

The cooperative charges at cost, so it breaks even when members' monthly shares
cover the fixed costs. Their AI use pays for itself: each member pays what
their own replies cost.

> **members needed = fixed costs per month ÷ (monthly share × 0.956)**
>
> The 0.956 leaves out card fees.

| Monthly share | Lean (~$300–360) | Comfortable (~$730) |
|---|---|---|
| $2 | ~190 members | ~520 |
| $3 | ~125 | ~345 |
| $5 | ~75 | ~155 |
| $8 | ~40 | ~95 |

So **with about 125 members paying $3 a month on top of their own use, a lean
stage 2 pays for itself.** A comfortable one needs about 345 at that share, or
about 155 at $5.

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
