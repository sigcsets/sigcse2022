---
layout: page
order: 1
title: SIGCSE TS 2021 Demo Schedule
sidebar: schedule_program
---

{% assign current_day = "TODAY" %}
{% assign current_block = "BLOCK1" %}

{% for session in site.data.program %}
  {% if session.session_type == "Demonstration"%}
  {% if session.day != current_day %}
    {% assign current_day = session.day %}
    {% assign day_split = current_day | split: ", " %}
    {% assign current_block = session.start_time %}
  {% endif %}
  {% if session.start_time != current_block %}
    {% assign current_block = session.start_time %}
    {% assign day_split = current_day | split: ", " %}

    {% endif %}
<div class="card">
  <div class="container">
    <h3 id="{{session.session_id | downcase}}">{{ session.session_title }}</h3>
    {% if session.session_type == "Poster" %}
    <span class="alert-box papersession">{{session.day}} at {{session.start_time}}</span>
    {% elsif session.session_type == "Keynote" %}
    <span class="alert-box keynote">{{session.day}} at {{session.start_time}}</span>
    {% elsif session.session_type == "Panel / Special Session" %}
    <span class="alert-box panel">{{session.day}} at {{session.start_time}}</span>
    {% elsif session.session_type == "Special Event" %}
    <span class="alert-box specialevent">{{session.day}} at {{session.start_time}}</span>
    {% endif %}
    {% for submission in session.submissions %}
        <strong>{{submission.title}}</strong><br>
        {{submission.authors}}<br><br>
    {% endfor %}
  </div>
</div> 
  {% endif %}
{% endfor %}