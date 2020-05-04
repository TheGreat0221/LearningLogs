import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from learning_logs.models import Topic

topics = Topic.objects.all()

for topic in topics:
    print(topic.id, topic)

#If you know the ID of a particular object, you can use the moethod Topic.objects.get()
# to retrive that object and examine any attribute the object has.

t = Topic.objects.get(id=1)
print(t.text)
print(t.date_added)

#To get data through a foriegn key relationship, you use the lowercase name of the
# related model followed by an underscore and the word set
entries = t.entry_set.all()

for entry in entries:
    print(entry)


from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username, user.id)
