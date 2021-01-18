---
layout: page
order: 1
title: SIGCSE TS 2021 Program Schedule
sidebar: schedule_program
---

{% for session in site.data.program %}
<div class="card">
  <div class="container">
    <h3 id="{{session.session_id | downcase}}">{{ session.session_title }}</h3>
    <span class="alert-box">{{session.session_type}} - {{session.day}} at {{session.start_time}}</span>
    {% for submission in session.submissions %}
        <strong>{{submission.title}}</strong><br>
        <em>{{submission.authors}}</em><br><br>
    {% endfor %}
  </div>
</div> 
{% endfor %}