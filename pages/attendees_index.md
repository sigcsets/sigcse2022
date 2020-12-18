---
layout: page
title: "For Attendees"
meta_title: "Information for Attendees for SIGCSE TS 2021"
permalink: "/attendees/"
sidebar: attendees
---

<a name="registration"></a>

## Registering for SIGCSE TS 2021

Registration for the 2021 SIGCSE Technical Symposium will open in early January 2021.

<style>
table tbody tr.odd, table tbody tr.alt, table tbody tr:nth-of-type(odd) {
    background-color: inherit;   /* reset rule in table.sccs */
}

table tbody:only-child tr.odd, table tbody:only-child tr.alt, table tbody:only-child tr:nth-of-type(odd) {
    background-color: #CCC;
}

table.multibody tbody:nth-child(odd) {
  background-color: #CCC;
}

th {
  text-align: center;
}

span.team-heading {
  font-size: 1.1rem;
}

</style>


### Registration Rates

<table width="100%" class="multibody">
    <tr><th scope="col">Registration Type</th><th scope="col">Early: <br>{{site.data.registration.dates.early}}</th><th scope="col">Advance: <br>{{site.data.registration.dates.advance}}</th><th scope="col">Late: <br>{{site.data.registration.dates.late}}</th></tr>
    <tbody>
    {% for rate_type in site.data.registration.rates %}
    <tr><td>{{ rate_type[0] }}</td><td>{{ rate_type[1].early }}</td><td>{{ rate_type[1].advance }}</td><td>{{ rate_type[1].late }}</td></tr>
    {% endfor %}

    </tbody>
</table>