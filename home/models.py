from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel


class HomePage(Page):

    logo_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    sponsor1 = models.ForeignKey(
        'Sponsor',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    sponsor2 = models.ForeignKey(
        'Sponsor',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    bg_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    banner_title = models.CharField(
        max_length=100, default='Welcome to my homepage')

    card_image_1 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    card_title_1 = models.CharField(
        max_length=100, default='Card 1')

    card_image_2 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    card_title_2 = models.CharField(
        max_length=100, default='Card 2')

    card_image_3 = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    card_title_3 = models.CharField(
        max_length=100, default='Card 3')

    adv_banner = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    news_post_double = models.ForeignKey(
        'SportNewsPost',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    news_post_text = models.ForeignKey(
        'SportNewsPost',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    news_post_left = models.ForeignKey(
        'SportNewsPost',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    adv_sport_news = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    news_post_right = models.ForeignKey(
        'SportNewsPost',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    last_game_home_team = models.ForeignKey(
        'MatchInfo',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    next_game_detail = models.ForeignKey(
        'MatchInfo',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    league_table_team_info_pos1 = models.ForeignKey(
        'TeamLeagueDetail',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    league_table_team_info_pos2 = models.ForeignKey(
        'TeamLeagueDetail',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    league_table_team_info_pos3 = models.ForeignKey(
        'TeamLeagueDetail',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    watch = models.ForeignKey(
        'Watch',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    featured_video = models.ForeignKey(
        'SportNewsPost',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    club_sponsors_board = models.ForeignKey(
        'SponsorsBoard',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("logo_image"),
        SnippetChooserPanel("sponsor1"),
        SnippetChooserPanel("sponsor2"),
        ImageChooserPanel("bg_image"),
        FieldPanel("banner_title"),
        ImageChooserPanel("card_image_1"),
        FieldPanel("card_title_1"),
        ImageChooserPanel("card_image_2"),
        FieldPanel("card_title_2"),
        ImageChooserPanel("card_image_3"),
        FieldPanel("card_title_3"),
        ImageChooserPanel("adv_banner"),
        SnippetChooserPanel("news_post_double"),
        SnippetChooserPanel("news_post_text"),
        SnippetChooserPanel("news_post_left"),
        ImageChooserPanel("adv_sport_news"),
        SnippetChooserPanel("news_post_right"),
        SnippetChooserPanel("last_game_home_team"),
        SnippetChooserPanel("next_game_detail"),
        SnippetChooserPanel("league_table_team_info_pos1"),
        SnippetChooserPanel("league_table_team_info_pos2"),
        SnippetChooserPanel("league_table_team_info_pos3"),
        SnippetChooserPanel("watch"),
        SnippetChooserPanel("featured_video"),
        SnippetChooserPanel("club_sponsors_board"),
    ]


@register_snippet
class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='+'
    )

    panels = [
        FieldPanel("name"),
        ImageChooserPanel("image"),
    ]

    def __str__(self):
        return f'Sponsor: {self.name}'


@register_snippet
class SportNewsPost(models.Model):
    post_title = models.CharField(max_length=100)
    post_type = models.CharField(max_length=20, blank=True)
    post_text = models.CharField(max_length=240, blank=True)
    date = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )

    panels = [
        FieldPanel("post_title"),
        FieldPanel("post_type"),
        FieldPanel("post_text"),
        ImageChooserPanel("image"),
    ]

    def __str__(self):
        return f'News Post title: {self.post_title}'


@register_snippet
class Watch(models.Model):
    watch_name = models.CharField(max_length=25)
    watch_type = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    watch_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    watch_hrs = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    watch_minutes = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    watch_seconds = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    watch_name_tag = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )

    panels = [
        FieldPanel("watch_name"),
        ImageChooserPanel("watch_type"),
        ImageChooserPanel("watch_image"),
        ImageChooserPanel("watch_hrs"),
        ImageChooserPanel("watch_minutes"),
        ImageChooserPanel("watch_seconds"),
        ImageChooserPanel("watch_name_tag"),
    ]

    def __str__(self):
        return f'Watch: {self.watch_name}'


@register_snippet
class MatchInfo(models.Model):
    match_type = models.CharField(max_length=100, blank=False)
    match_location = models.CharField(max_length=100, blank=False)
    match_date = models.DateTimeField(auto_now=False, editable=True)
    club_name = models.CharField(max_length=100, blank=False)
    against_name = models.CharField(
        max_length=100,
        blank=False,
        default="Other team"
    )
    score_home = models.IntegerField(blank=False, default='0')
    score_other_team = models.IntegerField(blank=False, default='0')
    club_logo = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='+'
    )
    other_club_logo = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='+'
    )

    panels = [
        FieldPanel("match_type"),
        FieldPanel("match_location"),
        FieldPanel("match_date"),
        FieldPanel("club_name"),
        ImageChooserPanel("club_logo"),
        FieldPanel("score_home"),
        FieldPanel("against_name"),
        ImageChooserPanel("other_club_logo"),
        FieldPanel("score_other_team"),
    ]

    def __str__(self):
        return f'Match in {self.match_type}, on: {self.match_date}'


@register_snippet
class TeamLeagueDetail(models.Model):
    league_position = models.IntegerField(max_length=2, blank=False)
    team_name = models.CharField(max_length=100, blank=False)
    games_played = models.IntegerField(max_length=2, blank=False)
    goals_diff = models.IntegerField(max_length=3, blank=False)
    points = models.IntegerField(max_length=3, blank=False)
    team_logo = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='+'
    )

    panels = [
        FieldPanel("league_position"),
        FieldPanel("team_name"),
        ImageChooserPanel("team_logo"),
        FieldPanel("games_played"),
        FieldPanel("goals_diff"),
        FieldPanel("points"),
    ]

    def __str__(self):
        return f'Team name: {self.team_name}'


@register_snippet
class SponsorsBoard(models.Model):
    sponsors_board_name = models.CharField(max_length=100, blank=False)
    main_sponsor_1 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    main_sponsor_2 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    sponsor_1 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    sponsor_2 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    sponsor_3 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    sponsor_4 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    sponsor_5 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    sponsor_6 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    sponsor_7 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    sponsor_8 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    sponsor_9 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    sponsor_10 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    sponsor_11 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    sponsor_12 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    sponsor_13 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    sponsor_14 = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )

    panels = [
        FieldPanel("sponsors_board_name"),
        ImageChooserPanel("main_sponsor_1"),
        ImageChooserPanel("main_sponsor_2"),
        ImageChooserPanel("sponsor_1"),
        ImageChooserPanel("sponsor_2"),
        ImageChooserPanel("sponsor_3"),
        ImageChooserPanel("sponsor_4"),
        ImageChooserPanel("sponsor_5"),
        ImageChooserPanel("sponsor_6"),
        ImageChooserPanel("sponsor_7"),
        ImageChooserPanel("sponsor_8"),
        ImageChooserPanel("sponsor_9"),
        ImageChooserPanel("sponsor_10"),
        ImageChooserPanel("sponsor_11"),
        ImageChooserPanel("sponsor_12"),
        ImageChooserPanel("sponsor_13"),
        ImageChooserPanel("sponsor_14"),
    ]

    def __str__(self):
        return f'Board: {self.sponsors_board_name}'
