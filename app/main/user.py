"""Modules used by User class."""
from uuid import uuid4
from .event import Event
from .person import Person


class User(Person):

    def __init__(self, name, email, password, rsvp_category):
        super().__init__(name, email, rsvp_category)
        self.rsvp_category = "organizer"
        self._id = uuid4().hex
        self.password = password
        self.events = dict()
    def __repr__(self):
        return "user:" + self.email    

    def create_event(self, name, description, category, date, author, location,
                     owner_id):
        """Add an event."""
        new_event = Event(
            name,
            description,
            category,
            date,
            author,
            location,
            owner_id=self._id)
        self.events[new_event._id] = new_event
        return self.events[new_event._id]

    def update_event(self, _id, name, description, category, date, author,
                     location):
        """Edits an event."""
        for key in self.events.copy().keys():
            if _id == key:
                self.events[key].name = name
                self.events[key].description = description
                self.events[key].category = category
                self.events[key].date = date
                self.events[key].author = author
                self.events[key].location = location

    def delete_event(self, _id):
        """Deletes an event."""
        for key in self.events.copy().keys():
            if _id == key:
                del self.events[_id]
