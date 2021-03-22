---
layout: page
title: "For Attendees"
meta_title: "Information for Attendees for SIGCSE TS 2021"
permalink: "/attendees/"
sidebar: attendees
---

<a name="registration"></a>


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


## Post-Conference Access to Pathable
The SIGCSE TS 2021 chairs are working with the SIGCSE board to investigate offering post-conference access to the materials in Pathable.  More will be posted and announce as decisions are made.

Note that anyone that already has purchased full registration to the 2021 Technical Symposium (prior to March 20, 2021) will continue to have access to Pathable until March 2022 and can login with the Pathable link in the nav menu above.

<a class="button large radius {{ site.data.registration.registration_button.style }}" href="{{ url }}{{ site.data.registration.registration_button.url }}"{% if site.data.registration.registration_button.url contains 'http' %} target="_blank" {% endif %}>{{ site.data.registration.registration_button.text }}</a>

## Registering for SIGCSE TS 2021

The 52nd ACM Technical Symposium on Computer Science Education     
Virtual Event hosted on Pathable at [http://pathable.sigcse2021.org](http://pathable.sigcse2021.org)

* Pre-Symposium Events: March 8-13
* Workshops: March 13-14
* Technical Symposium: March 14-20
* Pathable Virtual Platform Opens: March 1

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

* _All registration rates are in US$._    
* _Student registration rates are for full-time students only._    
* _Exhibits Only grants access to the exhibit hall, supporter sessions, and select affiliated events ONLY.  You will not have access to any other content from the Technical Symposium with this type of registration, including keynotes, technical sessions, workshops, Birds-of-a-Feather, and others.  Authors/presenters cannot choose this category as you will not have access to your session in Pathable._

### Registering for Other Symposium Events through Cvent

#### Workshops

Workshops provide an in-depth review of, or introduction to, a topic of interest. A successful workshop should provide participants with materials and/or ideas that are immediately useful in the classroom.

All workshops will take place the Saturday and Sunday before the Technical Symposium starts as a part of "Workshop Weekend."  Like the Symposium itself, workshops will take place in Zoom meeting rooms through Pathable and will appear on the Pathable schedule of registrants.  

Each workshop will be three hours long.  A workshop fee is required and can be paid when you register for the Technical Symposium or can be added afterward if you choose to modify your registration.  _Symposium registration is required to attend any SIGCSE TS 2021 workshop._

__Workshop Registration Rates:__<br>
Early: {{site.data.registration.dates.early}} - {{site.data.registration.workshoprates.early}}<br>
Regular: {{site.data.registration.dates.regular}} - {{site.data.registration.workshoprates.regular}}<br>
On-site: {{site.data.registration.dates.day-of}} - {{site.data.registration.workshoprates.day-of}}<br>
<a href="{{ site.url }}/{{ site.baseurl }}/schedule/workshops">List of Available Workshops</a><br>

#### Affiliated Events

Affiliated Events are an excellent venue for SIGCSE TS sub-communities or groups to arrange a time to gather and present or discuss topics of interest. This year's slate of affiliated events highlight existing and emerging subfields, engage groups of diversity, and bring together communities of practice.

Affiliated events will take place in Pathable as the virtual platform. _Symposium registration is required to attend any SIGCSE TS 2021 affilated event._ See each individual affiliated event for information on registering. Some events require prior application or submission. For any questions related to affiliated events, please contact the organizers directly.

<a href="{{ site.url }}/{{ site.baseurl }}/schedule/affiliatedevents">List of Affiliated Events</a>

#### Special Events

Special events are sessions that take place outside the regular SIGCSE TS program and have been invited by the Symposium Chairs and/or the SIGCSE Board. These special events provide another way to engage with others at the Technical Symposium. _Symposium registration is required to attend any SIGCSE TS 2021 special event._ See each individual affiliated event for information on registering. For any questions related to affiliated events, please contact the organizers directly.

<a href="{{ site.url }}/{{ site.baseurl }}/schedule/specialevents">List of Special Events</a>

### Host Information

If your institution requires an address for reimbursement or approval purposes, you can use:

_Host:_ Association for Computing Machinery (ACM) / Special Interest Group on Computer Science Education (SIGCSE)    
_Address:_ 1601 Broadway, 10th Floor, New York, NY 10019-7434

_NOTE:_ This address cannot be used to send physical payments for registering for the Techncial Symposium.  For questions about how to register, please email [registration@sigcse2021.org](mailto:registration@sigcse2021.org).

As the Technical Symposium is being hosted in the United States (even if it is virtual), we have no VAT number that we can provide.

We also cannot provide VISA letters at this time.

### Questions?

For general questions about registration or help with Cvent, please email [registration@sigcse2021.org](mailto:registration@sigcse2021.org).

For help with special circumstances, such as proof of participation, please email [support@sigcse2021.org](mailto:support@sigcse2021.org).

Authors or presenters with questions regarding their participation in the Technical Symposium should email [program@sigcse2021.org](mailto:program@sigcse2021.org) or [symposium@sigcse2021.org](mailto:symposium@sigcse2021.org) as appropriate.

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
