# Companions

The source of <https://companions.blaha.io/>, a proposal for a nonprofit,
member-governed home for AI companions, built on one promise: you can always
take your companion somewhere else.

Nothing is running yet. No organization is formed and no board exists. The page
is here to find out whether people want this, and this repository is here so that
anyone can suggest a change to it, the people it's written for most of all.

## Suggesting a change

If something on the page is wrong, out of date, or could be said better, open an
[issue](https://github.com/nelsonblaha/companions/issues) or a pull request.
[CONTRIBUTING.md](CONTRIBUTING.md) explains how, including how to preview the
page on your own computer. You don't need to know how to code to open an issue.

## What's here

| Path | What it is |
|---|---|
| `site/index.html` | The page, in English. Plain HTML: no template language and no build step. |
| `site/es/`, `pt/`, `id/`, `ja/`, `zh/` | The same page in Spanish, Brazilian Portuguese, Indonesian, Japanese and Traditional Chinese. |
| `deploy/strings/` | Each language's form messages and buttons, with notes on the translation choices most worth a native speaker's check. |
| `site/style.css` | This page's colours and headline width. Everything else comes from campaignlanding. |
| `site/img/` | The mark, and Maria's character card in each language. |
| `deploy/` | The small server that serves the page and receives the signup form. |
| `COSTS.md` | What the service would cost to run, and how many members would cover it. Estimates, with every assumption listed. |

The machinery behind the page is
[campaignlanding](https://github.com/nelsonblaha/campaignlanding), which this
site shares with [chucodata.org](https://chucodata.org/). Improvements that would
help any campaign page belong there rather than here.

## The signup form

The form posts to our own server, which appends one line per signup to a file on
the host. No Google Forms, no Mailchimp, no third-party form service, no
analytics, and no HTTP endpoint that returns anyone's contact details. The list
never enters this repository; `deploy/app.py` is the whole of the code that is
specific to this site.
