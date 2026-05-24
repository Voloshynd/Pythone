import calendar
from datetime import date


class Calendar:
    WEEKDAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

    def __init__(self, year, task_list):
        self.year = year
        self.task_list = task_list
        self.cal = calendar.Calendar(firstweekday=0)

    def day_class(self, weekday):
        return self.WEEKDAYS[weekday]

    def month_tasks_count(self, month):
        return sum(
            1 for task in self.task_list
            if task.date.month == month and task.date.year == self.year
        )

    def render_day(self, y, m, d, weekday):
        if d == 0:
            return "<td class='noday'>&nbsp;</td>"

        full_date = date(y, m, d)
        td_plans = []
        td_class = self.day_class(weekday)

        for task in self.task_list:
            if task.date.date() == full_date:
                td_plans.append(task.title)

                match task.status:
                    case "To Do":
                        td_class += " to-do"

                    case "In Progress":
                        td_class += " in-progress"

                    case "Completed":
                        td_class += " completed"

                    case "Overdue":
                        td_class += " overdue"

        if td_plans:
            return (
                f"<td class='{td_class}' "
                f"title='{', '.join(td_plans)}'>{d}</td>"
                # f"<span class='month__tasks'>{count}</span>"
            )

        return f"<td class='{self.day_class(weekday)}'>{d}</td>"

    def render_month(self, month):
        weeks = self.cal.monthdays2calendar(self.year, month)

        html = []
        html.append(f'''
        <table border="0" cellpadding="0" cellspacing="0" class="month">
            <tr><th colspan="7" class="month">{calendar.month_name[month]}</th></tr>
            <tr>
                <th class="mon">Mon</th>
                <th class="tue">Tue</th>
                <th class="wed">Wed</th>
                <th class="thu">Thu</th>
                <th class="fri">Fri</th>
                <th class="sat">Sat</th>
                <th class="sun">Sun</th>
            </tr>
        ''')

        for week in weeks:
            html.append("<tr>")
            for day, weekday in week:
                html.append(self.render_day(self.year, month, day, weekday))
            html.append("</tr>")

        if self.month_tasks_count(month):
            html.append(f"""
            <tr>
                <td colspan="7" class="month__tasks">
                    Tasks: {self.month_tasks_count(month)}
                </td>
            </tr>
            """)

        html.append("</table>")
        return "".join(html)

    def render_year(self):
        html = [f'''
        <table border="0" cellpadding="0" cellspacing="0" class="year">
            <tr><th colspan="3" class="year">{self.year}</th></tr>
            <tr>
        ''']

        for i in range(1, 13):
            html.append(f"<td>{self.render_month(i)}</td>")
            if i % 3 == 0:
                html.append("</tr><tr>")

        html.append("</tr></table>")
        return "".join(html)
