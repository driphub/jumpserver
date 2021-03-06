# -*- coding: utf-8 -*-
#

ASSETS_CACHE_KEY = "terminal__session__assets"
USERS_CACHE_KEY = "terminal__session__users"
SYSTEM_USER_CACHE_KEY = "terminal__session__system_users"


# Replay Storage

REPLAY_STORAGE_TYPE_NULL = 'null'
REPLAY_STORAGE_TYPE_SERVER = 'server'
REPLAY_STORAGE_TYPE_S3 = 's3'
REPLAY_STORAGE_TYPE_CEPH = 'ceph'
REPLAY_STORAGE_TYPE_SWIFT = 'swift'
REPLAY_STORAGE_TYPE_OSS = 'oss'
REPLAY_STORAGE_TYPE_AZURE = 'azure'

REPLAY_STORAGE_TYPE_EMPTY_FIELDS = []
REPLAY_STORAGE_TYPE_S3_FIELDS = [
    {'name': 'BUCKET'},
    {'name': 'ACCESS_KEY', 'write_only': True},
    {'name': 'SECRET_KEY', 'write_only': True},
    {'name': 'ENDPOINT'}
]
REPLAY_STORAGE_TYPE_CEPH_FIELDS = [
    {'name': 'BUCKET'},
    {'name': 'ACCESS_KEY', 'write_only': True},
    {'name': 'SECRET_KEY', 'write_only': True},
    {'name': 'ENDPOINT'}
]
REPLAY_STORAGE_TYPE_SWIFT_FIELDS = [
    {'name': 'BUCKET'},
    {'name': 'ACCESS_KEY', 'write_only': True},
    {'name': 'SECRET_KEY', 'write_only': True},
    {'name': 'REGION'},
    {'name': 'ENDPOINT'},
    {'name': 'PROTOCOL'},
]
REPLAY_STORAGE_TYPE_OSS_FIELDS = [
    {'name': 'BUCKET'},
    {'name': 'ACCESS_KEY', 'write_only': True},
    {'name': 'SECRET_KEY', 'write_only': True},
    {'name': 'ENDPOINT'}
]
REPLAY_STORAGE_TYPE_AZURE_FIELDS = [
    {'name': 'CONTAINER_NAME'},
    {'name': 'ACCOUNT_NAME'},
    {'name': 'ACCOUNT_KEY', 'write_only': True},
    {'name': 'ENDPOINT_SUFFIX'}
]

REPLAY_STORAGE_TYPE_FIELDS_MAP = {
    REPLAY_STORAGE_TYPE_NULL: REPLAY_STORAGE_TYPE_EMPTY_FIELDS,
    REPLAY_STORAGE_TYPE_SERVER: REPLAY_STORAGE_TYPE_EMPTY_FIELDS,
    REPLAY_STORAGE_TYPE_S3: REPLAY_STORAGE_TYPE_S3_FIELDS,
    REPLAY_STORAGE_TYPE_CEPH: REPLAY_STORAGE_TYPE_CEPH_FIELDS,
    REPLAY_STORAGE_TYPE_SWIFT: REPLAY_STORAGE_TYPE_SWIFT_FIELDS,
    REPLAY_STORAGE_TYPE_OSS: REPLAY_STORAGE_TYPE_OSS_FIELDS,
    REPLAY_STORAGE_TYPE_AZURE: REPLAY_STORAGE_TYPE_AZURE_FIELDS
}

REPLAY_STORAGE_TYPE_CHOICES_DEFAULT = [
    (REPLAY_STORAGE_TYPE_NULL, 'Null'),
    (REPLAY_STORAGE_TYPE_SERVER, 'Server'),
]

REPLAY_STORAGE_TYPE_CHOICES_EXTENDS = [
    (REPLAY_STORAGE_TYPE_S3, 'S3'),
    (REPLAY_STORAGE_TYPE_CEPH, 'Ceph'),
    (REPLAY_STORAGE_TYPE_SWIFT, 'Swift'),
    (REPLAY_STORAGE_TYPE_OSS, 'OSS'),
    (REPLAY_STORAGE_TYPE_AZURE, 'Azure')
]

REPLAY_STORAGE_TYPE_CHOICES = REPLAY_STORAGE_TYPE_CHOICES_DEFAULT + \
                              REPLAY_STORAGE_TYPE_CHOICES_EXTENDS


# Command Storage

COMMAND_STORAGE_TYPE_NULL = 'null'
COMMAND_STORAGE_TYPE_SERVER = 'server'
COMMAND_STORAGE_TYPE_ES = 'es'

COMMAND_STORAGE_TYPE_EMPTY_FIELDS = []
COMMAND_STORAGE_TYPE_ES_FIELDS = [
    {'name': 'HOSTS'},
    {'name': 'INDEX'},
    {'name': 'DOC_TYPE'}
]

COMMAND_STORAGE_TYPE_FIELDS_MAP = {
    COMMAND_STORAGE_TYPE_NULL: COMMAND_STORAGE_TYPE_EMPTY_FIELDS,
    COMMAND_STORAGE_TYPE_SERVER: COMMAND_STORAGE_TYPE_EMPTY_FIELDS,
    COMMAND_STORAGE_TYPE_ES: COMMAND_STORAGE_TYPE_ES_FIELDS,
}

COMMAND_STORAGE_TYPE_CHOICES_DEFAULT = [
    (COMMAND_STORAGE_TYPE_NULL, 'Null'),
    (COMMAND_STORAGE_TYPE_SERVER, 'Server'),
]

COMMAND_STORAGE_TYPE_CHOICES_EXTENDS = [
    (COMMAND_STORAGE_TYPE_ES, 'Elasticsearch')
]

COMMAND_STORAGE_TYPE_CHOICES = COMMAND_STORAGE_TYPE_CHOICES_DEFAULT + \
                               COMMAND_STORAGE_TYPE_CHOICES_EXTENDS


from django.db.models import TextChoices
from django.utils.translation import ugettext_lazy as _


class ComponentStatusChoices(TextChoices):
    critical = 'critical', _('Critical')
    high = 'high', _('High')
    normal = 'normal', _('Normal')

    @classmethod
    def status(cls):
        return set(dict(cls.choices).keys())


class TerminalTypeChoices(TextChoices):
    koko = 'koko', 'KoKo'
    guacamole = 'guacamole', 'Guacamole'
    omnidb = 'omnidb', 'OmniDB'

    @classmethod
    def types(cls):
        return set(dict(cls.choices).keys())

