from datetime import datetime

from django.shortcuts import render
from gcsa.conference import ConferenceSolution, EntryPoint, SolutionType
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar


def index(request):
    if request.method == 'POST':
        start = request.POST.get('datetime')
        start2 = datetime.fromisoformat(start)
        end = request.POST.get('enddatetime')
        end2 = datetime.fromisoformat(end)
        email = request.POST.get('email')
        calendar = GoogleCalendar('musaddiq838@gmail.com', credentials_path='E:\code_test\credentials.json')
        event = Event('Meeting',
                      start=start2,
                      end=end2,
                      timezone='Asia/Kolkata',
                      location='Karnataka',
                      conference_solution=ConferenceSolution(
                          entry_points=EntryPoint(
                              EntryPoint.VIDEO,
                              uri='https://meet.google.com/aaa-bbbb-ccc'
                          ),
                          solution_type=SolutionType.HANGOUTS_MEET,
                      ),
                      attendees=[
                          email,
                      ])
        c = calendar.add_event(event, send_updates='all')
        print(c)
    return render(request, 'index.html')
