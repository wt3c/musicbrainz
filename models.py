# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AlternativeMedium(models.Model):
    medium = models.IntegerField()
    alternative_release = models.IntegerField()
    name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alternative_medium'


class AlternativeMediumTrack(models.Model):
    alternative_medium = models.IntegerField(primary_key=True)
    track = models.IntegerField()
    alternative_track = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alternative_medium_track'
        unique_together = (('alternative_medium', 'track'),)


class AlternativeRelease(models.Model):
    gid = models.UUIDField()
    release = models.IntegerField()
    name = models.CharField(max_length=-1, blank=True, null=True)
    artist_credit = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    language = models.IntegerField()
    script = models.IntegerField()
    comment = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'alternative_release'


class AlternativeReleaseType(models.Model):
    name = models.TextField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'alternative_release_type'


class AlternativeTrack(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    artist_credit = models.IntegerField(blank=True, null=True)
    ref_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alternative_track'


class Annotation(models.Model):
    editor = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    changelog = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'annotation'


class Application(models.Model):
    owner = models.IntegerField()
    name = models.TextField()
    oauth_id = models.TextField()
    oauth_secret = models.TextField()
    oauth_redirect_uri = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application'


class Apps(models.Model):
    c1 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apps'


class Area(models.Model):
    gid = models.UUIDField()
    name = models.CharField(max_length=-1)
    type = models.IntegerField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    begin_date_year = models.SmallIntegerField(blank=True, null=True)
    begin_date_month = models.SmallIntegerField(blank=True, null=True)
    begin_date_day = models.SmallIntegerField(blank=True, null=True)
    end_date_year = models.SmallIntegerField(blank=True, null=True)
    end_date_month = models.SmallIntegerField(blank=True, null=True)
    end_date_day = models.SmallIntegerField(blank=True, null=True)
    ended = models.BooleanField()
    comment = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'area'


class AreaAlias(models.Model):
    area = models.IntegerField()
    name = models.CharField(max_length=-1)
    locale = models.TextField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=-1)
    begin_date_year = models.SmallIntegerField(blank=True, null=True)
    begin_date_month = models.SmallIntegerField(blank=True, null=True)
    begin_date_day = models.SmallIntegerField(blank=True, null=True)
    end_date_year = models.SmallIntegerField(blank=True, null=True)
    end_date_month = models.SmallIntegerField(blank=True, null=True)
    end_date_day = models.SmallIntegerField(blank=True, null=True)
    primary_for_locale = models.BooleanField()
    ended = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'area_alias'


class AreaAliasType(models.Model):
    name = models.TextField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'area_alias_type'


class AreaAnnotation(models.Model):
    area = models.IntegerField(primary_key=True)
    annotation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'area_annotation'
        unique_together = (('area', 'annotation'),)


class AreaAttribute(models.Model):
    area = models.IntegerField()
    area_attribute_type = models.IntegerField()
    area_attribute_type_allowed_value = models.IntegerField(blank=True, null=True)
    area_attribute_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_attribute'


class AreaAttributeType(models.Model):
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    free_text = models.BooleanField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'area_attribute_type'


class AreaAttributeTypeAllowedValue(models.Model):
    area_attribute_type = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'area_attribute_type_allowed_value'


class AreaGidRedirect(models.Model):
    gid = models.UUIDField(primary_key=True)
    new_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_gid_redirect'


class AreaTag(models.Model):
    area = models.IntegerField(primary_key=True)
    tag = models.IntegerField()
    count = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_tag'
        unique_together = (('area', 'tag'),)


class AreaTagRaw(models.Model):
    area = models.IntegerField(primary_key=True)
    editor = models.IntegerField()
    tag = models.IntegerField()
    is_upvote = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'area_tag_raw'
        unique_together = (('area', 'editor', 'tag'),)


class AreaType(models.Model):
    name = models.CharField(max_length=255)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'area_type'


class Artist(models.Model):
    gid = models.UUIDField()
    name = models.CharField(max_length=-1)
    sort_name = models.CharField(max_length=-1)
    begin_date_year = models.SmallIntegerField(blank=True, null=True)
    begin_date_month = models.SmallIntegerField(blank=True, null=True)
    begin_date_day = models.SmallIntegerField(blank=True, null=True)
    end_date_year = models.SmallIntegerField(blank=True, null=True)
    end_date_month = models.SmallIntegerField(blank=True, null=True)
    end_date_day = models.SmallIntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    ended = models.BooleanField()
    begin_area = models.IntegerField(blank=True, null=True)
    end_area = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey('ArtistType', models.DO_NOTHING, db_column='type', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist'


class ArtistAlias(models.Model):
    artist = models.IntegerField()
    name = models.CharField(max_length=-1)
    locale = models.TextField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=-1)
    begin_date_year = models.SmallIntegerField(blank=True, null=True)
    begin_date_month = models.SmallIntegerField(blank=True, null=True)
    begin_date_day = models.SmallIntegerField(blank=True, null=True)
    end_date_year = models.SmallIntegerField(blank=True, null=True)
    end_date_month = models.SmallIntegerField(blank=True, null=True)
    end_date_day = models.SmallIntegerField(blank=True, null=True)
    primary_for_locale = models.BooleanField()
    ended = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'artist_alias'


class ArtistAliasType(models.Model):
    name = models.TextField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'artist_alias_type'


class ArtistAnnotation(models.Model):
    artist = models.IntegerField(primary_key=True)
    annotation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'artist_annotation'
        unique_together = (('artist', 'annotation'),)


class ArtistAttribute(models.Model):
    artist = models.IntegerField()
    artist_attribute_type = models.IntegerField()
    artist_attribute_type_allowed_value = models.IntegerField(blank=True, null=True)
    artist_attribute_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist_attribute'


class ArtistAttributeType(models.Model):
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    free_text = models.BooleanField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'artist_attribute_type'


class ArtistAttributeTypeAllowedValue(models.Model):
    artist_attribute_type = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'artist_attribute_type_allowed_value'


class ArtistCredit(models.Model):
    name = models.CharField(max_length=-1)
    artist_count = models.SmallIntegerField()
    ref_count = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist_credit'


class ArtistCreditName(models.Model):
    artist_credit = models.ForeignKey(ArtistCredit, models.DO_NOTHING)
    position = models.SmallIntegerField()
    artist = models.ForeignKey(Artist, models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    join_phrase = models.TextField()
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist_credit_name'


class ArtistGidRedirect(models.Model):
    gid = models.UUIDField(primary_key=True)
    new_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist_gid_redirect'


class ArtistIpi(models.Model):
    artist = models.IntegerField(primary_key=True)
    ipi = models.CharField(max_length=11)
    edits_pending = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist_ipi'
        unique_together = (('artist', 'ipi'),)


class ArtistIsni(models.Model):
    artist = models.IntegerField(primary_key=True)
    isni = models.CharField(max_length=16)
    edits_pending = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist_isni'
        unique_together = (('artist', 'isni'),)


class ArtistMeta(models.Model):
    id = models.IntegerField(primary_key=True)
    rating = models.SmallIntegerField(blank=True, null=True)
    rating_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist_meta'


class ArtistRatingRaw(models.Model):
    artist = models.IntegerField(primary_key=True)
    editor = models.IntegerField()
    rating = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'artist_rating_raw'
        unique_together = (('artist', 'editor'),)


class ArtistTag(models.Model):
    artist = models.IntegerField(primary_key=True)
    tag = models.IntegerField()
    count = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist_tag'
        unique_together = (('artist', 'tag'),)


class ArtistTagRaw(models.Model):
    artist = models.IntegerField(primary_key=True)
    editor = models.IntegerField()
    tag = models.IntegerField()
    is_upvote = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'artist_tag_raw'
        unique_together = (('artist', 'editor', 'tag'),)


class ArtistType(models.Model):
    name = models.CharField(max_length=255)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'artist_type'


class ArtistWork(models.Model):
    artist = models.ForeignKey(Artist, models.DO_NOTHING)
    work = models.ForeignKey('Work', models.DO_NOTHING)
    category = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'artist_work'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AutoeditorElection(models.Model):
    candidate = models.IntegerField()
    proposer = models.IntegerField()
    seconder_1 = models.IntegerField(blank=True, null=True)
    seconder_2 = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    yes_votes = models.IntegerField()
    no_votes = models.IntegerField()
    propose_time = models.DateTimeField()
    open_time = models.DateTimeField(blank=True, null=True)
    close_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autoeditor_election'


class AutoeditorElectionVote(models.Model):
    autoeditor_election = models.IntegerField()
    voter = models.IntegerField()
    vote = models.IntegerField()
    vote_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'autoeditor_election_vote'


class Cdtoc(models.Model):
    discid = models.CharField(max_length=28)
    freedb_id = models.CharField(max_length=8)
    track_count = models.IntegerField()
    leadout_offset = models.IntegerField()
    track_offset = models.TextField()  # This field type is a guess.
    degraded = models.BooleanField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cdtoc'


class CdtocRaw(models.Model):
    release = models.IntegerField()
    discid = models.CharField(max_length=28)
    track_count = models.IntegerField()
    leadout_offset = models.IntegerField()
    track_offset = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cdtoc_raw'


class CountryArea(models.Model):
    area = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'country_area'


class DeletedEntity(models.Model):
    gid = models.UUIDField(primary_key=True)
    data = models.TextField()  # This field type is a guess.
    deleted_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'deleted_entity'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Edit(models.Model):
    editor = models.IntegerField()
    type = models.SmallIntegerField()
    status = models.SmallIntegerField()
    autoedit = models.SmallIntegerField()
    open_time = models.DateTimeField(blank=True, null=True)
    close_time = models.DateTimeField(blank=True, null=True)
    expire_time = models.DateTimeField()
    language = models.IntegerField(blank=True, null=True)
    quality = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'edit'


class EditArea(models.Model):
    edit = models.IntegerField(primary_key=True)
    area = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'edit_area'
        unique_together = (('edit', 'area'),)


class EditArtist(models.Model):
    edit = models.IntegerField(primary_key=True)
    artist = models.IntegerField()
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'edit_artist'
        unique_together = (('edit', 'artist'),)


class EditData(models.Model):
    edit = models.IntegerField(primary_key=True)
    data = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'edit_data'


class EditEvent(models.Model):
    edit = models.IntegerField(primary_key=True)
    event = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'edit_event'
        unique_together = (('edit', 'event'),)


class EditInstrument(models.Model):
    edit = models.IntegerField(primary_key=True)
    instrument = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'edit_instrument'
        unique_together = (('edit', 'instrument'),)


class EditLabel(models.Model):
    edit = models.IntegerField(primary_key=True)
    label = models.IntegerField()
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'edit_label'
        unique_together = (('edit', 'label'),)


class EditNote(models.Model):
    editor = models.IntegerField()
    edit = models.IntegerField()
    text = models.TextField()
    post_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edit_note'


class EditNoteRecipient(models.Model):
    recipient = models.IntegerField(primary_key=True)
    edit_note = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'edit_note_recipient'
        unique_together = (('recipient', 'edit_note'),)


class EditPlace(models.Model):
    edit = models.IntegerField(primary_key=True)
    place = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'edit_place'
        unique_together = (('edit', 'place'),)


class EditRecording(models.Model):
    edit = models.IntegerField(primary_key=True)
    recording = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'edit_recording'
        unique_together = (('edit', 'recording'),)


class EditRelease(models.Model):
    edit = models.IntegerField(primary_key=True)
    release = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'edit_release'
        unique_together = (('edit', 'release'),)


class EditReleaseGroup(models.Model):
    edit = models.IntegerField(primary_key=True)
    release_group = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'edit_release_group'
        unique_together = (('edit', 'release_group'),)


class EditSeries(models.Model):
    edit = models.IntegerField(primary_key=True)
    series = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'edit_series'
        unique_together = (('edit', 'series'),)


class EditUrl(models.Model):
    edit = models.IntegerField(primary_key=True)
    url = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'edit_url'
        unique_together = (('edit', 'url'),)


class EditWork(models.Model):
    edit = models.IntegerField(primary_key=True)
    work = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'edit_work'
        unique_together = (('edit', 'work'),)


class Editor(models.Model):
    name = models.CharField(max_length=64)
    privs = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    member_since = models.DateTimeField(blank=True, null=True)
    email_confirm_date = models.DateTimeField(blank=True, null=True)
    last_login_date = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=128)
    ha1 = models.CharField(max_length=32)
    deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'editor'


class EditorCollection(models.Model):
    gid = models.UUIDField()
    editor = models.IntegerField()
    name = models.CharField(max_length=-1)
    public = models.BooleanField()
    description = models.TextField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_collection'


class EditorCollectionArea(models.Model):
    collection = models.IntegerField(primary_key=True)
    area = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_collection_area'
        unique_together = (('collection', 'area'),)


class EditorCollectionArtist(models.Model):
    collection = models.IntegerField(primary_key=True)
    artist = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_collection_artist'
        unique_together = (('collection', 'artist'),)


class EditorCollectionDeletedEntity(models.Model):
    collection = models.IntegerField(primary_key=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'editor_collection_deleted_entity'
        unique_together = (('collection', 'gid'),)


class EditorCollectionEvent(models.Model):
    collection = models.IntegerField(primary_key=True)
    event = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_collection_event'
        unique_together = (('collection', 'event'),)


class EditorCollectionInstrument(models.Model):
    collection = models.IntegerField(primary_key=True)
    instrument = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_collection_instrument'
        unique_together = (('collection', 'instrument'),)


class EditorCollectionLabel(models.Model):
    collection = models.IntegerField(primary_key=True)
    label = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_collection_label'
        unique_together = (('collection', 'label'),)


class EditorCollectionPlace(models.Model):
    collection = models.IntegerField(primary_key=True)
    place = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_collection_place'
        unique_together = (('collection', 'place'),)


class EditorCollectionRecording(models.Model):
    collection = models.IntegerField(primary_key=True)
    recording = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_collection_recording'
        unique_together = (('collection', 'recording'),)


class EditorCollectionRelease(models.Model):
    collection = models.IntegerField(primary_key=True)
    release = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_collection_release'
        unique_together = (('collection', 'release'),)


class EditorCollectionReleaseGroup(models.Model):
    collection = models.IntegerField(primary_key=True)
    release_group = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_collection_release_group'
        unique_together = (('collection', 'release_group'),)


class EditorCollectionSeries(models.Model):
    collection = models.IntegerField(primary_key=True)
    series = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_collection_series'
        unique_together = (('collection', 'series'),)


class EditorCollectionType(models.Model):
    name = models.CharField(max_length=255)
    entity_type = models.CharField(max_length=50)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'editor_collection_type'


class EditorCollectionWork(models.Model):
    collection = models.IntegerField(primary_key=True)
    work = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_collection_work'
        unique_together = (('collection', 'work'),)


class EditorLanguage(models.Model):
    editor = models.IntegerField(primary_key=True)
    language = models.IntegerField()
    fluency = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'editor_language'
        unique_together = (('editor', 'language'),)


class EditorOauthToken(models.Model):
    editor = models.IntegerField()
    application = models.IntegerField()
    authorization_code = models.TextField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    access_token = models.TextField(blank=True, null=True)
    expire_time = models.DateTimeField()
    scope = models.IntegerField()
    granted = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'editor_oauth_token'


class EditorPreference(models.Model):
    editor = models.IntegerField()
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'editor_preference'


class EditorSubscribeArtist(models.Model):
    editor = models.IntegerField()
    artist = models.IntegerField()
    last_edit_sent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_subscribe_artist'


class EditorSubscribeArtistDeleted(models.Model):
    editor = models.IntegerField(primary_key=True)
    gid = models.UUIDField()
    deleted_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_subscribe_artist_deleted'
        unique_together = (('editor', 'gid'),)


class EditorSubscribeCollection(models.Model):
    editor = models.IntegerField()
    collection = models.IntegerField()
    last_edit_sent = models.IntegerField()
    available = models.BooleanField()
    last_seen_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'editor_subscribe_collection'


class EditorSubscribeEditor(models.Model):
    editor = models.IntegerField()
    subscribed_editor = models.IntegerField()
    last_edit_sent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_subscribe_editor'


class EditorSubscribeLabel(models.Model):
    editor = models.IntegerField()
    label = models.IntegerField()
    last_edit_sent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_subscribe_label'


class EditorSubscribeLabelDeleted(models.Model):
    editor = models.IntegerField(primary_key=True)
    gid = models.UUIDField()
    deleted_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_subscribe_label_deleted'
        unique_together = (('editor', 'gid'),)


class EditorSubscribeSeries(models.Model):
    editor = models.IntegerField()
    series = models.IntegerField()
    last_edit_sent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_subscribe_series'


class EditorSubscribeSeriesDeleted(models.Model):
    editor = models.IntegerField(primary_key=True)
    gid = models.UUIDField()
    deleted_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_subscribe_series_deleted'
        unique_together = (('editor', 'gid'),)


class EditorWatchArtist(models.Model):
    artist = models.IntegerField(primary_key=True)
    editor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_watch_artist'
        unique_together = (('artist', 'editor'),)


class EditorWatchPreferences(models.Model):
    editor = models.IntegerField(primary_key=True)
    notify_via_email = models.BooleanField()
    notification_timeframe = models.TextField()  # This field type is a guess.
    last_checked = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'editor_watch_preferences'


class EditorWatchReleaseGroupType(models.Model):
    editor = models.IntegerField(primary_key=True)
    release_group_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_watch_release_group_type'
        unique_together = (('editor', 'release_group_type'),)


class EditorWatchReleaseStatus(models.Model):
    editor = models.IntegerField(primary_key=True)
    release_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'editor_watch_release_status'
        unique_together = (('editor', 'release_status'),)


class Event(models.Model):
    gid = models.UUIDField()
    name = models.CharField(max_length=-1)
    begin_date_year = models.SmallIntegerField(blank=True, null=True)
    begin_date_month = models.SmallIntegerField(blank=True, null=True)
    begin_date_day = models.SmallIntegerField(blank=True, null=True)
    end_date_year = models.SmallIntegerField(blank=True, null=True)
    end_date_month = models.SmallIntegerField(blank=True, null=True)
    end_date_day = models.SmallIntegerField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    cancelled = models.BooleanField()
    setlist = models.TextField(blank=True, null=True)
    comment = models.CharField(max_length=255)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    ended = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'event'


class EventAlias(models.Model):
    event = models.IntegerField()
    name = models.CharField(max_length=-1)
    locale = models.TextField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=-1)
    begin_date_year = models.SmallIntegerField(blank=True, null=True)
    begin_date_month = models.SmallIntegerField(blank=True, null=True)
    begin_date_day = models.SmallIntegerField(blank=True, null=True)
    end_date_year = models.SmallIntegerField(blank=True, null=True)
    end_date_month = models.SmallIntegerField(blank=True, null=True)
    end_date_day = models.SmallIntegerField(blank=True, null=True)
    primary_for_locale = models.BooleanField()
    ended = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'event_alias'


class EventAliasType(models.Model):
    name = models.TextField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'event_alias_type'


class EventAnnotation(models.Model):
    event = models.IntegerField(primary_key=True)
    annotation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_annotation'
        unique_together = (('event', 'annotation'),)


class EventAttribute(models.Model):
    event = models.IntegerField()
    event_attribute_type = models.IntegerField()
    event_attribute_type_allowed_value = models.IntegerField(blank=True, null=True)
    event_attribute_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_attribute'


class EventAttributeType(models.Model):
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    free_text = models.BooleanField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'event_attribute_type'


class EventAttributeTypeAllowedValue(models.Model):
    event_attribute_type = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'event_attribute_type_allowed_value'


class EventGidRedirect(models.Model):
    gid = models.UUIDField(primary_key=True)
    new_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_gid_redirect'


class EventMeta(models.Model):
    id = models.IntegerField(primary_key=True)
    rating = models.SmallIntegerField(blank=True, null=True)
    rating_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_meta'


class EventRatingRaw(models.Model):
    event = models.IntegerField(primary_key=True)
    editor = models.IntegerField()
    rating = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'event_rating_raw'
        unique_together = (('event', 'editor'),)


class EventTag(models.Model):
    event = models.IntegerField(primary_key=True)
    tag = models.IntegerField()
    count = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_tag'
        unique_together = (('event', 'tag'),)


class EventTagRaw(models.Model):
    event = models.IntegerField(primary_key=True)
    editor = models.IntegerField()
    tag = models.IntegerField()
    is_upvote = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'event_tag_raw'
        unique_together = (('event', 'editor', 'tag'),)


class EventType(models.Model):
    name = models.CharField(max_length=255)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'event_type'


class Gender(models.Model):
    name = models.CharField(max_length=255)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'gender'


class Instrument(models.Model):
    gid = models.UUIDField()
    name = models.CharField(max_length=-1)
    type = models.IntegerField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'instrument'


class InstrumentAlias(models.Model):
    instrument = models.IntegerField()
    name = models.CharField(max_length=-1)
    locale = models.TextField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=-1)
    begin_date_year = models.SmallIntegerField(blank=True, null=True)
    begin_date_month = models.SmallIntegerField(blank=True, null=True)
    begin_date_day = models.SmallIntegerField(blank=True, null=True)
    end_date_year = models.SmallIntegerField(blank=True, null=True)
    end_date_month = models.SmallIntegerField(blank=True, null=True)
    end_date_day = models.SmallIntegerField(blank=True, null=True)
    primary_for_locale = models.BooleanField()
    ended = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'instrument_alias'


class InstrumentAliasType(models.Model):
    name = models.TextField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'instrument_alias_type'


class InstrumentAnnotation(models.Model):
    instrument = models.IntegerField(primary_key=True)
    annotation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'instrument_annotation'
        unique_together = (('instrument', 'annotation'),)


class InstrumentAttribute(models.Model):
    instrument = models.IntegerField()
    instrument_attribute_type = models.IntegerField()
    instrument_attribute_type_allowed_value = models.IntegerField(blank=True, null=True)
    instrument_attribute_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instrument_attribute'


class InstrumentAttributeType(models.Model):
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    free_text = models.BooleanField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'instrument_attribute_type'


class InstrumentAttributeTypeAllowedValue(models.Model):
    instrument_attribute_type = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'instrument_attribute_type_allowed_value'


class InstrumentGidRedirect(models.Model):
    gid = models.UUIDField(primary_key=True)
    new_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instrument_gid_redirect'


class InstrumentTag(models.Model):
    instrument = models.IntegerField(primary_key=True)
    tag = models.IntegerField()
    count = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instrument_tag'
        unique_together = (('instrument', 'tag'),)


class InstrumentTagRaw(models.Model):
    instrument = models.IntegerField(primary_key=True)
    editor = models.IntegerField()
    tag = models.IntegerField()
    is_upvote = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'instrument_tag_raw'
        unique_together = (('instrument', 'editor', 'tag'),)


class InstrumentType(models.Model):
    name = models.CharField(max_length=255)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'instrument_type'


class Iso31661(models.Model):
    area = models.IntegerField()
    code = models.CharField(primary_key=True, max_length=2)

    class Meta:
        managed = False
        db_table = 'iso_3166_1'


class Iso31662(models.Model):
    area = models.IntegerField()
    code = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'iso_3166_2'


class Iso31663(models.Model):
    area = models.IntegerField()
    code = models.CharField(primary_key=True, max_length=4)

    class Meta:
        managed = False
        db_table = 'iso_3166_3'


class Isrc(models.Model):
    recording = models.IntegerField()
    isrc = models.CharField(max_length=12)
    source = models.SmallIntegerField(blank=True, null=True)
    edits_pending = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'isrc'


class Iswc(models.Model):
    work = models.IntegerField()
    iswc = models.CharField(max_length=15, blank=True, null=True)
    source = models.SmallIntegerField(blank=True, null=True)
    edits_pending = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'iswc'


class LAreaArea(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_area_area'


class LAreaArtist(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_area_artist'


class LAreaEvent(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_area_event'


class LAreaInstrument(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_area_instrument'


class LAreaLabel(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_area_label'


class LAreaPlace(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_area_place'


class LAreaRecording(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_area_recording'


class LAreaRelease(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_area_release'


class LAreaReleaseGroup(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_area_release_group'


class LAreaSeries(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_area_series'


class LAreaUrl(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_area_url'


class LAreaWork(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_area_work'


class LArtistArtist(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_artist_artist'


class LArtistEvent(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_artist_event'


class LArtistInstrument(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_artist_instrument'


class LArtistLabel(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_artist_label'


class LArtistPlace(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_artist_place'


class LArtistRecording(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_artist_recording'


class LArtistRelease(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_artist_release'


class LArtistReleaseGroup(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_artist_release_group'


class LArtistSeries(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_artist_series'


class LArtistUrl(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_artist_url'


class LArtistWork(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_artist_work'


class LEventEvent(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_event_event'


class LEventInstrument(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_event_instrument'


class LEventLabel(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_event_label'


class LEventPlace(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_event_place'


class LEventRecording(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_event_recording'


class LEventRelease(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_event_release'


class LEventReleaseGroup(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_event_release_group'


class LEventSeries(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_event_series'


class LEventUrl(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_event_url'


class LEventWork(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_event_work'


class LInstrumentInstrument(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_instrument_instrument'


class LInstrumentLabel(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_instrument_label'


class LInstrumentPlace(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_instrument_place'


class LInstrumentRecording(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_instrument_recording'


class LInstrumentRelease(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_instrument_release'


class LInstrumentReleaseGroup(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_instrument_release_group'


class LInstrumentSeries(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_instrument_series'


class LInstrumentUrl(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_instrument_url'


class LInstrumentWork(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_instrument_work'


class LLabelLabel(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_label_label'


class LLabelPlace(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    link_order = models.IntegerField()
    entity0_credit = models.TextField()
    entity1_credit = models.TextField()

    class Meta:
        managed = False
        db_table = 'l_label_place'
