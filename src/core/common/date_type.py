from datetime import datetime
from typing import Annotated

from pydantic import PlainSerializer


def iso_datetime_format(dt: datetime) -> str:
    """ISO 8601 с +00:00 вместо +0000"""
    formatted = dt.strftime('%Y-%m-%dT%H:%M:%S')
    if dt.tzinfo:
        offset = dt.strftime('%z')  # +0000
        tz_formatted = f"{offset[:3]}:{offset[3:]}"  # +00:00
        return f"{formatted}{tz_formatted}"
    return formatted


IsoDateTime: type[datetime] = Annotated[
    datetime,
    PlainSerializer(iso_datetime_format, return_type=str),
]
