from django.test import TestCase
import food.models as models
import django.contrib.auth.models as auth
from datetime import datetime
from django.utils.timezone import utc

class BasicConfig():

    def __init__(self):
        """ creates some basic objects in the database to be tested with """
        self.names = {
            'vendor':'testVendor1',
            'event':'testEvent1',
            'user':'testUser1',
            'item':'testItem1',
            'subitem':'testItem2',
            'itemgroup':'testItemGroup1'}
        self.simple_date = datetime.fromtimestamp(1,utc)
        self.vendor = models.Vendor.objects.create(
            name=self.names['vendor'],
            description='test vendor')
        self.event = models.Event.objects.create(
            name=self.names['event'],
            postcode='XX00 0XX',
            description='test event')
        self.user = auth.User.objects.create(
            username=self.names['user'])
        self.order = models.Order.objects.create(
            event=self.event,
            vendor=self.vendor,
            organiser=self.user,
            closing_datetime=self.simple_date)
        self.userorder = models.UserOrder.objects.create(
            user=self.user,
            order=self.order)
        self.itemgroup = models.ItemGroup.objects.create(
            name=self.names['itemgroup'],
            vendor=self.vendor,
            description='item group')
        self.item = models.Item.objects.create(
            item_group = self.itemgroup,
            name = self.names['item'],
            description = 'item',
            price = 9.99)
        self.subitem = models.Item.objects.create(
            item_group = self.itemgroup,
            item = self.item,
            name = self.names['subitem'],
            description = 'subitem',
            price = 9.99)
        self.userorderitem = models.UserOrderItem.objects.create(
            user_order = self.userorder,
            item = self.item,
            comment = 'here is a comment')

    def delete(self):
        self.userorderitem.delete()
        self.userorder.delete()
        self.order.delete()
        self.user.delete()
        self.subitem.delete()
        self.item.delete()
        self.itemgroup.delete()
        self.event.delete()
        self.vendor.delete()

class VendorModelTestCase(TestCase):

    def setUp(self):
        self.basic = BasicConfig()

    def testUnicode(self):
        self.assertEqual(str(self.basic.vendor), self.basic.names['vendor'])

    def tearDown(self):
        self.basic.delete()


class ItemGroupModelTestCase(TestCase):

    def setUp(self):
        self.basic = BasicConfig()

    def testUnicode(self):
        self.assertEqual(str(self.basic.itemgroup), '{0} - {1}'.format(
            self.basic.names['vendor'],
            self.basic.names['itemgroup']))

    def tearDown(self):
        self.basic.delete()


class ItemModelTestCase(TestCase):

    def setUp(self):
        self.basic = BasicConfig()

    def testUnicode(self):
        self.assertEqual(str(self.basic.item), self.basic.names['item'])
        self.assertEqual(str(self.basic.subitem), '{0} - {1}'.format(
            self.basic.names['item'],
            self.basic.names['subitem']))

    def tearDown(self):
        self.basic.delete()


class EventModelTestCase(TestCase):

    def setUp(self):
        self.basic = BasicConfig()

    def testUnicode(self):
        self.assertEqual(str(self.basic.event), self.basic.names['event'])

    def tearDown(self):
        self.basic.delete()


class OrderModelTestCase(TestCase):

    def setUp(self):
        self.basic = BasicConfig()

    def testUnicode(self):
        self.assertEqual(str(self.basic.order), '{0} - {1} ({2})'.format(
            self.basic.names['event'],
            self.basic.names['vendor'],
            str(self.basic.simple_date)))

    def tearDown(self):
       self.basic.delete()


class UserOrderModelTestCase(TestCase):

    def setUp(self):
        self.basic = BasicConfig()

    def testUnicode(self):
        order_name = '{0} - {1} ({2})'.format(
            self.basic.names['event'],
            self.basic.names['vendor'],
            str(self.basic.simple_date))
        self.assertEqual(str(self.basic.userorder), '{0} ({1})'.format(
            self.basic.names['user'],
            order_name))

    def tearDown(self):
        self.basic.delete()


class UserOrderItemModelTestCase(TestCase):

    def setUp(self):
        self.basic = BasicConfig()

    def testUnicode(self):
        self.assertEqual(
            str(self.basic.userorderitem),
            self.basic.names['item'])

    def tearDown(self):
        self.basic.delete()


