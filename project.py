"""
Module: management_system.py

This module contains classes for managing employees, projects, and tasks in a fictional company.
"""

class Project:
    """
    Class representing a project in the company.

    Attributes:
        project_id (str): The ID of the project.
        name (str): The name of the project.
        description (str): The description of the project.
        start_date (str): The start date of the project.
        end_date (str): The end date of the project.
        employees (list): List of employees associated with the project.
    """

    def __init__(self, project_id, name, description, start_date, end_date):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.employees = []
        pass

    def assign_employee(self, employee):
        self.employees.append(employee)
        pass
 
