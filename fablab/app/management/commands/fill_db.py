import random

from django.core import management
from django.core.management.base import BaseCommand
from ...models import *
from .utils import random_date, random_timedelta


def add_works():
    Work.objects.create(
        name="Фотолитография внутренних слоев",
        description="На поверхность платы наносится тонкий слой фоторезиста, который является светочувствительной пленкой. Плата помещается под ультрафиолетовую лампу или лазер, чтобы фоторезист был экспонирован к свету через маску. Используя специальный раствор, фоторезист, который не был экспонирован к свету, удаляется, оставляя топологию токопроводящих медных слоев на поверхности платы.",
        price=random.randint(1000, 5000),
        image="works/1.png"
    )

    Work.objects.create(
        name="Травление внутренних слоев",
        description="Плату погружают в химический раствор, который растворяет не защищенные медные поверхности, оставляя только топологию слоев меди. Фоторезист, который ранее был использован для защиты меди от травления, удаляется с поверхности платы.",
        price=random.randint(1000, 5000),
        image="works/2.png"
    )

    Work.objects.create(
        name="АОИ внутренних слоев",
        description="Автоматическая оптическая инспекция внутренних слоев проводится для проверки и обнаружения дефектов и несоответствий в топологии слоев меди.",
        price=random.randint(1000, 5000),
        image="works/3.png"
    )

    Work.objects.create(
        name="Прессование",
        description="Поверхность платы покрывается слоем оксида, который сформирует диэлектрическую изоляцию. При высоких температурах и давлении между слоями платы происходит прессование, чтобы обеспечить механическую прочность платы и обеспечить электрическую связь между слоями.",
        price=random.randint(1000, 5000),
        image="works/4.png"
    )

    Work.objects.create(
        name="Вскрытие базовых отверстий",
        description="Базовые отверстия, необходимые для прохождения проводников через слои платы, пробиваются.",
        price=random.randint(1000, 5000),
        image="works/5.png"
    )

    print("Услуги добавлены")


def add_orders():
    owners = CustomUser.objects.filter(is_superuser=False)
    moderators = CustomUser.objects.filter(is_superuser=True)

    if len(owners) == 0 or len(moderators) == 0:
        print("Заявки не могут быть добавлены. Сначала добавьте пользователей с помощью команды add_users")
        return

    works = Work.objects.all()

    for _ in range(30):
        order = Order.objects.create()
        order.status = random.randint(2, 5)
        order.owner = random.choice(owners)

        if order.status in [3, 4]:
            order.date_complete = random_date()
            order.date_formation = order.date_complete - random_timedelta()
            order.date_created = order.date_formation - random_timedelta()
            order.moderator = random.choice(moderators)
        else:
            order.date_formation = random_date()
            order.date_created = order.date_formation - random_timedelta()

        for i in range(random.randint(1, 3)):
            order.works.add(random.choice(works))

        order.save()

    print("Заявки добавлены")


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        management.call_command("clean_db")
        management.call_command("add_users")

        add_works()
        add_orders()









