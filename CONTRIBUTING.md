# Suggesting a change

Thank you. Almost every useful change to this page is a change to its words, and
those are all in one file, `site/index.html`.

## Without installing anything

1. Open [`site/index.html`](site/index.html) on GitHub and click the pencil icon.
2. Make your change. The page is plain HTML: the words are between the tags, and
   you can leave the tags alone.
3. At the bottom, describe what you changed and why, then choose **Propose
   changes**. GitHub makes a copy for you and opens a pull request.

If you'd rather describe the problem than fix it, open an
[issue](https://github.com/nelsonblaha/companions/issues) instead. That's just as
helpful.

## Translations

The page is in English, Spanish, Brazilian Portuguese, Indonesian, Japanese and
Traditional Chinese. **Every translation is a machine-assisted draft that no
native speaker has reviewed yet**, and each page says so in its footer. If you
speak one of them, you're the person this repository most needs:

- The page itself is `site/<language>/index.html` (`es`, `pt`, `id`, `ja`, `zh`).
  Change the words; leave the tags and attributes alone.
- The form's messages and button labels are in `deploy/strings/<language>.json`.
  Its `review_notes` lists the choices the draft was least sure of.
- Maria's card (`site/img/card-<language>.svg`) shows her own words, translated.
  The field names on it (`name`, `personality` and so on) stay in English: they're
  the open format's own names.
- When a translation has been read through by a native speaker, say so in your
  pull request, and the "draft" line can come out of that page's footer.

## Previewing on your own computer

You need Python 3.11 or newer.

```sh
git clone https://github.com/nelsonblaha/companions
cd companions
python3 -m venv .venv && . .venv/bin/activate
pip install -r deploy/requirements.txt
COMPANIONS_SITE="$PWD/site" COMPANIONS_DATA=/tmp/companions-data \
  flask --app deploy/app run --port 8100
```

`COMPANIONS_SITE` has to be an absolute path, which is what `$PWD` is for: given a
relative one, the page loads but its pictures and stylesheet don't.

Then open <http://127.0.0.1:8100/>. Edit `site/index.html`, reload, and you see
the change. A signup submitted locally goes to `/tmp/companions-data`, not to the
real list.

## The rules for what goes on the page

- **Every factual claim has a source.** Add a numbered reference in the footer and
  link to it with a `<sup class="ref">` like the others. If a claim can't be
  sourced, it doesn't go on the page.
- **Say how good the source is.** Company statements, regulators and news wires are
  strong. Third-party blogs and forum posts are weaker, so the page says so.
- **Be fair to the companies.** When the page criticises one, it also says what
  they would say in their own defence. Removing that to make the argument stronger
  would make us the thing we're criticising.
- **Proposed is not real.** Nothing on the page may suggest that an organization,
  board, service or price exists before it does. The "Honestly" section is
  load-bearing: update it the moment any line in it stops being true.
- **No one's name without their say-so.** Don't add a person's name, username or
  story to the page unless they've agreed to it.
- **No trackers, no third-party scripts.** The page promises that, so a change
  that adds one will not be merged.
- **No donation requests** until there is an organization to donate to.

## How the page works

The section rail, tabs, signup modal and styles come from
[campaignlanding](https://github.com/nelsonblaha/campaignlanding), which also runs
[chucodata.org](https://chucodata.org/). Its
[markup contract](https://github.com/nelsonblaha/campaignlanding/blob/main/docs/markup-contract.md)
lists the handful of attributes the page has to keep, such as `data-section` on
each section and the hidden fields in the form. If you change the structure
rather than the words, check it against that list. A fix that would help any
campaign page is welcome there as well.
