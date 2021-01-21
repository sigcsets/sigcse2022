---
layout: page
order: 1
title: Special Event Schedule
sidebar: schedule_specialevents
---

<button onclick="topFunction()" id="toTopButton" title="Go to top">Back to Top</button> 

<strong>What are special events?</strong> : Special events are sessions that take place outside the regular SIGCSE TS program and have been invited by the Symposium Chairs and/or the SIGCSE Board.  These special events provide another way to engage with others at the Technical Symposium.  <em>Symposium registration is required to attend any SIGCSE TS 2021 special event.</em>  See each individual affiliated event for information on registering.  For any questions related to affiliated events, please contact the organizers directly.

{% for specialevent in site.data.specialevents.specialevents %}
<div class="card">
    <div class="container">
<h2 id="{{specialevent.event | downcase}}">{{ specialevent.title }}</h2>
<span class="alert-box info">{{ specialevent.day }} / {{ specialevent.time }}</span>
{% if specialevent.url %}
<p><strong>Event website</strong> : <a href="{{specialevent.url}}" target=_new>{{specialevent.url}}</a></p>
{% endif %}
<p><strong>Event organizers</strong> : {{specialevent.organizers}}</p>
<p><strong>Event contact</strong> : <a href="mailto:{{specialevent.contact}}">{{specialevent.contact}}</a></p>
<p><strong>How to register</strong> : {{specialevent.register}}</p>
{% if specialevent.submissions %}</p>
<p><strong>Submissions</strong> : {{specialevent.submissions}}</p>
{% endif %}
<p>{{specialevent.description}}</p>
</div>
</div>
{% endfor %}