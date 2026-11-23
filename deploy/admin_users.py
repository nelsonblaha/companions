"""OpenCompanions' private chat roster alongside the campaign's signup list."""
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from campaignlanding.admin import shell
from flask import Response, abort, redirect, render_template, url_for
from jinja2 import ChoiceLoader, FileSystemLoader


def register(app, data):
    app.jinja_loader = ChoiceLoader([FileSystemLoader(Path(__file__).with_name("templates")), app.jinja_loader])
    runtime = app.config["campaign"]
    mailing = app.view_functions["admin"]
    remove_signup = app.view_functions["admin_delete"]

    def navigation(active):
        return render_template("admin_nav.html", active=active)

    def users():
        if not runtime.admin_enabled():
            abort(404)
        if not runtime.is_admin():
            return redirect("/login", code=303)
        try:
            snap = json.loads((data / "chat-users.json").read_text())
            if snap["schema"] != 1:
                raise ValueError("Unknown report format")
            updated = datetime.fromisoformat(snap["updated"])
            stale = datetime.now(timezone.utc) - updated > timedelta(minutes=10)
        except (OSError, ValueError, KeyError, TypeError):
            snap, stale = None, True
        inner = navigation("users") + render_template("admin_users.html", snapshot=snap, stale=stale)
        return Response(shell("Users", runtime.config.name, inner), mimetype="text/html",
                        headers={"Cache-Control":"no-store", "X-Robots-Tag":"noindex, nofollow"})

    # Keep the upstream route's authentication, moderation form, fields and watermark.
    # Only entering the Mailing list tab should advance the watermark.
    @app.get("/admin/mailing-list")
    def mailing_list():
        response = mailing()
        if response.status_code == 200:
            html = response.get_data(as_text=True)
            response.set_data(html.replace("<body><main>", "<body><main>" + navigation("mailing"), 1))
        return response

    def delete_from_list():
        response = remove_signup()
        if response.status_code == 303 and response.location == "/admin":
            response.location = url_for("mailing_list")
        return response

    app.view_functions["admin"] = users
    app.view_functions["admin_delete"] = delete_from_list
