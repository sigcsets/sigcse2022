---
layout: page
order: 1
title: SIGCSE TS 2021 Program Schedule
sidebar: schedule_program
---

<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.2.2/jquery.min.js"></script>
<script src="//unpkg.com/isotope-layout@3/dist/isotope.pkgd.min.js"></script>


<script>
var filters = {};
$(document).ready(function() {
var $grid = $('.isotope');
window.isotope = new Isotope($grid[0], {
  itemSelector: '.element-item',
  layoutMode: 'vertical'
});

function concatValues( obj ) {
  var value = '';
  for ( var prop in obj ) {
    value += obj[ prop ];
  }
  return value;
}

$('.button-group').each( function( i, buttonGroup ) {
    var $buttonGroup = $( buttonGroup );
    $buttonGroup.on( 'click', 'button', function() {

          // get group key
        var $this = $(this);
        var $buttonGroup = $this.parents('.button-group');
        var filterGroup = $buttonGroup.attr('data-filter-group');
        console.log(filterGroup, $buttonGroup);
          // set filter for group
        filters[ filterGroup ] = $this.attr('data-filter');
        var filterValue = concatValues( filters );
        window.isotope.arrange({ filter: filterValue });
    });
});


  // change is-checked class on buttons
  $('.button-group').each( function( i, buttonGroup ) {
    var $buttonGroup = $( buttonGroup );
    $buttonGroup.on( 'click', 'button', function() {
      $buttonGroup.find('.is-checked').removeClass('is-checked');
      $( this ).addClass('is-checked');
    });
  });
});
</script>

<button onclick="topFunction()" id="toTopButton" title="Go to top">Back to Top</button> 
Day: 
<div class="button-group" data-filter-group="day">
  <button data-filter="">All</button>
  <button data-filter=".Sunday">Sun</button>
  <button data-filter=".Monday">Mon</button>
  <button data-filter=".Tuesday">Tue</button>
  <button data-filter=".Wednesday">Wed</button>
  <button data-filter=".Thursday">Thu</button>
  <button data-filter=".Friday">Fri</button>
  <button data-filter=".Saturday">Sat</button>
</div>

Session Type: 
<div class="button-group" data-filter-group="type">
  <button data-filter="">All</button>
  <button data-filter=".paper.session">Paper Session</button>
  <button data-filter=".keynote">Keynote</button>
  <button data-filter=".panel_special.session">Panel / Special Session</button>
  <button data-filter=".lightning.talk">Lightning Talk</button>
  <button data-filter=".special.event">Special Event</button>
</div>

<div class="isotope">
{% assign current_day = "TODAY" %}
{% assign current_block = "BLOCK1" %}

{% for session in site.data.program %}
  {% if session.day != current_day %}
    {% assign current_day = session.day %}
    {% assign day_split = current_day | split: ", " %}
  {% endif %}
  {% if session.start_time != current_block %}
    {% assign current_block = session.start_time %}
    {% assign day_split = current_day | split: ", " %}
    <!--
<div id="{{ day_split[0] }}-{{current_block | slice: 0}}"></div>
<div class="block_header">{{current_day}} - {{ current_block }}</div>
-->
    {% endif %}
<div class="element-item card {{ day_split[0] }} {{session.session_type | downcase | replace: ' / ', '_' | remove: ' '}}" style="width: 100%">
  <div class="container">
    <h3 id="{{session.session_id | downcase}}">{{ session.session_title }}</h3>
    {% if session.session_type == "Paper Session" %}
    <span class="alert-box papersession">{{session.day}} / {{session.start_time}} - {{session.end_time}}</span>
    {% elsif session.session_type == "Keynote" %}
    <span class="alert-box keynote">{{session.day}} / {{session.start_time}} - {{session.end_time}}</span>
    {% elsif session.session_type == "Panel / Special Session" or session.session_type == "Lightning Talk" %}
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
{% endfor %}
</div> 
