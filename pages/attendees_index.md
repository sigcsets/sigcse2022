---
layout: page
title: "Participant Information"
meta_title: "Information for SIGCSE TS 2022 Participants"
permalink: "/participants/"
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

<!-- Comment out for 2022
## Post-Conference Access to Pathable
The SIGCSE TS 2021 chairs are working with the SIGCSE board to investigate offering post-conference access to the materials in Pathable.  More will be posted and announce as decisions are made.

Note that anyone that already has purchased full registration to the 2021 Technical Symposium (prior to March 20, 2021) will continue to have access to Pathable until March 2022 and can login with the Pathable link in the nav menu above.

<a class="button large radius {{ site.data.registration.registration_button.style }}" href="{{ url }}{{ site.data.registration.registration_button.url }}"{% if site.data.registration.registration_button.url contains 'http' %} target="_blank" {% endif %}>{{ site.data.registration.registration_button.text }}</a>
-->
## Hotel and Travel Information for SIGCSE TS 2022          
- [Travel Information](https://www.goprovidence.com/sigcse/getting-here/)
- [Hotel Information](https://www.goprovidence.com/sigcse/hotel-information/)


## Registering for SIGCSE TS 2022          

The 53rd ACM Technical Symposium on Computer Science Education Hybrid Event will be held at the [Rhode Island Convention Center](http://www.riconvention.com) and [Omni Providence Hotel](https://www.omnihotels.com/hotels/providence)  in Providence, Rhode Island, USA. 

* Pre-Symposium Affiliated Events: March 2
* Workshops: March 2, 4, and 5
* Technical Symposium: March 2-5
* Virtual Platform Opens: TBD

The SIGCSE TS 2022 organizing committee is excited to offer options for participants to participate virtually or travel to Providence and attend the conference in person. We hope to have an exciting and engaging experience for all participants, and hope very much to see many of you in person.  Recognizing that participants need information to make decisions about travel and gathering, we will keep this site updated with information as it is available.  Our registration system will allow you to switch your own registration between in-person and virtual participation, but keep in mind the discount dates.  The cost for your new registration will be based on the date you change it, not the date when you first registered. 


### In-Person Registration
{% for rate_category in site.data.registration.rates %}
  <h3>{{ rate_category[0] }}</h3>
  <table width="100%" class="multibody">
    <tr><th scope="col">Registration Type</th><th scope="col">Early: <br>{{site.data.registration.dates.early}}</th><th scope="col">Regular: <br>{{site.data.registration.dates.regular}}</th><th scope="col">On-site: <br>{{site.data.registration.dates.day-of}}</th></tr>
    <tbody>
    {% for rate_type in rate_category[1] %}
      <tr><td width="50%">{{ rate_type[0] }}</td><td>{{ rate_type[1].early }}</td><td>{{ rate_type[1].regular }}</td><td>{{ rate_type[1].day-of }}</td></tr>
    {% endfor %}
    </tbody>
  </table>
  
{% endfor %}

### Virtual Registration
{% for rate_category in site.data.virtualRegistration.virtual %}
  <h3>{{ rate_category[0] }}</h3>
  <table width="100%" class="multibody">
    <tr><th scope="col">Registration Type</th><th scope="col">Early: <br>{{site.data.virtualRegistration.dates.early}}</th><th scope="col">Regular: <br>{{site.data.virtualRegistration.dates.regular}}</th><th scope="col">On-site: <br>{{site.data.virtualRegistration.dates.day-of}}</th></tr>
    <tbody>
    {% for rate_type in rate_category[1] %}
      <tr><td width="50%">{{ rate_type[0] }}</td><td>{{ rate_type[1].early }}</td><td>{{ rate_type[1].regular }}</td><td>{{ rate_type[1].day-of }}</td></tr>
    {% endfor %}
    </tbody>
  </table>
  
{% endfor %}
* _All registration rates are in US$._    
* _Student registration rates are for full-time students only. Please bring evidence of full-time student status to the conference._    
* _The Exhibits Only registration rates grant access ONLY to the exhibit hall, supporter sessions, and selected Affiliated Events.  Such participants will NOT have access to any other content from the Technical Symposium with this type of registration, including keynotes, technical sessions, workshops, Birds-of-a-Feather, and others.  Presenters cannot choose this category._

# Workshops
  <table width="100%" class="multibody">
    <tr><th scope="col">Registration Type</th><th scope="col">Early: <br>{{site.data.virtualRegistration.dates.early}}</th><th scope="col">Regular: <br>{{site.data.virtualRegistration.dates.regular}}</th><th scope="col">On-site: <br>{{site.data.virtualRegistration.dates.day-of}}</th></tr>
    <tbody>
    {% for rate_type in site.data.registration.workshoprates %}
      <tr><td width="50%">{{ rate_type[0] }}</td><td>{{ rate_type[1].early }}</td><td>{{ rate_type[1].regular }}</td><td>{{ rate_type[1].day-of }}</td></tr>
    {% endfor %}
    </tbody>
  </table>
* _All registration rates are in US$._    
  

<!--
## Health and Safety
The ACM SIGCSE TS 2022 committee is commited to providing our community with a conference that supports virtual and in-person participation.  As the registration dates get closer, we will provide details on the platform for virtual attendees and what to expect if traveling to Providence.

Please know that we will adhere to ACM, ACM SIGCSE, [CDC](https://www.cdc.gov/coronavirus/2019-ncov/your-health/gatherings.html) and [Rhode Island Convention Center](https://www.riconvention.com/attend-an-event/covid-19-event-updates) recommendations, guidelines, and health protocols. In particular, the SIGCSE Board is requiring all in-person attendees at the SIGCSE Technical Symposium 2022 in Providence, RI, USA, to show proof of full vaccination. They are not allowing exemptions at this time because there are opportunities for attendees to participate remotely.
-->

## Visas
<p><strong>Letters from ACM in support of visa applications:</strong></p><p>ACM is able to provide visa support letters to attendees as well as authors with accepted papers, posters, or members of the conference committee. For visa support letters, please send all requests to supportletters@acm.org with the following information.</p>
<ol>
<li>Name and mailing address as it appears on your passport.</li>
<li>The name of the conference you wish to attend.</li>
<li>Registration confirmation number.</li>
<li>If you are the author of any papers accepted for the conference, please provide the title.</li>
<li>Fax number and/or e-mail address of where the invitation letter should be sent</li>
</ol>


## Carbon Offsets
ACM SIGCSE makes it is easy for attendees to offset their carbon footprint to the ACM SIGCSE Technical Symposium through the registration process. Donations will be passed directly to <a href="https://www.cooleffect.org/">Cool Effect</a>, an organization that helps individuals and businesses develop practical and cost-effective solutions to slow, stop, and reduce the climate crisis. During the registration process, you will see a check box option that will allow you to make a donation to offset your emissions from attending the symposium. This contribution is optional and distinct from the registration fee and will appear as such on your registration receipt. Please consult your organization in advance to determine if the expense is reimbursable. If you need to use different credit cards for your registration and your donation, you can simply log in again after registering, update your registration, and pay with a second credit card. ACM will forward the names of the individuals that contribute along with the amount of their contribution to Cool Effect who will acknowledge the contribution to the individual donor for tax purposes.  You can utilize the <a href="https://www.cooleffect.org/content/travel-offset">carbon offset calculator</a> to make the appropriate donation based on travel and lodging. 

<!--
## Henry Walker Fund
The SIGCSE Board gratefully acknowledges former Board chair Henry Walker for his efforts in establishing this grant program and for his generous donation which served as the impetus to get the program started. This program depends upon donations for continued operation and possible expansion. Already, several SIGCSE members and friends have contributed, and we strongly encourage further donations to help support this ongoing program. Donations may be sent to:

    ACM, Office of Financial Services
    1601 Broadway, 10th Floor
    New York, NY 10019-7434

Please make checks payable to ACM/SIGCSE with the memo "The SIGCSE Travel Grant Program". ACM is a not-for-profit, tax-exempt organization under Section 501(c)(3) of the Internal Revenue Code. As such, your contribution to SIGCSE is deductible to the extent provided by law.

-->

## Roommate Database
Coming soon.

## KidsCamp
We will be offering KidsCamp, onsite in the Omni Hotel.  The contract is still being negotiated.  If you are interested in reserving a spot in KidsCamp, then please email kidscamp@sigcse2022.org.  We will email you as soon as you can sign up!


<!-- 
## Workshops

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

_NOTE:_ This address cannot be used to send physical payments for registering for the Techncial Symposium.  For questions about how to register, please email [registration@sigcse2022.org](mailto:registration@sigcse2022.org).

As the Technical Symposium is being hosted in the United States (even if it is virtual), we have no VAT number that we can provide.

We also cannot provide VISA letters at this time.

### Questions?

For general questions about registration or help with Cvent, please email [registration@sigcse2022.org](mailto:registration@sigcse2022.org).

For help with special circumstances, such as proof of participation, please email [support@sigcse2022.org](mailto:support@sigcse2022.org).

Authors or presenters with questions regarding their participation in the Technical Symposium should email [program@sigcse2022.org](mailto:program@sigcse2022.org) or [symposium@sigcse2022.org](mailto:symposium@sigcse2022.org) as appropriate.
-->

## Cancellation Policy

<p><strong>Cancellation requests must be made by March 1, 2022 at 11:59 PM Eastern Time.</strong> A processing fee of US$100 will be assessed for full rate registrations. A processing fee of US$25 will be assessed for reduced rate and virtual registrations. Regrettably, cancellations received after that date cannot be honored. The conference committee recognizes that sometimes last-minute cancellations can't be avoided due to weather, travel disruptions, and/or health issues. However, the conference incurs expenses for which it is liable based on registration counts. In-person registrants are strongly advised to purchase travel insurance to cover their non-refundable expenses. Also, registrants who find themselves unable to attend should be aware that registrations are transferable, but in general the conference committee cannot assist in finding an appropriate recipient.</p>

<p><strong>In the event that the Symposium is cancelled due to circumstances beyond the organizers' control,</strong> refunds are not guaranteed. If refunds are issued, the amount will depend on the expenses and financial commitments incurred by the Symposium as of the cancellation date.</p>

<hr />
