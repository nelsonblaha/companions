# Stage 4: our own hardware

*Part of [What it would cost](../COSTS.md). Prices seen on 23 October 2026.*

Like [stage 3](stage-3-cloud-gpus.md), but the GPU servers belong to the
cooperative. They sit in a data centre in Texas that rents out space, power and
a connection (colocation). The app server from [stage 2](stage-2-cloud.md)
stays as it is.

Owning costs a great deal up front and far less each month than renting. So
this stage is worked out two ways: against renting the same server, and against
paying OpenRouter by the reply.

## Two servers that could run the members' own model

Kimi K2.6, the pilot's default model, needs about 600 GB of GPU memory just to
load. These two servers both hold it:

| | 8 × NVIDIA RTX PRO 6000 (96 GB each) | 8 × NVIDIA H200 (141 GB each) |
|---|---|---|
| To buy, with Texas sales tax | **~$185,000** | **~$353,000** |
| Power it draws, at most | ~6 kW | ~10 kW |
| Colocation, Dallas, at ~$212 per kW a month | $1,270 | $2,160 |
| Bandwidth, and a reserve for spare parts | $525 | $910 |
| **Running cost a month** | **~$1,800** | **~$3,075** |
| Running cost plus the price spread over 3 years | ~$6,940 a month | ~$12,900 |
| The same, over 5 years | **~$4,880 a month** | **~$8,960** |

The RTX server is a build from parts, so its price is our estimate: eight cards
at about $16,000 each, plus a Supermicro chassis with eight GPU slots, processors
and memory. The H200 price is Supermicro's own starting price for the server.

**GPUs cost more than they did.** A shortage of memory chips has nearly doubled
the RTX PRO 6000's price since its launch, from about $8,600 to $16,000. Used
data-centre GPUs have been holding their value for the same reason, but nothing
here counts on selling them later.

## Against renting: how long until it pays back

> **months to pay back = price to buy ÷ (monthly rent − monthly running cost)**

| Renting the same thing | Rent a month | Owning pays back in |
|---|---|---|
| 8 × RTX PRO 6000, RunPod Secure Cloud ($2.49 per GPU per hour) | $14,540 | ~15 months |
| 8 × RTX PRO 6000, Nebius ($1.80) | $10,510 | ~21 months |
| 8 × H200, RunPod Secure Cloud ($5.29) | $30,890 | ~13 months |
| 8 × H200, Together, reserved for 3 to 6 months ($3.99) | $23,300 | ~17 months |
| 8 × H200, among the cheapest anywhere (~$2.00) | $11,680 | ~41 months, longer than it may last |

**So once a cooperative needs a GPU server all day, every day, owning beats
renting within one to two years**, unless rental prices fall a long way. A
server's useful life is usually taken as five years.

## Against paying by the reply: how many members

> **members needed = (running cost + price ÷ months of life) ÷ what each
> member's chat would cost on OpenRouter ($6.02 a month on Kimi K2.6)**

| | 8 × RTX PRO 6000 | 8 × H200 |
|---|---|---|
| Break-even, over 5 years | **~810 members** | **~1,490** |
| Break-even, over 3 years | ~1,150 | ~2,140 |
| Capacity, without caching | ~600 | ~1,000 |
| Capacity, with caching | ~1,600 | ~3,000 |
| Each member's share when full, over 5 years | ~$3.05 a month | ~$3 |

**It works only with caching.** Without it, each server fills up before it
pays for itself. With it, the RTX server pays from about 800 members and could
carry about 1,600, at roughly half what OpenRouter charges today.

**But OpenRouter's hosts cache too.** If the pilot's replies turn out to be 93%
cached there, a member's chat would cost about $2.47 a month through
OpenRouter. Then break-even rises to about 2,000 members for the RTX server,
more than it can carry, and owning wouldn't save money. Stage 1's measurements
decide this.

**What owning buys that money doesn't:** the same model, for as long as
members want it. Hosts drop models (two large ones already offer the next Kimi
instead of K2.6). A cooperative that owns its servers can keep a model members'
companions depend on running for years, whatever the market does.

## Pictures: the easy one

A GPU for pictures (an NVIDIA L40S, about $6,600) costs about nine months' rent
of the same GPU in the cloud, before power and a server to put it in. Of
everything here, it pays back soonest. It also lets adult accounts have
pictures, which Google's model forbids.

## Paying for it

**$185,000 or more has to exist before the first reply.** That could come from:
- **Member shares:** about $185 each from 1,000 members.
- **A loan:** that adds interest, which isn't counted here.
- **Saved surplus** from stage 2.

Whichever way, it's a decision for the members, not just the board, because it's
most of what the cooperative would own.

## What this stage depends on

- **Usage, and caching above all.** See [the overview](../COSTS.md#what-one-person-uses).
- **Capacity is estimated.** The H200 figures come from a published Kimi
  benchmark. The RTX figures come from volunteers' tests published on GitHub.
  Both should be checked by renting each server for a few hours on our own
  conversations, before buying.
- **Colocation prices vary.** Published Dallas prices run from about $146 to
  $293 per kW a month. Over five years that moves the RTX server's monthly cost
  between about $4,500 and $5,400. The H200 server's 10 kW needs more power than
  two standard circuits deliver, and dense racks cost more.
- **Someone has to look after it.** Hardware fails. Meta reported a faulty GPU or
  GPU memory as the cause of about half the interruptions in a 54-day run: about
  one interruption a year for every eleven GPUs. The warranty covers parts for
  one year and labour for three. The spares reserve here is 3% of the price a
  year. The people who swap parts and keep the software running aren't counted.

## What this leaves out

- **Tax deductions.** Faster tax write-offs exist, but a cooperative that returns
  its surplus to members has little taxable income to deduct from. So the prices
  here are spread evenly over the server's life.
- **Texas property tax on equipment.** It applies above the first $125,000 of
  equipment at each location, every year. The rate wasn't checked.
- **Insurance on the hardware, interest on a loan, and resale value.**

**A smaller option that doesn't scale:** Apple's Mac Studio with 512 GB of
memory can run Kimi K2.6 at about 3 bits on 270 watts. It writes about
22 tokens a second, for one or two conversations at a time, and the first reply
in a conversation waits about 24 seconds. That's enough for a handful of members, not
a cooperative. Apple stopped selling the 512 GB M3 Ultra in March 2026; the M5
Ultra had no published price on 23 October.

## Sources

Prices seen on 23 October 2026 unless noted.

- GPU and server prices:
  - [RTX PRO 6000 pricing](https://www.thundercompute.com/blog/nvidia-rtx-pro-6000-pricing), updated 16 October 2026
  - [Supermicro's store](https://store.supermicro.com/): SYS-821GE-TNHR (8 × H200), SYS-422GA-NRT (8 GPUs)
  - [L40S](https://gpudojo.com/l40s)
- Power:
  - [NVIDIA H200](https://www.nvidia.com/en-us/data-center/h200/)
  - the DGX H200 user guide
  - EIA Electric Power Monthly, table 5.6.A (Texas commercial, 8.47¢ per kWh, July 2026)
- Colocation: published Dallas plans from Cloudnium, Psychz and Tier.Net, via
  [Aliteq](https://aliteq.com/ai-server-colocation-cost-2026), 27 September 2026;
  CBRE's North America data centre trends, H2 2025 and H1 2026.
- Speeds:
  - Kimi on 8 × H200: [SemiAnalysis InferenceX](https://inferencex.semianalysis.com/blog/b200-nvfp4-vs-h200-int4-kimi-k2-vllm-perf-per-dollar)
  - Kimi K2.6 on 8 × RTX PRO 6000: [voipmonitor/rtx6kpro](https://github.com/voipmonitor/rtx6kpro)
  - Kimi K2.6 on a Mac Studio: [oMLX benchmarks](https://omlx.ai/benchmarks), 6 June 2026
- Rental prices: as in [stage 3](stage-3-cloud-gpus.md#sources).
- Failure rates: Meta, *The Llama 3 Herd of Models*
  ([arXiv 2407.21783](https://arxiv.org/abs/2407.21783)).
- Warranty: [Supermicro](https://www.supermicro.com/en/support/warranty).
- Depreciation: IRS Publication 946.
- Texas:
  - sales tax: [Comptroller](https://comptroller.texas.gov/taxes/sales/)
  - the $125,000 business personal property exemption from 2026: HB 9, as explained by [Dallas Central Appraisal District](https://www.dallascad.org/)
