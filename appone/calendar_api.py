from beautiful_date import Jul, hours
from gcsa.conference import ConferenceSolution, EntryPoint, SolutionType
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar


def calendar_api_work():
    start = (30 / Jul / 2022)[12:00]
    end = start + 2 * hours
    print(start)
    print(end)

calendar_api_work()
