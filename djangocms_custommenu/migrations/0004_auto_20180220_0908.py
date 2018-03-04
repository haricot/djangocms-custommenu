# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-20 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('djangocms_custommenu', '0003_stylemenu_configuration'),
    ]

    operations = [
        migrations.AddField(
            model_name='stylemenu',
            name='end_level',
            field=models.IntegerField(default=100, help_text='At which level the navigation tree should stop.', verbose_name='End level'),
        ),
        migrations.AddField(
            model_name='stylemenu',
            name='extra_active',
            field=models.IntegerField(default=100, help_text='How many levels of descendants of the currently active node should be displayed.', verbose_name='Extra active'),
        ),
        migrations.AddField(
            model_name='stylemenu',
            name='extra_inactive',
            field=models.IntegerField(default=0, help_text='How many levels of navigation should be displayed if a node is not a direct ancestor or descendant of the current active node.', verbose_name='Extra inactive'),
        ),
        migrations.AddField(
            model_name='stylemenu',
            name='levels',
            field=models.IntegerField(default=100, help_text='At which level the navigation tree should stop.', verbose_name='Levels'),
        ),
        migrations.AddField(
            model_name='stylemenu',
            name='menu_type',
            field=models.CharField(choices=[(b'show_menu', 'Show menu'), (b'show_sub_menu', 'Show sub menu')], default=b'show_menu', help_text='Check documentation here http://docs.django-cms.org/en/release-3.4.x/reference/navigation.html', max_length=255, verbose_name='Template'),
        ),
        migrations.AddField(
            model_name='stylemenu',
            name='nephews',
            field=models.IntegerField(default=100, help_text='How many levels of nephews (children of siblings) are shown.', verbose_name='Nephews'),
        ),
        migrations.AddField(
            model_name='stylemenu',
            name='root_level',
            field=models.IntegerField(blank=True, help_text='At what level, if any, the menu should have its root.', null=True, verbose_name='Root level'),
        ),
        migrations.AddField(
            model_name='stylemenu',
            name='root_page',
            field=models.ForeignKey(default=1, help_text='Menu tree starts from this page.', on_delete=django.db.models.deletion.CASCADE, to='cms.Page', verbose_name='Root page'),
        ),
        migrations.AddField(
            model_name='stylemenu',
            name='start_level',
            field=models.IntegerField(default=0, help_text='From which level the navigation should be rendered.', verbose_name='Start level'),
        ),
    ]