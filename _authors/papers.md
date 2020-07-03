---
layout: page
order: 0
title: "Paper"
plural: "Papers"
---

{% include submission-details.html %}

## SIGCSE Technical Symposium Paper Types

Papers describe an educational research project, classroom experience, teaching technique, curricular initiative, or pedagogical tool. All papers should explicitly state their motivating questions, relate to relevant literature, and contain an analysis of the effectiveness of the interventions. An **abstract submission is required for all papers** and it is due a week before the full paper is due.  

**Paper submissions are expected to be original and polished work.**  While there will be the opportunity for authors of accepted papers to revise work considering the feedback from reviewers, those revisions should be minor since there is no "review-revise-review" cycle for the SIGCSE Technical Symposium. Additionally, we expect submissions will include a review of previous, related work.

{% include review-anonymity.html %}

## Paper Tracks
Please ensure that you **submit your paper to the correct paper track**. Papers will be reviewed for the track they are submitted to and will not be moved between tracks.

* **Computing Education Research**. Papers should adhere to rigorous standards, describing research questions, hypotheses, methods, results, and limitations, as is typical and expected of research studies. These papers normally focus on topics relevant to computing education with emphasis on educational goals and knowledge units/topics; teaching and learning methods or techniques; evaluation of pedagogical approaches; studies of the many different populations that are engaged in computing education, including (but not limited to) students, instructors; and issues of gender, diversity, equity, and underrepresentation.  We welcome replication papers and papers that present null or negative results that meet the criteria below.

* **Experience Reports and Tools**. Papers should carefully describe the development and use of a computing education approach  or tool, the  context of use, and provide a rich reflection on what did or didn’t work, and why. This track accepts experience reports, teaching techniques, and pedagogical tools. All papers in this track should provide enough detail to enable the approach or tool to be  adopted by others.

* **Position and Curricula Initiative**. Position papers should engender fruitful academic discussion through a defensible opinion about a computing education topic, substantiated with evidence. Curricula Initiative papers discuss new and revised curricula, programs, degrees and include position papers. Papers about curricula, programs, and degrees should describe the motivating context before the new initiative was undertaken, what it took to put the initiative into place, the impact, and suggestions for others wishing to adopt it.

### Selecting a Track
Please select the most appropriate track for your work.  The Program Chairs will not move papers between tracks. Any submissions made to more than one track will be desk rejected from both tracks.  

Authors may find ["What is a SIGCSE Symposium Paper?"](https://dl.acm.org/citation.cfm?id=3243073) useful as they consider which track to submit to.  
* Computing Education Research papers report on work that addresses one or more research questions and where studies are pre-planned. 
* Experience Reports and Tools papers are a deeply reflective case study or experience that is of interest to the community; they typically don't have research questions, but instead, provide a reflection on the goal of the experience.  
* Papers that are describing a tool and its use should be submitted to the Experience Reports and Tools track.  A research study on a tool should be submitted to the Computing Education Research track.

### Paper Resources
There are many resources for writing high quality papers for submission to the SIGCSE Technical Symposium.  We encourage authors to read and evaluate papers from prior SIGCSE Technical Symposium, especially those designated as *best papers*, which were selected both due to content and high quality reporting (for example the [SIGCSE TS 2020 best papers](https://sigcse2020.sigcse.org/online/index.html#best-papers)).  Authors will also likely find the [paper review guidelines](/reviewers/paper-review-guidelines.html) beneficial for identifying how reviewers will assess papers for each track.   Below, we list additional resources that you may find useful as you write your papers, especially computing education research papers.

* [Writing a research question (csedresearch.org)](https://csedresearch.org/write-a-research-question/)
* [Reporting Tips (csedresearch.org)](https://csedresearch.org/reporting-activities/)
* [Checklist for Research Articles (csedresearch.org)](https://csedresearch.org/reviewing-articles/)
* [Evaluation Instruments (csedresearch.org)](https://csedresearch.org/evaluation-instruments/)
* [What's the difference between a research paper and an experience report? (Amy Ko)](https://gist.github.com/amyjko/689837b8eefccb3a8a28ff0aa5300615#whats-the-difference-between-a-research-paper-and-an-experience-report)

### Paper Topics
<section class="row">
<div class="large-3 columns">
<h4>Computing Topics</h4>
<ul>
{% for type in site.data.topics.computing %}
  <li>{{type}}</li>
{% endfor %}
</ul>
</div>
<div class="large-3 columns">
<h4>Education and Experience Topics</h4>
<ul>
{% for type in site.data.topics.experience%}
  <li>{{type}}</li>
{% endfor %}
</ul>
</div>
<div class="large-3 columns">
<h4>Methods Topics</h4>
<ul>
{% for type in site.data.topics.methods %}
  <li>{{type}}</li>
{% endfor %}
</ul>
</div>
<div class="large-3 columns">
<h4>Curriculum Topics</h4>
<ul>
{% for type in site.data.topics.curriculum%}
  <li>{{type}}</li>
{% endfor %}
</ul>
</div>
</section>

## Details about your abstract

Your abstract can be up to {{site.data.submissions.papers.abstract-limits}} and **must be submitted by the paper abstract deadline of {{site.data.cfp.round[0].date}}**.  There are no formatting requirements for the abstract. When you log in to EasyChair to submit the abstract, you may paste the abstract text into the form field. The abstract submission is required to have an opportunity to submit your paper; the full paper is due by **{{site.data.cfp.round[1].date}}**.

The abstract helps reviewers bid for papers that they are qualified and interested in reviewing.  To help the bidding and reviewing process, please submit an abstract that is as close to the finished version as possible.  The Program Chairs reserve the right to desk reject abstracts that do not contain content that can help a reviewer during bidding.

## How Should The Paper Be Formatted?

Authors **must submit ONLY an anonymized version of the paper**. The goal of the anonymized version is to, as much as possible, provide the author(s) of the paper with an unbiased review. The anonymized version should have ALL mentions of the authors removed (including author’s names and affiliation plus identifying information within the body of the paper such as websites or related publications). Self-citations need not be removed if they are worded so that the reviewer doesn’t know if the writer is citing themselves. That is, instead of writing “We reported on our first experiment in 2017 in a previous paper [1]”, the writer might write “In 2017, an initial experiment was done in this area as reported in [1].

If the paper is accepted for the conference and for publication, authors will be asked to complete a camera-ready copy that will include all appropriate author names, citations, and references.

The paper is limited to a maximum of {{site.data.submissions.papers.limits}} and must adhere to ACM's publication guidelines:

{% include template-information.html %}

If your paper is accepted you will have a chance to modify your publication version before it is published.

{% include submission-proposal.html %}
