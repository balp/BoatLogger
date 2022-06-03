import dataclasses
import datetime
import math
from typing import List

from pyramid.view import view_config


@dataclasses.dataclass
class Position:
    longitude: float
    latitude: float
    altitude: float


@dataclasses.dataclass
class LogEntry:
    when: datetime.datetime
    wind_direction: float
    wind_speed: float
    sea_state: str
    barometer: float
    temperature: float
    cog: float
    sog: float
    position: Position
    notes: str

    def degree(self, rad: float):
        return int(math.degrees(rad))


@view_config(route_name='home', renderer='boatLogger:templates/log_overview.jinja2')
def my_view(request):
    def degree(rad: float):
        return math.degrees(rad)

    logs: List[LogEntry] = [
        LogEntry(when=datetime.datetime.now() - datetime.timedelta(hours=2),
                 wind_direction=(3 * math.pi / 2),
                 wind_speed=6.5,
                 sea_state='',
                 barometer=0,
                 temperature=0,
                 cog=0.0,
                 sog=0.0,
                 position=Position(11.831233333333333, 58.14203333333333, 0.0),
                 notes="Passing Svanesund"
                 ),
        LogEntry(when=datetime.datetime.now() - datetime.timedelta(hours=1),
                 wind_direction=(3 * math.pi / 2),
                 wind_speed=6.5,
                 sea_state='',
                 barometer=0,
                 temperature=0,
                 cog=0.0,
                 sog=0.0,
                 position=Position(11.831233333333333, 58.14203333333333, 0.0),
                 notes="Still Passing Svanesund"
                 ),
        LogEntry(when=datetime.datetime.now(),
                 wind_direction=(3 * math.pi / 2),
                 wind_speed=6.5,
                 sea_state='',
                 barometer=0,
                 temperature=0,
                 cog=0.0,
                 sog=0.0,
                 position=Position(11.831233333333333, 58.14203333333333, 0.0),
                 notes="Not moving quickly"
                 )
    ]
    return {'project': 'boatLogger',
            'logbook': logs, }
