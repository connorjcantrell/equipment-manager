from django.db import models
import uuid


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    street = models.CharField(max_length=60)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    contact = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f'{self.street}, {self.city} {self.state} {self.zipcode}'


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    ar_number = models.CharField(max_length=25, blank=True, null=True)
    name = models.CharField(max_length=60)
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.name


class WorkOrder(models.Model):
    """Model representing an assigned work order."""
    number = models.CharField(primary_key=True, max_length=6)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    est_hours = models.DecimalField(max_digits=6, decimal_places=2)
    date_entered = models.DateField()
    description = models.CharField(max_length=300)
    hours_remaining = models.DecimalField(max_digits=6, decimal_places=2)

    CALL_TYPE = (
        ('s', 'Service'),
        ('m', 'Preventative Maintenance'),
        ('p', 'Project')
    )

    call_type = models.CharField(
        max_length=1,
        choices=CALL_TYPE,
        blank = True,
        default='s',
        help_text='Call type'
    )

    JOB_STATUS = (
        ('i', 'In Progress'),
        ('o', 'On Hold'),
        ('c', 'Complete'),
        ('r', 'Reassigned'),
        ('x', 'Canceled'),
    )

    status = models.CharField(
        max_length=1,
        choices=JOB_STATUS,
        blank=True,
        default='i',
        help_text='Job status',
    )

    
    def __str__(self):
        """String for representing the Model object."""
        return f'WO:{self.number} - {self.location.street} - {self.description[:50]}...'

    class Meta:
        verbose_name = 'Work Order'


class Labor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    work_order = models.ForeignKey('WorkOrder', on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=4, decimal_places=2)

    RATES = (
        ('r', 'Regular Time'),
        ('o', 'Over Time'),
        ('d', 'Double Time'),
    )

    rates = models.CharField(
        max_length=1,
        choices=RATES,
        blank=True,
        default='r',
        help_text='Straight time, over time, or double time?'
    )
    notes = models.CharField(blank=True, max_length=500)
    start_time = models.DateTimeField()

    def __str__(self):
        return f'{self.amount}'
    
    class Meta:
        verbose_name_plural = "Labor"
