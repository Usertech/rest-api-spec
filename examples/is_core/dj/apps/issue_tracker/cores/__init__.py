from django.contrib.auth.models import User

from is_core.main import UIRESTModelISCore

from issue_tracker.models import Issue, Project

from .resources import NumberOfUserIssuesResource


class UserIsCore(UIRESTModelISCore):
    model = User


class IssueIsCore(UIRESTModelISCore):
    model = Issue


class ProjectIsCore(UIRESTModelISCore):
    model = Project
