import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from MainApp.models import Pizza

pizzas = Pizza.objects.all()

for p in pizzas:
    print(p.id, ' ', p.text)

p = Pizza.objects.get(id=1)
print(p)

toppings = p.topping_set.all()

for t in toppings:
    print(t)

comments = p.comment_set.all()
for c in comments:
    print(c.text)