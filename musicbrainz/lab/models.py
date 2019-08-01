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
    name = models.CharField(max_length=200, blank=True, null=True)

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
    name = models.CharField(max_length=200, blank=True, null=True)
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
    name = models.CharField(max_length=200, blank=True, null=True)
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


class Area(models.Model):
    gid = models.UUIDField()
    name = models.CharField(max_length=200)
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
        # managed = False
        db_table = 'area'

    def __str__(self):
        return self.name


class AreaAlias(models.Model):
    area = models.IntegerField()
    name = models.CharField(max_length=200)
    locale = models.TextField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=200)
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
    id = models.IntegerField(primary_key=True)
    gid = models.UUIDField()
    name = models.CharField(max_length=200)
    sort_name = models.CharField(max_length=200)
    begin_date_year = models.SmallIntegerField(blank=True, null=True)
    begin_date_month = models.SmallIntegerField(blank=True, null=True)
    begin_date_day = models.SmallIntegerField(blank=True, null=True)
    end_date_year = models.SmallIntegerField(blank=True, null=True)
    end_date_month = models.SmallIntegerField(blank=True, null=True)
    end_date_day = models.SmallIntegerField(blank=True, null=True)
    # type = models.IntegerField(blank=True, null=True)
    type2 = models.ForeignKey('ArtistType', to_field='id', db_column='type', on_delete=models.CASCADE,
                             blank=True,
                             null=True)
    # area = models.IntegerField(blank=True, null=True)
    area = models.ForeignKey('Area', to_field='id', db_column='area', on_delete=models.CASCADE, )
    # gender = models.IntegerField(blank=True, null=True)
    gender = models.ForeignKey('Gender', to_field='id', db_column='gender', on_delete=models.CASCADE,
                               blank=True,
                               null=True)
    comment = models.CharField(max_length=255)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    ended = models.BooleanField()
    begin_area = models.IntegerField(blank=True, null=True)
    end_area = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        # managed = False
        db_table = 'artist'


class ArtistAlias(models.Model):
    artist = models.IntegerField()
    name = models.CharField(max_length=200)
    locale = models.TextField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=200)
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
        # managed = False
        db_table = 'artist_attribute_type_allowed_value'


class ArtistCredit(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    artist_count = models.SmallIntegerField()
    ref_count = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    artist = models.ManyToManyField(Artist, through='ArtistCreditName')

    def __str__(self):
        return self.name

    class Meta:
        # managed = True
        db_table = 'artist_credit'


class ArtistCreditName(models.Model):
    # artist_credit = models.IntegerField(primary_key=True)
    artist_credit = models.ForeignKey(ArtistCredit, on_delete=models.CASCADE)
    position = models.SmallIntegerField()
    # artist = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    join_phrase = models.TextField()

    class Meta:
        # managed = True
        db_table = 'artist_credit_name'
        unique_together = (('artist_credit', 'position', 'artist'),)


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
        # managed = False
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
        # managed = False
        db_table = 'artist_type'

    def __str__(self):
        return self.name


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
    name = models.CharField(max_length=200)
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
    name = models.CharField(max_length=200)
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
    name = models.CharField(max_length=200)
    locale = models.TextField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=200)
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
        # managed = False
        db_table = 'gender'

    def __str__(self):
        return self.name

class Instrument(models.Model):
    gid = models.UUIDField()
    name = models.CharField(max_length=200)
    type = models.IntegerField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'instrument'

    def __str__(self):
        return self.name


class InstrumentAlias(models.Model):
    instrument = models.IntegerField()
    name = models.CharField(max_length=200)
    locale = models.TextField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=200)
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


class LLabelRecording(models.Model):
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
        db_table = 'l_label_recording'


class LLabelRelease(models.Model):
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
        db_table = 'l_label_release'


class LLabelReleaseGroup(models.Model):
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
        db_table = 'l_label_release_group'


class LLabelSeries(models.Model):
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
        db_table = 'l_label_series'


class LLabelUrl(models.Model):
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
        db_table = 'l_label_url'


class LLabelWork(models.Model):
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
        db_table = 'l_label_work'


class LPlacePlace(models.Model):
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
        db_table = 'l_place_place'


class LPlaceRecording(models.Model):
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
        db_table = 'l_place_recording'


class LPlaceRelease(models.Model):
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
        db_table = 'l_place_release'


class LPlaceReleaseGroup(models.Model):
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
        db_table = 'l_place_release_group'


class LPlaceSeries(models.Model):
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
        db_table = 'l_place_series'


class LPlaceUrl(models.Model):
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
        db_table = 'l_place_url'


class LPlaceWork(models.Model):
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
        db_table = 'l_place_work'


class LRecordingRecording(models.Model):
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
        db_table = 'l_recording_recording'


class LRecordingRelease(models.Model):
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
        db_table = 'l_recording_release'


class LRecordingReleaseGroup(models.Model):
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
        db_table = 'l_recording_release_group'


class LRecordingSeries(models.Model):
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
        db_table = 'l_recording_series'


class LRecordingUrl(models.Model):
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
        db_table = 'l_recording_url'


class LRecordingWork(models.Model):
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
        db_table = 'l_recording_work'


class LReleaseGroupReleaseGroup(models.Model):
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
        db_table = 'l_release_group_release_group'


class LReleaseGroupSeries(models.Model):
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
        db_table = 'l_release_group_series'


class LReleaseGroupUrl(models.Model):
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
        db_table = 'l_release_group_url'


class LReleaseGroupWork(models.Model):
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
        db_table = 'l_release_group_work'


class LReleaseRelease(models.Model):
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
        db_table = 'l_release_release'


class LReleaseReleaseGroup(models.Model):
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
        db_table = 'l_release_release_group'


class LReleaseSeries(models.Model):
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
        db_table = 'l_release_series'


class LReleaseUrl(models.Model):
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
        db_table = 'l_release_url'


class LReleaseWork(models.Model):
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
        db_table = 'l_release_work'


class LSeriesSeries(models.Model):
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
        db_table = 'l_series_series'


class LSeriesUrl(models.Model):
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
        db_table = 'l_series_url'


class LSeriesWork(models.Model):
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
        db_table = 'l_series_work'


class LUrlUrl(models.Model):
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
        db_table = 'l_url_url'


class LUrlWork(models.Model):
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
        db_table = 'l_url_work'


class LWorkWork(models.Model):
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
        db_table = 'l_work_work'


class Label(models.Model):
    gid = models.UUIDField()
    name = models.CharField(max_length=200)
    begin_date_year = models.SmallIntegerField(blank=True, null=True)
    begin_date_month = models.SmallIntegerField(blank=True, null=True)
    begin_date_day = models.SmallIntegerField(blank=True, null=True)
    end_date_year = models.SmallIntegerField(blank=True, null=True)
    end_date_month = models.SmallIntegerField(blank=True, null=True)
    end_date_day = models.SmallIntegerField(blank=True, null=True)
    label_code = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    ended = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'label'


class LabelAlias(models.Model):
    label = models.IntegerField()
    name = models.CharField(max_length=200)
    locale = models.TextField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=200)
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
        db_table = 'label_alias'


class LabelAliasType(models.Model):
    name = models.TextField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'label_alias_type'


class LabelAnnotation(models.Model):
    label = models.IntegerField(primary_key=True)
    annotation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'label_annotation'
        unique_together = (('label', 'annotation'),)


class LabelAttribute(models.Model):
    label = models.IntegerField()
    label_attribute_type = models.IntegerField()
    label_attribute_type_allowed_value = models.IntegerField(blank=True, null=True)
    label_attribute_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label_attribute'


class LabelAttributeType(models.Model):
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    free_text = models.BooleanField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'label_attribute_type'


class LabelAttributeTypeAllowedValue(models.Model):
    label_attribute_type = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'label_attribute_type_allowed_value'


class LabelGidRedirect(models.Model):
    gid = models.UUIDField(primary_key=True)
    new_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label_gid_redirect'


class LabelIpi(models.Model):
    label = models.IntegerField(primary_key=True)
    ipi = models.CharField(max_length=11)
    edits_pending = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label_ipi'
        unique_together = (('label', 'ipi'),)


class LabelIsni(models.Model):
    label = models.IntegerField(primary_key=True)
    isni = models.CharField(max_length=16)
    edits_pending = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label_isni'
        unique_together = (('label', 'isni'),)


class LabelMeta(models.Model):
    id = models.IntegerField(primary_key=True)
    rating = models.SmallIntegerField(blank=True, null=True)
    rating_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label_meta'


class LabelRatingRaw(models.Model):
    label = models.IntegerField(primary_key=True)
    editor = models.IntegerField()
    rating = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'label_rating_raw'
        unique_together = (('label', 'editor'),)


class LabelTag(models.Model):
    label = models.IntegerField(primary_key=True)
    tag = models.IntegerField()
    count = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label_tag'
        unique_together = (('label', 'tag'),)


class LabelTagRaw(models.Model):
    label = models.IntegerField(primary_key=True)
    editor = models.IntegerField()
    tag = models.IntegerField()
    is_upvote = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'label_tag_raw'
        unique_together = (('label', 'editor', 'tag'),)


class LabelType(models.Model):
    name = models.CharField(max_length=255)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'label_type'


class Language(models.Model):
    iso_code_2t = models.CharField(max_length=3, blank=True, null=True)
    iso_code_2b = models.CharField(max_length=3, blank=True, null=True)
    iso_code_1 = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=100)
    frequency = models.IntegerField()
    iso_code_3 = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language'


class Link(models.Model):
    link_type = models.IntegerField()
    begin_date_year = models.SmallIntegerField(blank=True, null=True)
    begin_date_month = models.SmallIntegerField(blank=True, null=True)
    begin_date_day = models.SmallIntegerField(blank=True, null=True)
    end_date_year = models.SmallIntegerField(blank=True, null=True)
    end_date_month = models.SmallIntegerField(blank=True, null=True)
    end_date_day = models.SmallIntegerField(blank=True, null=True)
    attribute_count = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    ended = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'link'


class LinkAttribute(models.Model):
    link = models.IntegerField(primary_key=True)
    attribute_type = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_attribute'
        unique_together = (('link', 'attribute_type'),)


class LinkAttributeCredit(models.Model):
    link = models.IntegerField(primary_key=True)
    attribute_type = models.IntegerField()
    credited_as = models.TextField()

    class Meta:
        managed = False
        db_table = 'link_attribute_credit'
        unique_together = (('link', 'attribute_type'),)


class LinkAttributeTextValue(models.Model):
    link = models.IntegerField(primary_key=True)
    attribute_type = models.IntegerField()
    text_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'link_attribute_text_value'
        unique_together = (('link', 'attribute_type'),)


class LinkAttributeType(models.Model):
    parent = models.IntegerField(blank=True, null=True)
    root = models.IntegerField()
    child_order = models.IntegerField()
    gid = models.UUIDField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_attribute_type'


class LinkCreditableAttributeType(models.Model):
    attribute_type = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'link_creditable_attribute_type'


class LinkTextAttributeType(models.Model):
    attribute_type = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'link_text_attribute_type'


class LinkType(models.Model):
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    gid = models.UUIDField()
    entity_type0 = models.CharField(max_length=50)
    entity_type1 = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link_phrase = models.CharField(max_length=255)
    reverse_link_phrase = models.CharField(max_length=255)
    long_link_phrase = models.CharField(max_length=255)
    priority = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    is_deprecated = models.BooleanField()
    has_dates = models.BooleanField()
    entity0_cardinality = models.IntegerField()
    entity1_cardinality = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'link_type'


class LinkTypeAttributeType(models.Model):
    link_type = models.IntegerField(primary_key=True)
    attribute_type = models.IntegerField()
    min = models.SmallIntegerField(blank=True, null=True)
    max = models.SmallIntegerField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_type_attribute_type'
        unique_together = (('link_type', 'attribute_type'),)


class Medium(models.Model):
    release = models.IntegerField()
    position = models.IntegerField()
    format = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    track_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medium'


class MediumAttribute(models.Model):
    medium = models.IntegerField()
    medium_attribute_type = models.IntegerField()
    medium_attribute_type_allowed_value = models.IntegerField(blank=True, null=True)
    medium_attribute_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medium_attribute'


class MediumAttributeType(models.Model):
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    free_text = models.BooleanField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'medium_attribute_type'


class MediumAttributeTypeAllowedFormat(models.Model):
    medium_format = models.IntegerField(primary_key=True)
    medium_attribute_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medium_attribute_type_allowed_format'
        unique_together = (('medium_format', 'medium_attribute_type'),)


class MediumAttributeTypeAllowedValue(models.Model):
    medium_attribute_type = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'medium_attribute_type_allowed_value'


class MediumAttributeTypeAllowedValueAllowedFormat(models.Model):
    medium_format = models.IntegerField(primary_key=True)
    medium_attribute_type_allowed_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medium_attribute_type_allowed_value_allowed_format'
        unique_together = (('medium_format', 'medium_attribute_type_allowed_value'),)


class MediumCdtoc(models.Model):
    medium = models.IntegerField()
    cdtoc = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medium_cdtoc'


class MediumFormat(models.Model):
    name = models.CharField(max_length=100)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    year = models.SmallIntegerField(blank=True, null=True)
    has_discids = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'medium_format'


class MediumIndex(models.Model):
    medium = models.IntegerField(primary_key=True)
    toc = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medium_index'


class OldEditorName(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'old_editor_name'


class OrderableLinkType(models.Model):
    link_type = models.IntegerField(primary_key=True)
    direction = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'orderable_link_type'


class Place(models.Model):
    gid = models.UUIDField()
    name = models.CharField(max_length=200)
    type = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200)
    area = models.IntegerField(blank=True, null=True)
    coordinates = models.TextField(blank=True, null=True)  # This field type is a guess.
    comment = models.CharField(max_length=255)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    begin_date_year = models.SmallIntegerField(blank=True, null=True)
    begin_date_month = models.SmallIntegerField(blank=True, null=True)
    begin_date_day = models.SmallIntegerField(blank=True, null=True)
    end_date_year = models.SmallIntegerField(blank=True, null=True)
    end_date_month = models.SmallIntegerField(blank=True, null=True)
    end_date_day = models.SmallIntegerField(blank=True, null=True)
    ended = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'place'


class PlaceAlias(models.Model):
    place = models.IntegerField()
    name = models.CharField(max_length=200)
    locale = models.TextField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=200)
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
        db_table = 'place_alias'


class PlaceAliasType(models.Model):
    name = models.TextField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'place_alias_type'


class PlaceAnnotation(models.Model):
    place = models.IntegerField(primary_key=True)
    annotation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'place_annotation'
        unique_together = (('place', 'annotation'),)


class PlaceAttribute(models.Model):
    place = models.IntegerField()
    place_attribute_type = models.IntegerField()
    place_attribute_type_allowed_value = models.IntegerField(blank=True, null=True)
    place_attribute_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place_attribute'


class PlaceAttributeType(models.Model):
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    free_text = models.BooleanField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'place_attribute_type'


class PlaceAttributeTypeAllowedValue(models.Model):
    place_attribute_type = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'place_attribute_type_allowed_value'


class PlaceGidRedirect(models.Model):
    gid = models.UUIDField(primary_key=True)
    new_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place_gid_redirect'


class PlaceTag(models.Model):
    place = models.IntegerField(primary_key=True)
    tag = models.IntegerField()
    count = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place_tag'
        unique_together = (('place', 'tag'),)


class PlaceTagRaw(models.Model):
    place = models.IntegerField(primary_key=True)
    editor = models.IntegerField()
    tag = models.IntegerField()
    is_upvote = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'place_tag_raw'
        unique_together = (('place', 'editor', 'tag'),)


class PlaceType(models.Model):
    name = models.CharField(max_length=255)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'place_type'


class Recording(models.Model):
    gid = models.UUIDField()
    name = models.CharField(max_length=200)
    # artist_credit = models.IntegerField()
    artist_credit = models.ForeignKey(ArtistCredit, on_delete=models.CASCADE, )
    length = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    video = models.BooleanField()

    class Meta:
        # managed = False
        db_table = 'recording'

    def __str__(self):
        return self.name


class RecordingAlias(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    recording = models.IntegerField()
    name = models.CharField(max_length=200)
    locale = models.TextField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=200)
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
        db_table = 'recording_alias'


class RecordingAliasType(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.TextField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'recording_alias_type'


class RecordingAnnotation(models.Model):
    recording = models.IntegerField()
    annotation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recording_annotation'


class RecordingAttribute(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    recording = models.IntegerField()
    recording_attribute_type = models.IntegerField()
    recording_attribute_type_allowed_value = models.IntegerField(blank=True, null=True)
    recording_attribute_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recording_attribute'


class RecordingAttributeType(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    free_text = models.BooleanField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'recording_attribute_type'


class RecordingAttributeTypeAllowedValue(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    recording_attribute_type = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'recording_attribute_type_allowed_value'


class RecordingGidRedirect(models.Model):
    gid = models.UUIDField()
    new_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recording_gid_redirect'


class RecordingMeta(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    rating = models.SmallIntegerField(blank=True, null=True)
    rating_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recording_meta'


class RecordingRatingRaw(models.Model):
    recording = models.IntegerField()
    editor = models.IntegerField()
    rating = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'recording_rating_raw'


class RecordingTag(models.Model):
    recording = models.IntegerField()
    tag = models.IntegerField()
    count = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recording_tag'


class RecordingTagRaw(models.Model):
    recording = models.IntegerField()
    editor = models.IntegerField()
    tag = models.IntegerField()
    is_upvote = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'recording_tag_raw'


class Release(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    gid = models.UUIDField()
    name = models.CharField(max_length=200)
    artist_credit = models.IntegerField()
    release_group = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    packaging = models.IntegerField(blank=True, null=True)
    language = models.IntegerField(blank=True, null=True)
    script = models.IntegerField(blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255)
    edits_pending = models.IntegerField()
    quality = models.SmallIntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release'


class ReleaseAlias(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    release = models.IntegerField()
    name = models.CharField(max_length=200)
    locale = models.TextField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=200)
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
        db_table = 'release_alias'


class ReleaseAliasType(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.TextField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'release_alias_type'


class ReleaseAnnotation(models.Model):
    release = models.IntegerField()
    annotation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'release_annotation'


class ReleaseAttribute(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    release = models.IntegerField()
    release_attribute_type = models.IntegerField()
    release_attribute_type_allowed_value = models.IntegerField(blank=True, null=True)
    release_attribute_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_attribute'


class ReleaseAttributeType(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    free_text = models.BooleanField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'release_attribute_type'


class ReleaseAttributeTypeAllowedValue(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    release_attribute_type = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'release_attribute_type_allowed_value'


class ReleaseCountry(models.Model):
    release = models.IntegerField()
    country = models.IntegerField()
    date_year = models.SmallIntegerField(blank=True, null=True)
    date_month = models.SmallIntegerField(blank=True, null=True)
    date_day = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_country'


class ReleaseCoverart(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    cover_art_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_coverart'


class ReleaseGidRedirect(models.Model):
    gid = models.UUIDField()
    new_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_gid_redirect'


class ReleaseGroup(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    gid = models.UUIDField()
    name = models.CharField(max_length=200)
    artist_credit = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_group'


class ReleaseGroupAlias(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    release_group = models.IntegerField()
    name = models.CharField(max_length=200)
    locale = models.TextField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=200)
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
        db_table = 'release_group_alias'


class ReleaseGroupAliasType(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.TextField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'release_group_alias_type'


class ReleaseGroupAnnotation(models.Model):
    release_group = models.IntegerField()
    annotation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'release_group_annotation'


class ReleaseGroupAttribute(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    release_group = models.IntegerField()
    release_group_attribute_type = models.IntegerField()
    release_group_attribute_type_allowed_value = models.IntegerField(blank=True, null=True)
    release_group_attribute_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_group_attribute'


class ReleaseGroupAttributeType(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    free_text = models.BooleanField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'release_group_attribute_type'


class ReleaseGroupAttributeTypeAllowedValue(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    release_group_attribute_type = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'release_group_attribute_type_allowed_value'


class ReleaseGroupGidRedirect(models.Model):
    gid = models.UUIDField()
    new_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_group_gid_redirect'


class ReleaseGroupMeta(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    release_count = models.IntegerField()
    first_release_date_year = models.SmallIntegerField(blank=True, null=True)
    first_release_date_month = models.SmallIntegerField(blank=True, null=True)
    first_release_date_day = models.SmallIntegerField(blank=True, null=True)
    rating = models.SmallIntegerField(blank=True, null=True)
    rating_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_group_meta'


class ReleaseGroupPrimaryType(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'release_group_primary_type'


class ReleaseGroupRatingRaw(models.Model):
    release_group = models.IntegerField()
    editor = models.IntegerField()
    rating = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'release_group_rating_raw'


class ReleaseGroupSecondaryType(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.TextField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'release_group_secondary_type'


class ReleaseGroupSecondaryTypeJoin(models.Model):
    release_group = models.IntegerField()
    secondary_type = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'release_group_secondary_type_join'


class ReleaseGroupTag(models.Model):
    release_group = models.IntegerField()
    tag = models.IntegerField()
    count = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_group_tag'


class ReleaseGroupTagRaw(models.Model):
    release_group = models.IntegerField()
    editor = models.IntegerField()
    tag = models.IntegerField()
    is_upvote = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'release_group_tag_raw'


class ReleaseLabel(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    release = models.IntegerField()
    label = models.IntegerField(blank=True, null=True)
    catalog_number = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_label'


class ReleaseMeta(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    date_added = models.DateTimeField(blank=True, null=True)
    info_url = models.CharField(max_length=255, blank=True, null=True)
    amazon_asin = models.CharField(max_length=10, blank=True, null=True)
    amazon_store = models.CharField(max_length=20, blank=True, null=True)
    cover_art_presence = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'release_meta'


class ReleasePackaging(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'release_packaging'


class ReleaseRaw(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, blank=True, null=True)
    added = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    lookup_count = models.IntegerField(blank=True, null=True)
    modify_count = models.IntegerField(blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'release_raw'


class ReleaseStatus(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'release_status'


class ReleaseTag(models.Model):
    release = models.IntegerField()
    tag = models.IntegerField()
    count = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_tag'


class ReleaseTagRaw(models.Model):
    release = models.IntegerField()
    editor = models.IntegerField()
    tag = models.IntegerField()
    is_upvote = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'release_tag_raw'


class ReleaseUnknownCountry(models.Model):
    release = models.IntegerField()
    date_year = models.SmallIntegerField(blank=True, null=True)
    date_month = models.SmallIntegerField(blank=True, null=True)
    date_day = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_unknown_country'


class ReplicationControl(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    current_schema_sequence = models.IntegerField()
    current_replication_sequence = models.IntegerField(blank=True, null=True)
    last_replication_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'replication_control'


class Script(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    iso_code = models.CharField(max_length=4)
    iso_number = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    frequency = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'script'


class Series(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    gid = models.UUIDField()
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=255)
    type = models.IntegerField()
    ordering_attribute = models.IntegerField()
    ordering_type = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'series'


class SeriesAlias(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    series = models.IntegerField()
    name = models.CharField(max_length=200)
    locale = models.TextField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=200)
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
        db_table = 'series_alias'


class SeriesAliasType(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.TextField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'series_alias_type'


class SeriesAnnotation(models.Model):
    series = models.IntegerField()
    annotation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'series_annotation'


class SeriesAttribute(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    series = models.IntegerField()
    series_attribute_type = models.IntegerField()
    series_attribute_type_allowed_value = models.IntegerField(blank=True, null=True)
    series_attribute_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'series_attribute'


class SeriesAttributeType(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    free_text = models.BooleanField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'series_attribute_type'


class SeriesAttributeTypeAllowedValue(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    series_attribute_type = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'series_attribute_type_allowed_value'


class SeriesGidRedirect(models.Model):
    gid = models.UUIDField()
    new_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'series_gid_redirect'


class SeriesOrderingType(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'series_ordering_type'


class SeriesTag(models.Model):
    series = models.IntegerField()
    tag = models.IntegerField()
    count = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'series_tag'


class SeriesTagRaw(models.Model):
    series = models.IntegerField()
    editor = models.IntegerField()
    tag = models.IntegerField()
    is_upvote = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'series_tag_raw'


class SeriesType(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.CharField(max_length=255)
    entity_type = models.CharField(max_length=50)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'series_type'


class Tag(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.CharField(max_length=255)
    ref_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tag'


class TagRelation(models.Model):
    tag1 = models.IntegerField()
    tag2 = models.IntegerField()
    weight = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag_relation'


class Track(models.Model):
    # id = models.AutoField(db_column='BID', primary_key=True)
    id = models.AutoField(primary_key=True)
    gid = models.UUIDField()
    # recording = models.IntegerField()
    recording = models.ForeignKey(Recording, on_delete=models.CASCADE)
    medium = models.IntegerField()
    position = models.IntegerField()
    number = models.TextField()
    name = models.CharField(max_length=200)
    artist_credit = models.IntegerField()
    # artist_credit = models.ForeignKey(Recording, on_delete=models.CASCADE)
    length = models.IntegerField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    is_data_track = models.BooleanField()

    class Meta:
        # managed = False
        db_table = 'track'

    def __str__(self):
        return self.name


class TrackGidRedirect(models.Model):
    gid = models.UUIDField()
    new_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'track_gid_redirect'


class TrackRaw(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    release = models.IntegerField()
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'track_raw'


class Url(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    gid = models.UUIDField()
    url = models.TextField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'url'


class UrlGidRedirect(models.Model):
    gid = models.UUIDField()
    new_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'url_gid_redirect'


class Vote(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    editor = models.IntegerField()
    edit = models.IntegerField()
    vote = models.SmallIntegerField()
    vote_time = models.DateTimeField(blank=True, null=True)
    superseded = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'vote'


class Work(models.Model):
    # id = models.AutoField(db_column='BID', primary_key=True)
    id = models.AutoField(primary_key=True, unique=True)
    gid = models.UUIDField()
    name = models.CharField(max_length=200)
    type = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    artists = models.ManyToManyField(Artist, through='ArtistWork')

    class Meta:
        # managed = False
        db_table = 'work'

    def __str__(self):
        return self.name


class ArtistWork(models.Model):
    # id = models.IntegerField(primary_key=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'artistwork'


class WorkAlias(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    work = models.IntegerField()
    name = models.CharField(max_length=200)
    locale = models.TextField(blank=True, null=True)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort_name = models.CharField(max_length=200)
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
        db_table = 'work_alias'


class WorkAliasType(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.TextField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'work_alias_type'


class WorkAnnotation(models.Model):
    work = models.IntegerField()
    annotation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'work_annotation'


class WorkAttribute(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    work = models.IntegerField()
    work_attribute_type = models.IntegerField()
    work_attribute_type_allowed_value = models.IntegerField(blank=True, null=True)
    work_attribute_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_attribute'


class WorkAttributeType(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    free_text = models.BooleanField()
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'work_attribute_type'


class WorkAttributeTypeAllowedValue(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    work_attribute_type = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'work_attribute_type_allowed_value'


class WorkGidRedirect(models.Model):
    gid = models.UUIDField()
    new_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_gid_redirect'


class WorkLanguage(models.Model):
    work = models.IntegerField()
    language = models.IntegerField()
    edits_pending = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_language'


class WorkMeta(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    rating = models.SmallIntegerField(blank=True, null=True)
    rating_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_meta'


class WorkRatingRaw(models.Model):
    work = models.IntegerField()
    editor = models.IntegerField()
    rating = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'work_rating_raw'


class WorkTag(models.Model):
    work = models.IntegerField()
    tag = models.IntegerField()
    count = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_tag'


class WorkTagRaw(models.Model):
    work = models.IntegerField()
    editor = models.IntegerField()
    tag = models.IntegerField()
    is_upvote = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'work_tag_raw'


class WorkType(models.Model):
    id = models.AutoField(db_column='BID', primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.IntegerField(blank=True, null=True)
    child_order = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    gid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'work_type'
