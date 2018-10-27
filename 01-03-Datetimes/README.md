# 01-03 Datetimes

The datetime library allows for easy processing of dates and times.

```python
from datetime import datetime, date, timedelta
```

## Datetime
The datetime object is the default python object to represents any date&time. It supports a variety of methods including methods to pull the current time, add and subtract time.

```python
pi_datetime = datetime(year=2015, month=3, day=14, hour=9, minute=26, second=53)
```

## Date
The date object is a slimed down version fo the date object. It represents...surprisingly...the date. The date object can be added and subtracted from the datetime object as well as other date object.

```python
pi_date = date(year=2015, month=3, day=14)
```

## Timedelta
The timedelta is the result of any mathematical operations on either a date or datetime object. A timedelta object can also be added or subtracted from a datetime or date object to return the initial type. timedelta are useful for representing increments in time and performing consecutive operations on time.
