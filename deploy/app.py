"""Companions: the site and its signup list.

The machinery is campaignlanding, https://github.com/nelsonblaha/campaignlanding,
the same package chucodata.org runs on. What is in this file is only what is
about this campaign. If something here starts looking like machinery, it belongs
upstream instead, where every campaign gets it.

Signups land in $COMPANIONS_DATA/signups.jsonl on the host and are read over SSH.
There is no admin view until COMPANIONS_SECRET_KEY and a password hash are both
configured; until then /login and /admin 404 and the page carries no admin markup.
"""

import json
import os
from pathlib import Path

from campaignlanding import Config, Language, Repeat, create_app

SITE_DIR = Path(os.environ.get("COMPANIONS_SITE", "/app/site"))
DATA_DIR = Path(os.environ.get("COMPANIONS_DATA", "/data"))
STRINGS_DIR = Path(__file__).resolve().parent / "strings"


def translated(code: str, prefix: str, thanks: str, **extra) -> Language:
    """A language whose words live in strings/<prefix>.json, so a native speaker
    correcting them edits one file beside its review notes, not this one."""
    doc = json.loads((STRINGS_DIR / f"{prefix}.json").read_text(encoding="utf-8"))
    return Language(
        code=code,
        page=f"{prefix}/index.html",
        prefix=prefix,
        thanks_path=f"/{prefix}/{thanks}",
        strings=doc["strings"],
        join_words=doc["join_words"],
        **extra,
    )

app = create_app(
    Config(
        name="Companions",
        site_dir=SITE_DIR,
        data_dir=DATA_DIR,
        # English at "/", which negotiates, and at "/en/", which does not. The
        # others are machine-assisted drafts awaiting native review; each page
        # says so in its footer.
        languages=[
            Language(
                code="en",
                page="index.html",
                strings={
                    "thanks_body": (
                        "That's the whole thing. We'll email when there's something "
                        "real to report: a board, a decision, a service you can "
                        "actually use."
                    ),
                    "back": "Back to the proposal",
                },
            ),
            translated("es", "es", "gracias"),
            translated("pt", "pt", "obrigado"),
            translated("id", "id", "terima-kasih"),
            translated("ja", "ja", "thanks"),
            # Traditional Chinese, coded by script. Browsers ask by region, so
            # name the ones that read Traditional characters.
            translated("zh-Hant", "zh", "thanks", accepts=("zh-TW", "zh-HK", "zh-MO")),
        ],
        canonical_host="opencompanions.org",
        legacy_hosts=frozenset({"www.opencompanions.org", "companions.blaha.io"}),
        # On only once https://opencompanions.org/ answers: a 301 is cached hard.
        redirect_legacy_hosts=False,
        help_choices=frozenset(
            {"updates", "story", "board", "legal", "technical", "spread"}
        ),
        # A row per companion, each with what they might be willing to do. The
        # data-max on the form's group matches max_rows.
        repeats={
            "companions": Repeat(
                label="Companions",
                choices=frozenset({"advisory", "story", "speak", "early"}),
                max_rows=10,
            ),
        },
        # The rail's labels, hyphen-spaced, so /roadmap is something a reader can
        # share and it opens at that section.
        # Japanese and Chinese use the English slugs.
        sections={
            "why": "why",
            "the-proposal": "proposal",
            "roadmap": "roadmap",
            "how-to-help": "help",
            # es
            "por-que": "why",
            "la-propuesta": "proposal",
            "hoja-de-ruta": "roadmap",
            "como-ayudar": "help",
            # pt (por-que is shared with es)
            "a-proposta": "proposal",
            "roteiro": "roadmap",
            "como-ajudar": "help",
            # id
            "mengapa": "why",
            "usulan": "proposal",
            "peta-jalan": "roadmap",
            "cara-membantu": "help",
        },
        # The four reasons are tabs inside the "why" section, keyed by element id.
        tabs={
            "portability": "tab-port",
            "purchases": "tab-buy",
            "changes": "tab-change",
            "privacy": "tab-privacy",
            # es
            "portabilidad": "tab-port",
            "compras": "tab-buy",
            "cambios": "tab-change",
            "privacidad": "tab-privacy",
            # pt (compras is shared with es)
            "portabilidade": "tab-port",
            "mudancas": "tab-change",
            "privacidade": "tab-privacy",
            # id
            "portabilitas": "tab-port",
            "pembelian": "tab-buy",
            "perubahan": "tab-change",
            "privasi": "tab-privacy",
        },
        tabs_section="why",
        # Below this the invitation is not shown at all: "join 2 others" tells a
        # reader the list is nearly empty at the moment they are deciding.
        show_count_above=16,
        # COMPANIONS_SECRET_KEY, COMPANIONS_ADMIN_HASH_FILE.
        env_prefix="COMPANIONS",
    )
)
