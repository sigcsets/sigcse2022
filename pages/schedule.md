---
layout: page-fullwidth
title: "Official Schedule for SIGCSE TS 2021"
meta_title: "Official Schedule for SIGCSE TS 2021"
# teaser: "COVID-19 Information for SIGCSE TS 2021"
permalink: "/schedule/"
---
<style>

/* declare a 7 column grid on the table */
#calendar {
	width: 100%;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
}

#calendar tr, #calendar tbody {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
 width: 100%;
}

caption {
	text-align: center;
  grid-column: 1 / -1;
  font-size: 130%;
  font-weight: bold;
  padding: 10px 0;
}

#calendar a {
	color: #8e352e;
	text-decoration: none;
}

#calendar td, #calendar th {
	padding: 5px;
	box-sizing:border-box;
	border: 1px solid #ccc;
}

#calendar .weekdays {
	background: #4a9bb4;  
}


#calendar .weekdays th {
	text-align: center;
	text-transform: uppercase;
	line-height: 20px;
	border: none !important;
	padding: 10px 6px;
	color: #fff;
	font-size: 13px;
}

#calendar td {
	min-height: 180px;
  display: flex;
  flex-direction: column;
}

#calendar .days li:hover {
	background: #d3d3d3;
}

#calendar .date {
	text-align: center;
	margin-bottom: 5px;
	padding: 4px;
	background: #333;
	color: #fff;
	width: 30px;
	border-radius: 50%;
  flex: 0 0 auto;
  align-self: flex-end;
}

#calendar .event {
  flex: 0 0 auto;
	font-size: 13px;
	border-radius: 4px;
	padding: 5px;
	margin-bottom: 5px;
	line-height: 14px;
	background: #e4f2f2;
	border: 1px solid #b5dbdc;
	color: #003aaf;
	text-decoration: none;
}

#calendar .event-desc {
	color: #666;
	margin: 3px 0 7px 0;
	text-decoration: none;	
}

#calendar .other-month {
	background: #f5f5f5;
	color: #666;
}

/* ============================
				Mobile Responsiveness
   ============================*/


@media(max-width: 768px) {

	#calendar .weekdays, #calendar .other-month {
		display: none;
	}

	#calendar li {
		height: auto !important;
		border: 1px solid #ededed;
		width: 100%;
		padding: 10px;
		margin-bottom: -1px;
	}
  
  #calendar, #calendar tr, #calendar tbody {
    grid-template-columns: 1fr;
  }
  
  #calendar  tr {
    grid-column: 1 / 2;
  }

	#calendar .date {
		align-self: flex-start;
	}
}
</style>
Last update: October 7, 2020    
All times Eastern Time Zone (North America)

<table id="calendar">
  <caption>March 2021</caption>
  <tr class="weekdays">
    <th scope="col">Sunday</th>
    <th scope="col">Monday</th>
    <th scope="col">Tuesday</th>
    <th scope="col">Wednesday</th>
    <th scope="col">Thursday</th>
    <th scope="col">Friday</th>
    <th scope="col">Saturday</th>
  </tr>
  

  <tr>
    <td class="day">
      <div class="date">7</div>
    </td>
    <td class="day">
      <div class="date">8</div>
    </td>
    <td class="day">
      <div class="date">9</div>
    </td>
    <td class="day">
      <div class="date">10</div>
    </td>
    <td class="day">
      <div class="date">11</div>
    </td>
    <td class="day">
      <div class="date">12</div>
    </td>
    <td class="day">
      <div class="date">13</div>
      <div class="event">
        <div class="event-desc">
          Workshop Block A
        </div>
        <div class="event-time">
          1:00pm to 4:00pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Workshop Block B
        </div>
        <div class="event-time">
          7:00pm to 10:00pm
        </div>
      </div>
    </td>
  </tr>
  <tr>
    <td class="day">
      <div class="date">14</div>
      <div class="event">
        <div class="event-desc">
          Workshop Block C
        </div>
        <div class="event-time">
          1:00pm to 4:00pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Special Event!
        </div>
        <div class="event-time">
          4:30pm to 7:30pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          SIGCSE TS 2021 Opening Event and Reception
        </div>
        <div class="event-time">
          8:00pm to 10:00pm
        </div>
      </div>
    </td>
    <td class="day">
      <div class="date">15</div>
      <div class="event">
        <div class="event-desc">
          Block 1A: Opening Keynote
        </div>
        <div class="event-time">
          1:00pm to 2:00pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          First Timer's Session and Keynote
        </div>
        <div class="event-time">
          2:00pm to 3:00pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Exhibit Hall and Supporter Sessions
        </div>
        <div class="event-time">
          3:00pm to 8:00pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Networking Block 1
        </div>
        <div class="event-time">
          4:15pm to 6:45pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Block 1B: Technical Sessions
        </div>
        <div class="event-time">
          8:00pm to 9:45pm
        </div>
      </div>
    </td>
    <td class="day">
      <div class="date">16</div>
      <div class="event">
        <div class="event-desc">
          Block 2A: Technical Sessions
        </div>
        <div class="event-time">
          1:00pm to 2:45pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Exhibit Hall and Supporter Sessions
        </div>
        <div class="event-time">
          3:00pm to 8:00pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Networking Block 2
        </div>
        <div class="event-time">
          4:15pm to 6:45pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Block 2B: Technical Sessions
        </div>
        <div class="event-time">
          8:00pm to 9:45pm
        </div>
      </div>
    </td>
    <td class="day">
      <div class="date">17</div>
            <div class="event">
        <div class="event-desc">
          Block 3A: Technical Sessions
        </div>
        <div class="event-time">
          1:00pm to 2:45pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Exhibit Hall and Supporter Sessions
        </div>
        <div class="event-time">
          3:00pm to 8:00pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Networking Block 3
        </div>
        <div class="event-time">
          4:15pm to 6:45pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Block 3B: SIGCSE Lifetime Achievement Award Keynote
        </div>
        <div class="event-time">
          8:00pm to 9:45pm
        </div>
      </div>
    </td>
    <td class="day">
      <div class="date">18</div>
            <div class="event">
        <div class="event-desc">
          Block 4A: Technical Sessions
        </div>
        <div class="event-time">
          1:00pm to 2:45pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Exhibit Hall and Supporter Sessions
        </div>
        <div class="event-time">
          3:00pm to 8:00pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Networking Block 4
        </div>
        <div class="event-time">
          4:15pm to 6:45pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Block 4B: Technical Sessions
        </div>
        <div class="event-time">
          8:00pm to 9:45pm
        </div>
      </div>
    </td>
    <td class="day">
      <div class="date">19</div>
            <div class="event">
        <div class="event-desc">
          Block 5A: Technical Sessions
        </div>
        <div class="event-time">
          1:00pm to 2:45pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Exhibit Hall and Supporter Sessions
        </div>
        <div class="event-time">
          3:00pm to 8:00pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Networking Block 5
        </div>
        <div class="event-time">
          4:15pm to 6:45pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Block 5B: Technical Sessions
        </div>
        <div class="event-time">
          8:00pm to 9:45pm
        </div>
      </div>
    </td>
    <td class="day">
      <div class="date">20</div>
            <div class="event">
        <div class="event-desc">
          Block 6A: Closing Keynote
        </div>
        <div class="event-time">
          1:00pm to 2:45pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Exhibit Hall and Supporter Sessions
        </div>
        <div class="event-time">
          3:00pm to 8:00pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Networking Block 6
        </div>
        <div class="event-time">
          4:15pm to 6:45pm
        </div>
      </div>
      <div class="event">
        <div class="event-desc">
          Nifty Block and SIGCSE TS Celebration!
        </div>
        <div class="event-time">
          8:00pm to 9:45pm
        </div>
      </div>
    </td>
  </tr>

</table>

### Session Types

_(This information is subject to change after the virtual platform has been selected.)_

__Technical Sessions__: Each Technical Session block will have eight parallel "rooms" with either paper presentations or panels/special sessions.  

__Paper Presentation Sessions__: Authors will be invited to prerecord a 20 minute presentation of their work that will be made available before the Technical Symposium in the virtual platform.  During the paper presentation session itself, each author will be given 20 minutes - 5 minutes for a short recap of their work with a few slides and then 15 minutes of Q&A.  Five authors will present during each paper presentation session.  All paper presentation sessions will be recorded and will be available on-demand through the virtual platform.

__Panels and Special Sessions__: Panels and Special Sessions will have the option of either prerecording their panel discussion and making it available before the Technical Symposium and then only having live Q&A and follow up discussion or doing the entire session live.  All panels and special sessions will be recorded and will be available on-demand through the virtual platform.