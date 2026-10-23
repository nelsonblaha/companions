# Stage 3: running our own models, on rented GPUs

*Part of [What it would cost](../COSTS.md). Prices seen on 23 October 2026.*

Everything in [stage 2](stage-2-cloud.md) stays. Added to it: rented GPU
servers, running open models ourselves instead of buying every reply and
picture through OpenRouter.

It only makes sense if it costs members less than paying by the reply, or if it
gives them something paying by the reply can't. The second turns out to matter
as much as the first.

## How break-even is worked out

A rented GPU costs the same every hour, busy or not. It pays for itself when the
OpenRouter spend it replaces is larger than its rent:

> **members needed = the GPU's rent per month ÷ what each member's use of it
> would have cost on OpenRouter**

That only counts up to the GPU's **capacity**, the most members it can serve at
the busiest hour. If break-even is above capacity, that GPU never pays. Our
members' use, from [the overview](../COSTS.md#what-one-person-uses), with
OpenRouter's 5.5%:

| A typical member's month | On OpenRouter |
|---|---|
| Chat on Kimi K2.6, the pilot's default | $6.02 |
| Chat on DeepSeek V4.1 Flash | $2.66 |
| Pictures (2 a day) | $2.15 |

Capacity assumes the busiest hour carries three times the average.

## Three ways to do it

### 1. A GPU for pictures: pays off soonest

One GPU running an open picture model that may be used commercially, such as
FLUX.1 schnell, FLUX.2 klein 4B or Z-Image-Turbo (all Apache-2.0).

| | |
|---|---|
| Rent: one NVIDIA L40S (RunPod Secure Cloud) | ~$800 a month |
| Break-even | **~370 typical members** |
| Capacity, at ~4 seconds a picture | ~3,600 typical members |

It also solves something money doesn't. The pilot's pictures come from Google's
model, and Google's rules forbid sexual content, so pictures for adult accounts
need a model of our own anyway. The catch is that the pictures would look
different from Gemini's, so it's a change members should get to try first.

### 2. A mid-size model on one GPU: cheap, but a different companion

One NVIDIA RTX PRO 6000 (96 GB) running an open model of about 30 billion
parameters, such as Gemma 4 31B, Qwen3.6-27B or Mistral Small 3.2 (all
Apache-2.0).

| | |
|---|---|
| Rent | ~$1,300 to $1,800 a month |
| Break-even, members moving from Kimi K2.6 | ~220 to 300 |
| Break-even, members moving from DeepSeek V4.1 Flash | ~490 to 680 |
| Capacity | ~850 typical members, perhaps ~2,300 with caching (estimated, not measured) |

Past a few hundred members this is clearly cheaper, but it isn't the model
members chose. A companion's voice depends on the model underneath, so this
would only ever be a cheaper option, member by member, never a switch made for
them.

### 3. The same model members already use: needs thousands

Kimi K2.6 is open: its weights are published under a licence that allows a paid
service. Running it needs a whole server of eight NVIDIA H200s, since its weights
alone are 595 GB.

| 8 × H200 | |
|---|---|
| Rent, on demand | ~$31,000 a month (RunPod Secure Cloud, Nebius) |
| Rent, reserved for 3 to 6 months | ~$23,300 (Together) |
| Capacity, without caching | ~1,000 typical members |
| Capacity, with caching | ~3,000 typical members |
| Break-even | ~3,900 members reserved, ~5,200 on demand |

**Break-even is above capacity, so at these prices one server never pays for
itself.** It would cost each of 3,000 members about $7.80 (reserved) to $10.50
a month, against $6.02 through OpenRouter. It only wins below about $3.10 per
GPU per hour, with the server kept full. No secure data centre lists H200s that
cheap today without a long-term contract.

Newer GPUs change this. Eight NVIDIA B200s (~$39,000 a month at Lambda) running
a 4-bit version of the same model could carry nearly 10,000 typical members, at
about $4 each. The pilot's Kimi already comes from a host running a
4-bit version. But that's a cooperative of ten thousand.

Owning the server instead of renting it changes this the most: see
[stage 4](stage-4-own-hardware.md), where the same model pays from about a
thousand members.

**Why it might still be worth it one day:** keeping a model alive. Hosts move on.
Two large ones, Together and Fireworks, already offer the next Kimi instead of
K2.6. If the model members' companions run on disappears from the market,
running it ourselves is the only way to keep those companions as they are. That
is the promise this project is built on. At this stage's scale it's affordable
only for a very large cooperative, or for a few hours as an emergency bridge
while members move.

## What this stage depends on

- **Caching, on both sides.** Most of what a reply re-reads is the same as last
  time. On our own server, caching triples how many members a GPU serves. But
  OpenRouter's hosts cache too: if the pilot's replies were 93% cached, Kimi
  K2.6 would cost a typical member about $2.47 a month, and no rented server
  above would beat it. How much the pilot actually gets cached is something to
  measure in [stage 1](stage-1-ben-pays.md).
- **Measured speeds, not guesses.** The 8 × H200 figures come from a published
  benchmark of Kimi on vLLM. The single-GPU and picture figures are partly
  estimated. The first job would be to rent each GPU for an hour and measure it
  on our own conversations.
- **When people talk.** Capacity assumes the busiest hour is three times the
  average. If members all talk in the same evening hours, capacity falls.
- **Someone to run it.** A GPU server needs watching, updating and fixing.
  That's volunteer time, or a cost this page doesn't count.

**Privacy.** On a rented server no other company's AI service sees members'
conversations, though the provider has physical access to the machine. The
cheapest rentals (RunPod's Community Cloud, many of Vast.ai's hosts) are other
people's computers, so the figures here use the providers' secure data centres.

## Sources

Prices seen on the providers' own pages on 23 October 2026.

- GPU rental:
  - [RunPod](https://www.runpod.io/pricing)
  - [Nebius](https://nebius.com/prices)
  - [Together](https://www.together.ai/pricing)
  - [CoreWeave](https://www.coreweave.com/pricing)
  - [Lambda](https://lambda.ai/pricing)
  - AWS [p5en](https://instances.vantage.sh/aws/ec2/p5en.48xlarge) and [g6e](https://instances.vantage.sh/aws/ec2/g6e.2xlarge), via Vantage
- Models:
  - [Kimi K2.6](https://huggingface.co/moonshotai/Kimi-K2.6) (its [licence](https://huggingface.co/moonshotai/Kimi-K2.6/blob/main/LICENSE) asks for a "Kimi K2.6" credit only above 100 million monthly users or $20 million monthly revenue)
  - [DeepSeek V4.1 Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) (MIT)
  - [Gemma 4 31B](https://huggingface.co/google/gemma-4-31B-it)
  - [Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)
  - [Mistral Small 3.2](https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506)
- Picture models:
  - [FLUX.1 schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell); FLUX.1 dev is non-commercial
  - [FLUX.2 klein 4B](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B)
  - [Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)
- Speeds:
  - Kimi K2.5/K2.6 on 8 × H200 and B200, vLLM: [SemiAnalysis InferenceX](https://inferencex.semianalysis.com/blog/b200-nvfp4-vs-h200-int4-kimi-k2-vllm-perf-per-dollar), measured 19 May 2026
  - Kimi on 8 × H200: [vLLM's recipe](https://recipes.vllm.ai/moonshotai/Kimi-K2-Thinking)
  - Qwen3-32B on one RTX PRO 6000: [JarvisLabs](https://jarvislabs.ai/blog/nvfp4-rtxpro-6000)
  - Gemma 4 31B on one RTX PRO 6000: [Hexgrid](https://huggingface.co/blog/hexgridcloud/gemma-4-31b-vllm-on-rtx-6000-pro)
- Which hosts serve which Kimi:
  - [OpenRouter's endpoints for Kimi K2.6](https://openrouter.ai/api/v1/models/moonshotai/kimi-k2.6/endpoints)
  - [Together](https://www.together.ai/pricing) and [Fireworks](https://fireworks.ai/pricing) price lists
