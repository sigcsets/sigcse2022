---
layout: page
order: 1
title: SIGCSE TS 2021 Poster Schedule
sidebar: schedule_program
---

<button onclick="topFunction()" id="toTopButton" title="Go to top">Back to Top</button> 

{% assign current_day = "TODAY" %}
{% assign current_block = "BLOCK1" %}

{% for session in site.data.program %}
  {% if session.session_type == "Poster"%}
  {% if session.day != current_day %}
    {% assign current_day = session.day %}
    {% assign day_split = current_day | split: ", " %}
    {% assign current_block = session.start_time %}
<div id="{{ day_split[0] }}-{{current_block | slice: 1}}"></div>
<div class="block_header">{{current_day}} - {{ current_block }}</div>
  {% endif %}
  {% if session.start_time != current_block %}
    {% assign current_block = session.start_time %}
    {% assign day_split = current_day | split: ", " %}

    {% endif %}
<div class="card">
  <div class="container">
    <h3 id="{{session.session_id | downcase}}">{{ session.session_title }}</h3>
    {% if session.session_type == "Poster" %}
    <span class="alert-box papersession">{{session.day}} / {{session.start_time}} - {{session.end_time}}</span>
    {% elsif session.session_type == "Keynote" %}
    <span class="alert-box keynote">{{session.day}} / {{session.start_time}} - {{session.end_time}}</span>
    {% elsif session.session_type == "Panel / Special Session" %}
    <span class="alert-box panel">{{session.day}} / {{session.start_time}} - {{session.end_time}}</span>
    {% elsif session.session_type == "Special Event" %}
    <span class="alert-box specialevent">{{session.day}} / {{session.start_time}} - {{session.end_time}}</span>
    {% endif %}
    {% for submission in session.submissions %}
        <strong>{{submission.title}}</strong><br>
        {{submission.authors}}<br><br>
    {% endfor %}
  </div>
</div> 
  {% endif %}
{% endfor %}