# KSBA Calendar Filter

Filter and download events from any KSBA (Kentucky School Boards Association) school calendar.

## Instructions

1. **Fork this repo.**

2. **Open `filter_calendar.py`.**

3. Change:
   ```python
   SCHOOL_CALENDAR_URL = "[insert school calendar URL here]"
   ```
   to your actual school calendar URL and email, this can be found here in Schulnetz/Agenda/Schüler/-innenpläne -> oben rechts -> Diesen Plan im ICAL Format abonnieren.
   <img width="620" height="470" alt="image" src="https://github.com/user-attachments/assets/63feca46-1893-4f3b-93b8-a1d011af6302" />

4. You can find the new URL which you can enter in every calender program under: <br>
 ```https://[your account name].github.io/ksba-calendar-filter/filtered.ics```

It will run every day at around 7-8 and then it'll take 2-6h to update depending on the email provider you connect it with.
You can also change the time it runs at in the workflow file if you want it to update at a different time.
