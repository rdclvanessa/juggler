from django.db import models


class Project(models.Model):
    """Project name and details"""
    name = models.CharField(
        max_length=50,
        help_text="Name of the Project."
    )
    lead = models.CharField(
        max_length=50,
        help_text="Team lead name"
    )
    dateStarted = models.DateField(
        verbose_name="Date the project was started."
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    """Task labels, details and completion"""
    label = models.CharField(
        max_length=50,
        help_text="Label of the task"
    )
    description = models.TextField(
        help_text="Task description"
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE)

    complete = models.BooleanField(
        default=False,
        help_text="Task completed or not"
    )

    def __str__(self):
        return self.label
