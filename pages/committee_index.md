---
layout: page
title: "Symposium Committee"
meta_title: "Symposium Committee for SIGCSE TS 2021"
permalink: "/committee/"
sidebar: committee
---

<style>
table tbody tr.even, table tbody tr.alt, table tbody tr:nth-of-type(even) {
    background-color: inherit;   /* reset rule in table.sccs */
}

table tbody:only-child tr.even, table tbody:only-child tr.alt, table tbody:only-child tr:nth-of-type(even) {
    background-color: #CCC;
}

table.multibody tbody:nth-child(even) {
  background-color: #CCC;
}

table.multibody tbody:hover, tbody:hover th[rowspan], tbody:hover td[rowspan], tr:hover td {
   background-color: #FEFCDD; 
}

th {
  text-align: center;
}

span.team-heading {
  font-size: 1.1rem;
}

</style>
{% for comm in site.data.committee %}
<a name = "{{comm[0] | remove: " " }}"></a>  <!-- create anchors from committee name with no spaces -->
{% if comm[0] == "Program Committee" or comm[0] == "Organizing Committee" %}
<h2>{{comm[0]}}</h2>
<table width="100%" class="multibody">
  <tr><th scope="col">Team</th><th scope="col">Member</th><th scope="col">Institution</th></tr>
  {% for team in comm[1] %}
    {% assign team_rows = team[1].members.size | plus:1 %}
    <tbody>
      <tr><th scope="row" rowspan="{{team_rows}}"><span  class="team-heading">{{team[0]}}</span><br/>
        {% if team[1].email %}
          Email: <a href="mailto:{{team[1].email}}">{{team[1].email}}</a>
        {% endif %}
      </th></tr>
      {% for member in team[1].members %}
        <tr>
          <td>{{member.name}}</td>
          {% if member.inst %}
            <td>{{member.inst}}</td>
          {% else %}
            <td>&nbsp;</td>
          {% endif %}
        </tr>
      {% endfor %}
    </tbody>
  {% endfor %}
</table>
{% else %}
<h2>{{comm[0]}}</h2>
{% if comm[1].email %}
<p>Email: <a href="mailto:{{comm[1].email}}">{{comm[1].email}}</a></p>
{% endif %}
  <table width="100%">
    <tr><th scope="col">Name</th><th scope="col">Institution</th></tr>
      {% for member in comm[1].members %}
        <tr>
          <td>{{member.name}}</td>
          {% if member.inst %}
            <td>{{member.inst}}</td>
          {% else %}
            <td>&nbsp;</td>
          {% endif %}
        </tr>
      {% endfor %}
  </table>
{% endif %}
{% endfor %}

