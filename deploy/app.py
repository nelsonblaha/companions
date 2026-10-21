"""Companions: the site and its signup list.

The machinery is campaignlanding, https://github.com/nelsonblaha/campaignlanding,
the same package chucodata.org runs on. What is in this file is only what is
about this campaign. If something here starts looking like machinery, it belongs
upstream instead, where every campaign gets it.

Signups land in $COMPANIONS_DATA/signups.jsonl on the host and are read over SSH.
There is no admin view until COMPANIONS_SECRET_KEY and a password hash are both
configured; until then /login and /admin 404 and the page carries no admin markup.
"""

import os
from pathlib import Path

from campaignlanding import Config, Language, Repeat, create_app

SITE_DIR = Path(os.environ.get("COMPANIONS_SITE", "/app/site"))
DATA_DIR = Path(os.environ.get("COMPANIONS_DATA", "/data"))

app = create_app(
    Config(
        name="Companions",
        site_dir=SITE_DIR,
        data_dir=DATA_DIR,
        # English only for now. A second language is a second page and one more
        # entry here; see how chucodata.org does Spanish.
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
        ],
        canonical_host="companions.blaha.io",
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
        sections={
            "why": "why",
            "the-proposal": "proposal",
            "roadmap": "roadmap",
            "how-to-help": "help",
        },
        # The four reasons are tabs inside the "why" section, keyed by element id.
        tabs={
            "portability": "tab-port",
            "purchases": "tab-buy",
            "changes": "tab-change",
            "privacy": "tab-privacy",
        },
        tabs_section="why",
        # Below this the invitation is not shown at all: "join 2 others" tells a
        # reader the list is nearly empty at the moment they are deciding.
        show_count_above=16,
        # COMPANIONS_SECRET_KEY, COMPANIONS_ADMIN_HASH_FILE.
        env_prefix="COMPANIONS",
    )
)
