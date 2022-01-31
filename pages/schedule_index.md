---
layout: page-fullwidth
title: "Program-At-A-Glance for SIGCSE TS 2022"
meta_title: "Program-At-A-Glance for SIGCSE TS 2022"
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

/* #calendar a {
	color: #8e352e;
	text-decoration: none;
} */

#calendar td, #calendar th {
	padding: 5px;
	box-sizing:border-box;
	border: 1px solid #ccc;
}

#calendar .weekdays {
	background: #52bdf9;  
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

a {
  color: #003aaf;
}

#calendar .event:hover {
  background: #a1e1f5;
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
Last update: {{ "now" | date: "%A, %B %d, %Y" }}    

<div markdown="1">
1. The program below may not reflect recent changes in which authors have changed their presentation mode, title, author names, or affiliations. Such changes will be updated periodically betweeen now and the start of the Technical Symposium.
1. Each entry includes the day, time, and room assigned. The day and time assignments should be correct and final, whereas the room assignment process is still on-going. All times shown are Eastern Standard Time (EST).
1. For full details about the Workshops, please visit the [Workshops Page](/schedule/workshops).
1. Full details about Affiliated Events are now included below.
1. A [roadmap](https://docs.google.com/document/d/1Z7w8HJ03WB5X0qF0b71eOKaP6CsDUMPw/edit?usp=sharing&ouid=107906839535250673001&rtpof=true&sd=true) of suggested sessions for K-12 participants to attend is now available.
</div>

<div markdown="1">
We thank you for your patience with us as we navigate the complexities associated with the hybrid design of this conference while adjusting to the evolving pandemic situation. If you have any questions, please do not hesitate to contact the Program Co-Chairs (Judy, Leen-Kiat, and Brian) at [program@sigcse2022.org](mailto:program@sigcse2022.org).
</div>

{% for day in site.data.program2['days'] %}
<div class="block_header">{{day.name}}</div>
{% for session in site.data.program2['sessions'] %}
{% if day.day == session.day %}
{% if session.id == null %}
<div class="element-item card" style="width: 100%">
{% else %}
<div class="element-item card" style="width: 100%" id="{{ session.id }}">
{% endif %}  
  <div class="container">
    <h3>{{session.title}}</h3>
    {{day.name}} 
		{% if session.start != null and session.end != null %}
			/ {{ session.start }} - {{ session.end }}
		{% endif %}
	<br>
    {% if session.location %} <i>{{ session.location }}</i><br> {% endif %}
    {% if session.subsessions == null and session.presenters %}
		<p>{{session.presenters}}</p>
    {% endif %}
    {% if session.description != null %}<span markdown="1">{{ session.description }}</span><br><br>{% endif %}
    {% if session.subsessions != null %}
		<br>
		{% for subsession in session.subsessions %}
            <strong>{{subsession.title}}</strong> <br>
			{% if session.location == null and subsession.location != null %}
				<i>{{ subsession.location }}</i><br>
			{% endif %}
            {{subsession.presenters}}<br><br>
        {% endfor %}
    {% endif %}
  </div>
</div> 
{% endif %}
{% endfor %}
{% endfor %}

<div class="block_header">Posters</div>

<h3 id="poster-session-1">Poster Session #1</h3>

**An Exploration into School District Decision Making Around Elementary Computer Science Programs**  
Eleanor Richard (University of Massachusetts Dartmouth)
  
**Exploring Threshold Concepts for Intermediate Students**  
Brian M. McSkimming (University at Buffalo); Adrienne Decker (University at Buffalo)
  
**ITT: An Interactive Tutoring Tool to Improve the Learning and Visualization of Compiler Design Theory From Implementation**  
Rafael Del Vado Vírseda (Universidad Complutense de Madrid)

**Incorporating the Concepts of Fairness and Bias into an Undergraduate Computer Science Course to Promote Fair Automated Decision Systems**  
Sheikh Rabiul Islam (University of Hartford); Ingrid Russell (University of Hartford); William Eberle (Tennessee Tech University); Darina Dicheva (Winston-Salem State University)

**Including Neurodiversity in Foundational and Applied Computational Thinking (INFACT)**  
Jodi Asbell-Clarke (TERC); Tara Robillard (TERC); Teon Edwards (TERC); Erin Bardar (TERC); Maya Israel (University of Florida); David Weintrop (University of Maryland); Shuchi Grover (Looking Glass Inc)

**Using Deep Learning to Localize Errors in Student Code Submissions**  
Shion Fujimori (University of Toronto); Mohamed Harmanani (University of Toronto); Owais Siddiqui (University of Toronto Mississauga); Lisa Zhang (University of Toronto Mississauga)
  
**LupSeat: A Randomized Seating Chart Generator to Prevent Exam Cheating**  
Joël Porquet-Lupine (University of California, Davis); Hiroya Gojo (University of California, Davis); Philip Breault (University of California, Davis)
  
**Unplugged Parallelism for First-Year CS Majors**  
Barbara M. Anthony (Southwestern University); D. Cenk Erdil (Sacred Heart University); Robert Montante (Bloomsburg University of Pennsylvania); Olga Glebova (Georgia State University)

**The CCLA: Cultivating a Culture of Computing at a Small Liberal Arts University**  
Mark M. Meysenburg (Doane University)
  
**CLICK: A Mentoring Approach to Increasing Female Participation in Computer Science**  
Amanda O'Farrell (TU Dublin); Micheal Griffin (Kishoge Community College); Keith Nolan (TU Dublin)

**Design and Implementation of an Academic Integrity Module for Undergraduate CS Students**  
Debarati Basu (Embry-Riddle Aeronautical University); Harini Ramaprasad (University of North Carolina at Charlotte)
  
**Preferred Course Modality and Effective Teaching Methods for Graduate Level Courses**  
Dewan Tanvir Ahmed (University of North Carolina at Charlotte)
  
**Where’s the Bug? Helping Students Find Errors in Physical Computing**  
Michael Schneider (University of Colorado, Boulder)

**Students of Color Organization Improves CS1 Grades**  
Allana Johnson (DePauw University); Gloria Childress Townsend (DePauw University); Khadija Stewart (DePauw University)
  
**Building K-12 Teacher Capacity to Expand Uptake in a National CS Curriculum**  
Keith Quille (TU Dublin); Roisin Faherty (TU Dublin); Brett A. Becker (UCD)
  
**CryptoScratch: Teaching Cryptography with Block-based Coding**  
Nathan Percival (University of Massachusetts Lowell); Pranathi Rayavaram (University of Massachusetts Lowell); Sashank Narain (University of Massachusetts Lowell); Claire Seungeun Lee (University of Massachusetts Lowell)
  
**Exploration of the Week-by-Week ICAP Transitions by Students**  
Adam M Gaweda (North Carolina State University); Collin F Lynch (North Carolina State University)

**Developing Inclusive Computing with the CT Pathways Toolkit**  
Merijke Coenraad (Digital Promise); Quinn Burke (Digital Promise); Pati Ruiz (Digital Promise); Kelly Mills (Digital Promise); Jeremy Roschelle (Digital Promise)
  
**Cybersecurity Shuffle: Using Card Magic to Introduce Cybersecurity Concepts**  
Preston Moore (New York University); Justin Cappos (New York University)
  
**Programming Practice Logs as a Tool to Support Equity and Inclusion**  
Sonya Cates (Roger Williams University)
  
**Transfer Support and Student Outcomes Correlations among URM and Non-URM Computing and Engineering Students**  
Danyelle Ireland (University of Maryland, Baltimore County); Amanda Menier (SageFox Consulting Group); Rebecca Zarch (SageFox Consulting Group); Jordan Esiason (SageFox Consulting Group)
  
**Exploring the Relationship Between Undergraduate Near-Peer Intersectional Computing, Mentoring, and Instructor Identities**  
Kristina Kramarczuk (University of Maryland); Maya Narayanasamy (University of Maryland); Anaum Khan (University of Maryland); Jandelyn Plane (University of Maryland); Kate Atchison (University of Maryland)
  
**Reflections on Educational Choices Made by Coding Bootcamp and Computer Science Graduates**  
Sherry Seibel (Simmons University); Nanette Veilleux (Simmons University); Tabitha Miles (Simmons University); Rachel Beaulieu (Simmons University)
  
**Building Community and Validating Co-Curricular Achievement**  
Paul Gestwicki (Ball State University); David L. Largent (Ball State University)

<h3 id="poster-session-2">Poster Session #2</h3>

**The Sol y Agua RPP: A Bilingual and Culturally Responsive Approach to Introduce Computational Thinking in Middle School**  
Monika Akbar (The University of Texas at El Paso); Katherine Mortimer (The University of Texas at El Paso); Grecia Navarrete (The University of Texas at El Paso); Stephanie Galvan (The University of Texas at El Paso); George Molina (The University of Texas at El Paso); Romelia Reyes (The University of Texas at El Paso); Cynthia Ontiveros (El Paso Independent School District); Scott Gray (El Paso Independent School District); Sarah Escandon (El Paso Independent School District); Monica Lyons (El Paso Independent School District); Pedro Delgado (El Paso Independent School District); Victor Medrano (El Paso Independent School District); Haleigh Kneedler (El Paso Independent School District); Patricia Benitez (El Paso Independent School District); Jacob Ramirez (El Paso Independent School District); Jesus Vazquez (El Paso Independent School District); Melissa Anderson (El Paso Independent School District)

**XDesign: Integrating Interface Design into Explainable AI Education**  
Hyungyu Shin (KAIST (Korea Advanced Institute of Science and Technology)); Nabila Sindi (KAIST (Korea Advanced Institute of Science and Technology)); Yoonjoo Lee (KAIST (Korea Advanced Institute of Science and Technology)); Jaeryoung Ka (KAIST (Korea Advanced Institute of Science and Technology)); Jeanyoung Y. Song (DGIST (Daegu Gyeongbuk Institute of Science and Technology)); Juho Kim (KAIST (Korea Advanced Institute of Science and Technology))
  
**Introducing Programming to Middle School Students to Increase Knowledge and Interest in Computer Science**  
Callan J. Noak (Lamar University); Jennifer L. Tsan (Lamar University); Sujing Wang (Lamar University); Stefan Andrei (Lamar University)
  
**INSPIRE: Fourth Industrial Revolution Teaching in the Classroom**  
Oli Howson (The Open University); Patricia Charlton (The Open University); Francisco Iniesto (The Open University); Wayne Holmes (The Open University)

**CSLINC a Nationwide CS MOOC for Second-level Students**  
Karen Nolan (TU Dublin); Keith Quille (TU Dublin); Brett A. Becker (University College Dublin)
  
**Climate Science, Data Science and Distributed Computing to Build Teen Students' Positive Perceptions of CS**  
Shuchi Grover (Looking Glass Ventures); Jessica Oster (Vanderbilt University); Ákos Lédeczi (Vanderbilt University); Brian Broll (Vanderbilt University); Menton Deweesw (Vanderbilt University)
  
**Women’s Longitudinal Career Trajectories Following Their Participation in a 3-Year Computing Camp**  
Maya Narayanasamy (University of Maryland)
  
**Pencil Puzzles as a Context for Introductory Computing Assignments in Diverse Settings**  
Zack Butler (Rochester Institute of Technology); Ivona Bezakova (Rochester Institute of Technology); Angelina Brilliantova (Rochester Institute of Technology); Hannah Miller (Rochester Institute of Technology); Kimberly Fluet (University of Rochester)
  
**Who is Failing CS1? Early Results from DFW Rate Investigation**  
Matthew Hertz (University at Buffalo); Carl Alphonce (University at Buffalo); Brian M. McSkimming (University at Buffalo); Adrienne Decker (University at Buffalo)
  
**Computer Science Education Policy: What California Can Tell Us about Contributing Factors to Success and Opportunities for Further Progress**  
Joel Knudson (American Institutes for Research); Candice Handjojo (American Institutes for Research); Ashley Sunde (American Institutes for Research)
  
**A Course on Data Quality in Analytics**  
Hongwei Zhu (University of Massachusetts Lowell)
  
**Developing and Implementing an Immersive Virtual Study Abroad Course on the History and Science of Information**  
James J. Butler (Pacific University); Shereen Khoja (Pacific University)
  
**Removing the Veil: Shining Light on the Lack of Inclusivity in Cybersecurity Education for Students with Disabilities**  
Felicia Hellems (Sacred Heart University); Sajal Bhatia (Sacred Heart University)
  
**Teaching Parallel Programming with Java and Pyjama**  
Ruth Kurniawati (Westfield State University)
  
**Can CS1 Curricula Be Used For Middle School Computer Programming Education?**  
Gurmeher Kaur (Chapel Hill High School); Kris Jordan (University of North Carolina at Chapel Hill); Jasleen Kaur (University of North Carolina at Chapel Hill)
  
**Equity in Access to and Participation in K-12 Computer Science Education**  
Madeline L Haynes (Texas Advanced Computing Center); Yiwen Yang (Texas Advanced Computing Center); Natashia Bibriescas (Texas Advanced Computing Center); Miriam Jacobson (Texas Advanced Computing Center); Stephanie Baker (Texas Advanced Computing Center); Jayce Warner (Texas Advanced Computing Center)

**How is Computational Thinking Defined in Elementary Science?**  
Jennifer Pietros (University of Rhode Island); Sara Sweetman (University of Rhode Island); Minsuk Shim (University of Rhode Island)
  
**Analyzing Student Experience of Time Trackers on Assessments**  
Ella Truslow (University of Virginia); Nour Goulmamine (University of Virginia); John R Hott (University of Virginia); Nada Basit (University of Virginia)
  
**MOCSIDE: An Open-source and Scalable Online IDE and Auto-Grader for Computer Science Education**  
Jonathan Cazalas (Florida Southern College); Max Barlow (Florida Southern College); Ibraheem Cazalas (Florida Southern College); Chase Robinson (Florida Southern College)
  
**The Effect of Program Cost on Minority Student Virtual Computing Outreach Participation**  
Kaylah Mackroy (Morehouse College); Whitney Nelson (Morehouse College); Kinnis Gosha (Morehouse College)
  
**Measuring the Impact of COVID-19 on the Health and Wellbeing of Computer Science Practitioners**  
Tom Crick (Swansea University); Cathryn Knight (Swansea University); Richard Watermeyer (University of Bristol)

**Add Some Action to the Output: A Ready-to-Use, Customizable Asset for Easily Adding Animation to Python Programs**  
Madalene Spezialetti (Trinity College); Brian Garten (Trinity College)
  
**Instantiating Specifications Grading in Computer Science Courses**  
David L. Largent (Ball State University)

**Insights from Virtual Culturally Responsive Computing Camps**  
Jaemarie Solyst (Carnegie Mellon University); Tara Nkrumah (Arizona State University); Angela Stewart (Carnegie Mellon University); Amanda Buddemeyer (University of Pittsburgh); Erin Walker (University of Pittsburgh); Amy Ogan (Carnegie Mellon University)

<h3 id="poster-session-3">Poster Session #3</h3>

**Computational Thinking Integration Design Principles in Humanities**  
Secil Caskurlu (Michigan State University); Anne Drew Hu (Michigan State University); Aman Yadav (Michigan State University); Rafi Santo (Telos Learning)

**Designing Equity-Centered Formative Assessment Artifacts for Computing**  
Pati Ruiz (Digital Promise); Emily Nestor (Talladega County Schools); Kelly Mills (Digital Promise); Merijke Coenraad (Digital Promise); Quinn Burke (Digital Promise)
  
**ExCITE: Broadening Participation with Service Learning**  
Lily R. Liang (University of the District of Columbia); Briana Wellman (University of the District of Columbia); Uzma Amir (University of the District of Columbia)
  
**Beyond MCQ: Designing Innovative, Engaging, Autogradable Assessments for Supporting Teaching & Learning in K-12 Computer Science**  
Shuchi Grover (Looking Glass Ventures); Bob Carmichael (Looking Glass Ventures); Shivram Venkatasubramaniam (Looking Glass Ventures)
  
**Investigating the Impact of Voice Response Options in Surveys**  
Pan Chen (University of Toronto); Naaz Sibia (University of Toronto Mississauga); Angela Zavaleta Bernuy (University of Toronto); Michael Liut (University of Toronto Mississauga); Joseph Jay Williams (University of Toronto)
  
**Training Near-Peer Mentors for Instructional Roles in Informal K-12 Computing Programs**  
Kristina Kramarczuk (University of Maryland, College Park); Maya Narayanasamy (University of Maryland, College Park); Kate Atchison (University of Maryland, College Park); Jandelyn Plane (University of Maryland, College Park)
 
**Predicting Success in CS1 - An Open Access Data Project**  
Keith Quille (TU Dublin); Keith Nolan (TU Dublin)
  
**Reflections of Cybersecurity Workshop for K-12 Teachers and High School Students**  
Chad Mourning (Ohio University); David Juedes (Ohio University); Allyson Hallman-Thrasher (Ohio University); Harsha Chenji (Ohio University); Savas Kaya (Ohio University); Avinash Karanth (Ohio University)
  
**A Case Study on The Adoption of Open Educational Resources in a C Programming Course**  
Julio César Bahamón (University of North Carolina at Charlotte)
 
**Women More Likely to Have a Sense of Belonging in Coding Bootcamps than University Computer Science Programs**  
Sherry Seibel (Simmons University); Nanette Veilleux (Simmons University); Tabitha Miles (Simmons University); Rachel Beaulieu (Simmons University)
  
**How Do Students Seek Help and How Do TAs Respond? Investigating Help-Seeking Strategies in CS1 Office Hours**  
Harrison Kwik (Northwestern University); Haoqi Zhang (Northwestern University); Eleanor O'Rourke (Northwestern University)

**Bringing Ethics and Justice into CS1 Courses through Data that Shows an Incomplete Picture**  
Yunhao Wang (University of Michigan); Johanna Okerlund (University of Michigan); H. V. Jagadish (University of Michigan)
  
**Universal Design of Interactive Mathematical Notebooks on Programming**  
Bin Guo (McMaster University); Jason Nagy (McMaster University); Emil Sekerinski (McMaster University)
 
**Curricula Design in Public Interest Tech Using OER**  
Susan P. Imberman (College of Staten Island CUNY)
  
**Validation of the Programming Emotions Questionnaire**  
Sarthak Awasthi (The Ohio State University); Rakhi Batra (The Ohio State University); Syedah Zahra Atiq (The Ohio State University)
  
**Students' Engagement in Collaborative Active Learning - Online v.s. Face-to-Face**  
Karen Jin (University of New Hampshire)
  
**Co-Designing Learning Experiences to Support the Development of Culturally Relevant CS Lessons in Elementary Classrooms**  
Jennie Chiu (University of Virginia); Anita Crowder (CodeVA); Dwayne Ray Cormier (Virginia Commonwealth University); Sheila Mosby (Petersburg School District); Eric Bredder (University of Virginia)

**Reading Between the Lines: Student Experiences of Resubmission in an Introductory CS Course**  
Leah Perlmutter (University of Washington); Jayne Everson (University of Washington); Ken Yasuhara (University of Washington); Brett Wortzman (University of Washington); Kevin Lin (University of Washington)

**Exam Time: How Students Spend Their Time When Taking Exams**  
Brian P. Railing (Carnegie Mellon University)
  
**Reversing Our Ways from x86 VM Configurations onto ARM-Based Raspberry Pis**  
Hsiao-An Wang (Marquette University); Dennis Brylow (Marquette University); Debbie Perouli (Marquette University)

**High-level to Low-level in Unity with GPU Shader Programming**  
Dimitrij (Mitja) Hmeljak (Indiana University)

**Metrics for Student Classroom Engagement and Correlation to Software Assignment Plagiarism**  
William Allen (Rensselaer Polytechnic Institute); Shelly Belsky (Rensselaer Polytechnic Institute); Ben Kelly (Rensselaer Polytechnic Institute); Jenay Barela (Rensselaer Polytechnic Institute); Matthew Peveler (PopSQL, Inc.); Barbara Cutler (Rensselaer Polytechnic Institute)
  
**An Introduction to Computer Science in the New Curriculum for Wales**  
Tom Crick (Swansea University)
  
<h3 id="poster-session-4">Poster Session #4 [Virtual]</h3>

**From the Game Ideas Prototypes to their Final Versions using International Intensive Project Results**  
Piotr Milczarski (University of Lodz); Norbert Borowski (University of Lodz); Artur Hłobaż (University of Lodz); Michał Beczkowski (University of Lodz)
  
**Teacher Self-efficacy During Professional Development for Game Design and Unity**  
Charles B. Hodges (Georgia Southern University); Mete Akcaoglu (Georgia Southern University); Andrew Allen (Georgia Southern University); Selçuk Doğan (Georgia Southern University)

**Diversifying the Face of Computing through Re-entry Initiatives for Returning Women**  
Farzana Rahman (Syracuse University); Elodie Billionniere (Miami Dade University); Vaishnavi Prashant Subhedar (Syracuse University)
  
**First Impressions of Using Stack Overflow for Education in a Computer Science Bachelor Programme**  
Stefan Hugtenburg (Delft University of Technology); Andy Zaidman (Delft University of Technology)
  
**How Do You Know if They Don't Know? The Design of Pre-Tests in Computing Education Research**  
Miranda C. Parker (University of California, Irvine); Yvonne S. Kao (WestEd)
  
**Do students Git it? A Lightweight Intervention to Increase Usage of Advanced Git Features**  
Todd Sproull (Washington University in St. Louis)
  
**Equity-focused Peer Mentoring for High School CS Teachers**  
Aleata Hubbard Cheuoua (WestEd); Bryan Twarek (CSTA); Ed Campos (CSTA); Amy Fetherston (CSTA Wisconsin Dairyland); Yvonne Kao (WestEd); Linnea Logan (CSTA Wisconsin Dairyland)
  
**Feedback on Program Development Process for CS1 Students**  
Charis Charitsis (Stanford University); Chris Piech (Stanford University); John C. Mitchell (Stanford University)
  
**Are We There Yet? Novices' Code Smells linked to Loop Constructs**  
Cruz Izu (The University of Adelaide); Shrey Chandra (The University of Adelaide)

**Inclusive Thinking Questionnaire: Preliminary Results**  
Dhruv Nagpal (BITS Pilani); Jaskaran Singh Bhatia (BITS Pilani); Dev Goel (BITS Pilani); Parthasarathy P D (BITS Pilani); Snigdha Tiwari (BITS Pilani); Swaroop Joshi (BITS Pilani)

**Authentic Learning of Machine Learning in Cybersecurity with Portable Hands-on Labware**  
Dan Chia-Tien Lo (Kennesaw State University); Hossain Shahriar (Kennesaw State University); Kai Qian (Kennesaw State University); Michael Whitman (Kennesaw State University); Fan Wu (Tuskegee University); Cassandra Thomas (Tuskegee University)
  
**“It is what the situation demands”: How Communities of Practice Create Value for CS Teachers in the Time of Covid**  
M. Livingston (University at Albany, SUNY); Lijun Ni (University at Albany, SUNY); Yan Tian (University at Albany, SUNY); Jason Bohrer (CSTA); Jake Baskin (CSTA)
  
**A Novel Machine Learning and Artificial Intelligence Course for Secondary School Students**  
Joyce Mahon (University College Dublin); Keith Quille (Technological University of Dublin); Brian Mac Namee (University College Dublin); Brett A. Becker (University College Dublin)
  
**Increasing Computing Participation through School Counselors**  
Wendy Chi (National Center for Women & Information Technology); Patricia Morreale (Kean University); Jean Chu (Kean University); Angela Cleveland (National Center for Women & Information Technology); Maureen Stewart (National Center for Women & Information Technology)

**Enhance Capacity to Foster Secondary Computer Science Teachers in Multiple Pathways**  
Dan Chia-Tien Lo (Kennesaw State University); Brian Lawler (Kennesaw State University)

**A Tool to Teach Expressions with Feedback About Broken Laws**  
Oleg Sychev (Volgograd State Technical University); Nikita Penskoy (Volgograd State Technical University); Grigory Terekhov (Volgograd State Technical University)
  
**TinyMLedu: The Tiny Machine Learning Open Education Initiative**  
Brian Plancher (Harvard John A. Paulson School of Engineering and Applied Sciences); Vijay Janapa Reddi (Harvard John A. Paulson School of Engineering and Applied Sciences)
 
**Evaluating Short Animation Videos in Asynchronous Teaching**  
Chen Liang (University of Michigan); Bobak Mortazavi (Texas A&M University)
  
**Testing Machine Learning Models to Identify Computer Science Students at High-risk of Probation**  
Hamza Errahmouni Barkam (University of California, Irvine); Max Wang (Cal Poly Pomona); Barbara Martinez Neda (University of California, Irvine); Sergio Gago Masague (University of California, Irvine)
  
**Developing an Ecosystem of Support for K-12 CS Educators**  
Bryan Twarek (Computer Science Teachers Association); Janice Mak (Arizona State University); Shaina Glass (Computer Science Teachers Association); Sababu Chaka Barashango (Georgia Institute of Technology); Cindi Chang (Nevada Department of Education)
  
**Enabling In-Class Peer Feedback on Introductory Computer Science Coding Exercises**  
Alina Zaman (University of Memphis); Vinhthuy Phan (University of Memphis); Amy Cook (University of Memphis)
  
**Don't Just Paste Your Stacktrace: Shaping Discussion Forums in Introductory CS Courses**  
Amogh Mannekote (University of Florida); Mehmet Celepkolu (University of Florida); Aisha Chung Galdo (University of Florida); Kristy Elizabeth Boyer (University of Florida); Maya Israel (University of Florida); Sarah Heckman (North Carolina State University); Kristin Stephens-Martinez (Duke University)
  
**Improved Testing of PrairieLearn Question Generators**  
Aayush Shah (UC Berkeley); Alan Lee (UC Berkeley); Chris Chi (Harvard University); Ruiwei Xiao (Washington University in St. Louis); Pranav Sukumar (UC Berkeley); Jesus Villalobos (UC Berkeley); Dan Garcia (UC Berkeley)
  
**Supporting Teacher Professional Learning and Curriculum Implementation Through Collaborative Curriculum Design**  
Lijun Ni (University at Albany, State University of New York); Gillian Bausch (University at Albany, State University of New York); Bernardo Feliciano (University of Massachusetts Lowell); Hsien-Yuan Hsu (University of Massachusetts Lowell); Fred Martin (University of Massachusetts Lowell)
  
**Using WebAssembly to Teach Code Generation in a Compiler Design Course**  
Ariel Ortiz (Tecnologico de Monterrey)
  
**Seamless Embedding of Programming IDEs into Computer-Based Testing Software**  
Abel Yagubyan (University of California, Berkeley); Dan Garcia (University of California, Berkeley)
  
**A Preliminary Study of Peer Assessment Feedback within Team Software Development Projects**  
Tom Crick (Swansea University); Tom Prickett (Northumbria University); Jill Bradnum (Northumbria University)
  
**Grading Mastery: Calculating Grades from Domain-Law Violations**  
Oleg Sychev (Volgograd State Technical University); Yaroslav Kamennov (Volgograd State Technical University)

<h3 id="poster-session-SRC-UG">Undergraduate Student Research Competition Poster Session</h3>

**K-12 CS Teacher Licensing in the US**  
Jessica M Yauney (Brigham Young University)
  
**Constructivism in Computer Science Education**  
Julie Smith (University of North Texas)
  
**Rho-NLR: A Neural Lumigraph Renderer with Controllable Illumination**  
Laura Perkins (New College of Florida)
  
**The Effect of Animation and Real-world Analogies on Learning Computer Systems Concepts by Diverse Students**  
Zhen Wu (University of Pittsburgh); Rachel Puckett (University of Pittsburgh); Wonsun Ahn (University of Pittsburgh); Sherif Khattab (University of Pittsburgh); Luis Oliveira (University of Pittsburgh); Vinicius Petrucci (University of Pittsburgh)
  
**Misconceptions about Computer Science Leads to Deferred Entrance to the Technology Field**  
Tabitha Miles (Simmons University)
  
**Interactive Network Visualization of Learning Progressions**  
Nathan Hurtig (Rose-Hulman Institute of Technology)

**Celer: A Smart Fleet Management System (Optimizing Traffic Flow in New York City)**  
Ugo Dos Reis (University of Toronto); Maheen Ferdousi (University of Toronto); Ilir Dema (University of Toronto)

**Using LSTM Networks for Multiparameter Physiological Signal Reconstruction to Reduce Training Time**  
Alia E. Alramahi (Benedictine University); Adrian K. Cornely (Benedictine University); Grace M. Mirsky (Benedictine University)

**[Virtual] Mining Data on Computing Majors Knowledge Game**
Sam Thach (Oregon Institute of Technology); Cecily Heiner (Oregon Institute of Technology)
 
<h3 id="poster-session-SRC-G">Graduate Student Research Competition Poster Session</h3>

**The Development of Computational Thinking in Computing Higher Education**  
Carolina Moreira Oliveira (Federal University of Paraná)

**Finding the Most Relevant Pages of the Learning Materials on which a Student Just Focuses**  
Taichi Imbe (Meisei University)

**What Does Literature Tell Us About Recursion?**  
Sean Mackay (University at Buffalo)
  
**Equipping Middle School Teachers with Culturally Responsive Pedagogy for Computer Science Through Community-centered Professional Development**  
Gillian Bausch (University at Albany, SUNY)
  
**Cross-grade Comparison of Computational Thinking in Young Children Using Normalized Unplugged Assessment Scores**  
Emily Relkin (Tufts University)

**[Virtual] Supporting Novice Learners’ Coding through Productive Failure-Based Debugging Activities** 
Sagun Giri (The Pennsylvania State University)
