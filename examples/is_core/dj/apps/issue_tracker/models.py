from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


@python_2_unicode_compatible
class Project(models.Model):

    title = models.CharField(verbose_name=_('Title'), max_length=100, null=False, blank=False)
    leader = models.OneToOneField(AUTH_USER_MODEL, verbose_name=_('Leader'), null=False, blank=False,
                                  related_name='leading_project')

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Issue(models.Model):

    project = models.ForeignKey(Project, verbose_name=_('project'), null=False, blank=False,
                                related_name='issues')
    title = models.CharField(verbose_name=_('Title'), max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    watchers = models.ManyToManyField(AUTH_USER_MODEL, verbose_name=_('Watched by'), blank=True,
                                      related_name='watched_issues')
    reporter = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_('Created by'), null=False, blank=False,
                                 related_name='reported_issues')
    assignee = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_('Solver'), null=True, blank=True,
                                 related_name='assigned_issues')

    def __str__(self):
        return 'issue: {}'.format(self.name)
