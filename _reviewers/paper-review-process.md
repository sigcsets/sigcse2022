---
layout: page
order: 1.2
title: Paper Review Process
showTitle: true
---

SIGCSE Technical Symposium papers are reviewed using a dual-anonymous review process (see below) managed through EasyChair. There are four phases to the review process: [bid](#bid), [review](#review), [discussion](#discussion), and [recommendation](#recommendation). In addition to the Program Co-Chairs, two other types of volunteers contribute to this process:
- **Reviewers** provide high-quality reviews for submissions to provide authors with feedback so they may improve their work for presentation or future submission.
- **Associate Program Chairs** (APCs) meta-review each paper and provide a recommendation and feedback to the Program Chairs.

Each *paper* submission will receive 3 reviews and a meta-review.  

All reviews are submitted through EasyChair.  Reviewers are considered "Ordinary PC members" in EasyChair.  APCs are considered "Senior PC members" in EasyChair.

### Dual-Anonymous Review Process
In the dual-anonymous process, submissions are anonymized (so Reviewers and APCs are unaware of the author) and Reviewers and APCs are anonymous to each other and the authors.  During the discussion of a paper in EasyChair, Reviewers can refer to each other by their Reviewer number on that  paper’s review.

## Reviewer and APC Timeline

The following dates describe the timeline for Reviewer & APC work on SIGCSE TS 2021. Please consider your workload around these dates before accepting a Reviewer or APC invitation.

<div class="table-responsive" style="margin-top: 20px;">
  <table class="table">
      <tbody>
		<tr>
			<td><strong>Timeline Period</strong></td>
			<td><strong>Start Date</strong></td>
			<td><strong>End Date</strong></td>
		</tr>
		<tr>
			<td>Bidding</td>
			<td>{{site.data.cfp.reviewDates[0].bidstart}}</td>
			<td>{{site.data.cfp.reviewDates[0].bidend}}</td>
		</tr>
		<tr>
			<td>Review</td>
			<td>{{site.data.cfp.reviewDates[0].reviewstart}}</td>
			<td>{{site.data.cfp.reviewDates[0].reviewend}}</td>
		</tr>
		<tr>
			<td>Discussion</td>
			<td>{{site.data.cfp.reviewDates[0].discussionstart}}</td>
			<td>{{site.data.cfp.reviewDates[0].discussionend}}</td>
		</tr>
		</tbody>
	</table>
</div>

**APC Recommendation and Meta-Review Deadline**: {{site.data.cfp.reviewDates[0].discussionend}} anywhere on earth (AOE)

## Workload
SIGSE Technical Symposium papers are up to 6 pages with 1 additional page that contains references. 
- **Reviewers:** 3 papers
- **APCs**: 8-9 papers

## Bid

On first authentication to EasyChair, please update your Reviewer profile and include at least 5 topics that you are most qualified to review. If you do not bid, we will use topics to assign papers for review.  

If you are reviewing for the Computing Education Research track, please ensure that you select at least one of the new **Methods Topics**. We will be using these topics to better match Reviewers to papers within their expertise.

**Reviewers** and **APCs** will bid on papers they are interested in reviewing or meta-reviewing during the week between abstract submission and full paper submission.  Please bid for papers where the title and abstract are in your area of expertise.  Bidding will help with assigning papers for review or meta-review that you're qualified and interested in reviewing!

Additionally, please declare any conflicts with submitting authors before bidding!

## Review

### Reviewer Responsibilities

As a **Reviewer**, we ask that you carefully read each submission assigned to you and write a constructive review that concisely summarizes what you believe the submission to be about.  When reviewing a submission, consider:

* The strengths and weaknesses, 
* The contribution to an outstanding SIGCSE TS 2021 program and experience for attendees,
* How it brings new ideas or extends current ideas through replication to the field and practitioners and researchers of computer science education, and
* Additional details about reviewing including track-specific details are provided in the [paper review guidelines](/reviewers/paper-review-guidelines).

{% include reviewreminder.html %}

### APC Responsibilities

As an **APC**, we ask that you carefully read each submission assigned to you and inspect the [paper review guidelines](/reviewers/paper-review-guidelines) for the track you are meta-reviewing. Additionally,

* Ensure that Reviewers are making progress on their tasks. Don't wait to see all reviews entered at the last moment. Instead, encourage partial progress from the Reviewers along the way.
* Use EasyChair to send reminder messages to the Reviewers.

{% include reviewers-discussion.html isPaper=true %}

### Reviewer Responsibilities

As a **Reviewer**, we expect that you engage with the discussion on each paper during the discussion period.  Read the reviews from the other Reviewers and engage in discussion using the Comments feature in EasyChair, until all Reviewers have come to a consensus on the recommendation for acceptance or rejection. During this period you will be able to revise your review based on the discussion, but you are not required to do so.

### APC Responsibilities

As an **APC**, we expect you to lead the discussion among the Reviewers to reach consensus on a recommendation about whether the paper should be accepted or rejected.  You will submit your meta-review and recommendation through EasyChair.

* The goal is not to have Reviewers change or update their scores, though that might happen as a by-product of the discussion.
* The goal is to reach an agreement on the quality of the submission. For example, one Reviewer might find objection with some premises of the paper and give the paper a low score. Another Reviewer might excuse that limitation and give the paper a high score due to the high quality of the results. Both reviews are valid, presumably, and thus their scores should not be updated. But their reviews (and possibly the meta-review) should highlight the trade-offs that result from this discussion, and come up with an agreeable decision to both Reviewers.
* In a few rare cases, the Reviewers will have opposite views and the meta-reviewer should capture the essence of all reviews and leave the recommendation as neutral.

It is important that at no point Reviewers should feel forced to change their reviews, scores, or viewpoints in this process. The APC can disagree with them and communicate that to the Program Co-Chairs as needed, but the APC should NOT force Reviewers to change their review because of a difference in viewpoint.

## Recommendation

After the discussion period, each **APC** will write a meta-review for each of their assigned papers that summarizes the reviews for the papers. 

Please **do not** include your recommendation for acceptance or rejection of a paper in the meta-review.  Instead, use the provided radio buttons to make a recommendation based on your meta-review and the discussion and provide any details in the confidential comments to the chairs (and APC).  As an APC, you will only see a small portion of the submitted papers and a paper you recommend for acceptance may be rejected when considering the full set of submissions.

Additionally, the Program Chairs will request feedback from APCs on the quality of reviews for decisions about future invitations to review for the SIGCSE Technical Symposium.

{% include reviewers-recalcitrant.html %}
