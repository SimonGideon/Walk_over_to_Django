class Entry(models.Model):
    objects = models.Manager()
    entries = EntryManager()
    b = Blog.objects.get(id=1)
    b.entry_set(manager='entries').all()