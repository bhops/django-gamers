# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from django.db import IntegrityError
from django.forms.models import model_to_dict

class GameScraperPipeline(object):
    def process_item(self, item, spider):
        try:
            item.save()
        except IntegrityError:
            pass
        return item

    def get_or_create(self, model, platform):
        model_class = type(model)
        created = False

        # Normally, we would use `get_or_create`. However, `get_or_create` would
        # match all properties of an object (i.e. create a new object
        # anytime it changed) rather than update an existing object.
        #
        # Instead, we do the two steps separately
        try:
            obj = model_class.objects.get(slug=model.slug, platform=platform)
            print "Got Item"
        except model_class.DoesNotExist:
            print "model.DoesNotExist"
            created = True
            obj = model  # DjangoItem created a model for us.
            obj.platform = platform
            return (obj, created)


    def update_model(destination, source, commit=True):
        pk = destination.pk

        source_dict = model_to_dict(source)
        for (key, value) in source_dict.items():
            setattr(destination, key, value)

        setattr(destination, 'pk', pk)

        if commit:
            destination.save()

