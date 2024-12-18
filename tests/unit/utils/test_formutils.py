"""
DataTables sqlite tests.
"""

from lute.db import db
from lute.utils.formutils import language_choices, valid_current_language_id
from lute.models.repositories import UserSettingRepository


def test_language_choices(app_context):
    "Gets all languages."
    choices = language_choices(db.session)
    assert choices[0][1] == "-", "- at the top"
    langnames = [c[1] for c in choices]
    assert "Spanish" in langnames, "have Spanish"


def test_valid_current_language_id(app_context):
    "Sanity check only."
    repo = UserSettingRepository(db.session)
    repo.set_value("current_language_id", 9999)
    assert int(repo.get_value("current_language_id")) == 9999, "pre-check"
    curr_lang_id = int(valid_current_language_id(db.session))
    assert curr_lang_id == 0, "set back to 0"
    assert int(repo.get_value("current_language_id")) == 0, "re-set to 0"
