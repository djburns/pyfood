# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemGroup'
        db.create_table(u'food_itemgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vendor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['food.Vendor'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'food', ['ItemGroup'])

        # Adding model 'Item'
        db.create_table(u'food_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['food.ItemGroup'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['food.Item'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal(u'food', ['Item'])

        # Adding model 'UserOrder'
        db.create_table(u'food_userorder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['food.Order'])),
        ))
        db.send_create_signal(u'food', ['UserOrder'])

        # Adding model 'UserOrderItem'
        db.create_table(u'food_userorderitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['food.UserOrder'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['food.Item'])),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'food', ['UserOrderItem'])

        # Deleting field 'Order.closing_date'
        db.delete_column(u'food_order', 'closing_date')

        # Adding field 'Order.closing_datetime'
        db.add_column(u'food_order', 'closing_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 10, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ItemGroup'
        db.delete_table(u'food_itemgroup')

        # Deleting model 'Item'
        db.delete_table(u'food_item')

        # Deleting model 'UserOrder'
        db.delete_table(u'food_userorder')

        # Deleting model 'UserOrderItem'
        db.delete_table(u'food_userorderitem')


        # User chose to not deal with backwards NULL issues for 'Order.closing_date'
        raise RuntimeError("Cannot reverse this migration. 'Order.closing_date' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Order.closing_date'
        db.add_column(u'food_order', 'closing_date',
                      self.gf('django.db.models.fields.DateField')(),
                      keep_default=False)

        # Deleting field 'Order.closing_datetime'
        db.delete_column(u'food_order', 'closing_datetime')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'food.event': {
            'Meta': {'object_name': 'Event'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        u'food.item': {
            'Meta': {'object_name': 'Item'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['food.Item']"}),
            'item_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['food.ItemGroup']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        },
        u'food.itemgroup': {
            'Meta': {'object_name': 'ItemGroup'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['food.Vendor']"})
        },
        u'food.order': {
            'Meta': {'object_name': 'Order'},
            'closing_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['food.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organiser': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['food.Vendor']"})
        },
        u'food.userorder': {
            'Meta': {'object_name': 'UserOrder'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['food.Order']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'food.userorderitem': {
            'Meta': {'object_name': 'UserOrderItem'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['food.Item']"}),
            'user_order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['food.UserOrder']"})
        },
        u'food.vendor': {
            'Meta': {'object_name': 'Vendor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['food']