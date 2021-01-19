---
layout: page
order: 1
title: SIGCSE TS 2021 Program Schedule
sidebar: schedule_program
---

{% for session in site.data.program %}
  {% if session.session_type == "Paper Session" or session.session_type == "Keynote" or session.session_type == "Panel / Special Session" %}
<div class="card">
  <div class="container">
    <h3 id="{{session.session_id | downcase}}">{{ session.session_title }}</h3>
    {% if session.session_type == "Paper Session" %}
    <span class="alert-box">{{session.day}} at {{session.start_time}}</span>
    {% elsif session.session_type == "Keynote" %}
    <span class="alert-box keynote">{{session.day}} at {{session.start_time}}</span>
    {% elsif session.session_type == "Panel / Special Session" %}
    <span class="alert-box panel">{{session.day}} at {{session.start_time}}</span>
    {% endif %}
    {% for submission in session.submissions %}
        <strong>{{submission.title}}</strong><br>
        <em>{{submission.authors}}</em><br><br>
    {% endfor %}
  </div>
</div> 
  {% endif %}
{% endfor %}