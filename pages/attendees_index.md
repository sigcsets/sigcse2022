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

_All registration rates are in USD._

{% for rate_category in site.data.registration.rates %}
  <h3>{{ rate_category[0] }}</h3>
  <table width="100%" class="multibody">
    <tr><th scope="col">Registration Type</th><th scope="col">Early: <br>{{site.data.registration.dates.early}}</th><th scope="col">Regular: <br>{{site.data.registration.dates.regular}}</th><th scope="col">On-site: <br>{{site.data.registration.dates.day-of}}</th></tr>
    <tbody>
    {% for rate_type in rate_category[1] %}
      <tr><td>{{ rate_type[0] }}</td><td>{{ rate_type[1].early }}</td><td>{{ rate_type[1].regular }}</td><td>{{ rate_type[1].day-of }}</td></tr>
    {% endfor %}
    </tbody>
  </table>
  
{% endfor %}

_Student registration rates are for full-time students only._

__Workshop Registration Rates:__<br>
Early: {{site.data.registration.dates.early}} - {{site.data.registration.workshoprates.early}}<br>
Regular: {{site.data.registration.dates.regular}} - {{site.data.registration.workshoprates.regular}}<br>
On-site: {{site.data.registration.dates.day-of}} - {{site.data.registration.workshoprates.day-of}}<br>
<a href="{{ site.url }}/{{ site.baseurl }}/schedule/workshops">List of Available Workshops</a><br>

### Cancellation Policy

<p><strong>Cancellation requests must be made by March 1, 2021 at 11:59 PM Eastern Time.</strong> A processing fee of US$100 will be assessed for full rate registrations. A processing fee of US$25 will be assessed for reduced rate registrations. Regrettably, cancellations received after that date cannot be honored. The conference committee recognizes that sometimes last-minute cancellations can't be avoided<!-- For 2021, include only as HTML comment: due to weather, travel disruptions, and/or health issues -->. However, the conference incurs expenses for which it is liable based on registration counts. Registrants <!-- For 2021, include only as HTML comment: are strongly advised to purchase travel insurance to cover their non-refundable expenses. Also, registrants -->who find themselves unable to attend should be aware that registrations are transferable, but in general the conference committee cannot assist in finding an appropriate recipient.</p>

<p><strong>In the event that the symposium is cancelled due to circumstances beyond the organizers' control,</strong> refunds are not guaranteed. If refunds are issued, the amount will depend on the expenses and financial commitments incurred by the symposium as of the cancellation date.</p>

<!-- For 2021, include only as HTML comment: Please bring evidence of full-time student status to the conference. -->

<!-- For 2021, include only as HTML comment:
<hr />
<p><strong>Letters from ACM in support of visa applications:</strong></p><p>ACM is able to provide visa support letters to attendees as well as authors with accepted papers, posters, or members of the conference committee. For visa support letters, please send all requests to supportletters@acm.org with the following information.</p>
<ol>
<li>Name and mailing address as it appears on your passport.</li>
<li>The name of the conference you wish to attend.</li>
<li>Registration confirmation number.</li>
<li>If you are the author of any papers accepted for the conference, please provide the title.</li>
<li>Fax number and/or e-mail address of where the invitation letter should be sent</li>
</ol>
-->
