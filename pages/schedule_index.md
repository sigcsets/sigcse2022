---
layout: page-fullwidth
title: "Program-At-A-Glance for SIGCSE TS 2022"
meta_title: "Program-At-A-Glance for SIGCSE TS 2022"
permalink: "/schedule/"
---
<style>

/* declare a 7 column grid on the table */
#calendar {
	width: 100%;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
}

#calendar tr, #calendar tbody {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
 width: 100%;
}

caption {
	text-align: center;
  grid-column: 1 / -1;
  font-size: 130%;
  font-weight: bold;
  padding: 10px 0;
}

/* #calendar a {
	color: #8e352e;
	text-decoration: none;
} */

#calendar td, #calendar th {
	padding: 5px;
	box-sizing:border-box;
	border: 1px solid #ccc;
}

#calendar .weekdays {
	background: #52bdf9;  
}


#calendar .weekdays th {
	text-align: center;
	text-transform: uppercase;
	line-height: 20px;
	border: none !important;
	padding: 10px 6px;
	color: #fff;
	font-size: 13px;
}

#calendar td {
	min-height: 180px;
  display: flex;
  flex-direction: column;
}

#calendar .days li:hover {
	background: #d3d3d3;
}

#calendar .date {
	text-align: center;
	margin-bottom: 5px;
	padding: 4px;
	background: #333;
	color: #fff;
	width: 30px;
	border-radius: 50%;
  flex: 0 0 auto;
  align-self: flex-end;
}

#calendar .event {
  flex: 0 0 auto;
	font-size: 13px;
	border-radius: 4px;
	padding: 5px;
	margin-bottom: 5px;
	line-height: 14px;
	background: #e4f2f2;
	border: 1px solid #b5dbdc;
	color: #003aaf;
	text-decoration: none;
}

a {
  color: #003aaf;
}

#calendar .event:hover {
  background: #a1e1f5;
}

#calendar .event-desc {
	color: #666;
	margin: 3px 0 7px 0;
	text-decoration: none;	
}

#calendar .other-month {
	background: #f5f5f5;
	color: #666;
}

/* ============================
				Mobile Responsiveness
   ============================*/


@media(max-width: 768px) {

	#calendar .weekdays, #calendar .other-month {
		display: none;
	}

	#calendar li {
		height: auto !important;
		border: 1px solid #ededed;
		width: 100%;
		padding: 10px;
		margin-bottom: -1px;
	}
  
  #calendar, #calendar tr, #calendar tbody {
    grid-template-columns: 1fr;
  }
  
  #calendar  tr {
    grid-column: 1 / 2;
  }

	#calendar .date {
		align-self: flex-start;
	}
}
</style>
Last update: {{ "now" | date: "%A, %B %d, %Y" }}    

For full details about the Workshops, please visit the <a href="/schedule/workshops">Workshops Page</a>.<br>
For full details about Affiliated Events, please visit the <a href="/schedule/affiliatedevents">Affiliated Events Page</a>.<br>

<br>
1. All times shown are Eastern Standard Time (EST).
2. All rooms shown are in the Rhode Island Convention Center unless otherwise indicated.
3. The following program does not reflect any recent changes where authors have changed their presentation modes, or submission-related information such as title, author names, and affiliations. Such changes will be updated periodically betweeen now and the start of the Technical Symposium.
4. For each entry, there are day, time, and room assigned. The day and time assignments should be correct and final, whereas the room assignment process is still on-going.

We thank you for your patience with us as we navigate the complexities associated with the hybrid design of this conference while adjusting to the evolving pandemic situation.
If you have any questions, please do not hesitate to contact the Program Co-Chairs (Judy, Leen-Kiat, and Brian) at <a href="mailto:program@sigcse2022.org">program@sigcse2022.org</a>.

{% for day in site.data.program2['days'] %}
<div class="block_header">{{day.name}}</div>
{% for session in site.data.program2['sessions'] %}
{% if day.day == session.day %}
<div class="element-item card" style="width: 100%">
  <div class="container">
    <h3>{{session.title}}</h3>
    {{day.name}} / {{ session.start }} - {{ session.end }}<br>
    {% if session.subsessions == null and session.location %} <i>{{ session.location }}</i><br> {% endif %}
    {% if session.subsessions == null and session.presenters %}
    <p>{{session.presenters}}</p><br>
    {% endif %}
    {% if session.description != null %}<span markdown="1">{{ session.description }}</span><br>{% endif %}
    <br>
    {% if session.subsessions != null %}
    <br>
        {% for submission in session.subsessions %}
            <strong>{{submission.title}} in {{ submission.location }}</strong><br>
            {{submission.presenters}}<br><br>
        {% endfor %}
    {% endif %}
  </div>
</div> 
{% endif %}
{% endfor %}
{% endfor %}
