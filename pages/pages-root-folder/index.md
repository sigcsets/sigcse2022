---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
mediaplayer: true
layout: frontpage
header:
  image_fullwidth: sigcse2021-logo-header.png
widget1:
  title: "2021 Schedule is Live!"
  url: '/schedule'
  image: schedule-widget.png
  text: 'See the schedule for the first virtual Technical Symposium along with commentary on how it was created!'
# widget2:
#   title: "Submit to SIGCSE TS!"
#   url: '/authors'
#   text: 'See the Call for Papers for more information on submitting to SIGCSE TS 2021!'
#   image: ribbons-widget.png
widget2:
  title: "Statement on Equity"
  url: '/equity'
  image: widget-2021logo.png
  text: 'A statement from the SIGCSE TS 2021 chairs, published in the SIGCSE Bulletin.'
#
# Use the call for action to show a button on the frontpage
#
# To make internal links, just use a permalink like this
# url: /getting-started/
#
# To style the button in different colors, use no value
# to use the main color or success, alert or secondary.
# To change colors see sass/_01_settings_colors.scss
#
callforaction:
  url: https://easychair.org/conferences/?conf=sigcse-ts2021
  text: Login to EasyChair ›
  style: alert
permalink: /index.html
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: true
aside: true
---
<div align="center"><iframe width="560" height="315" src="https://www.youtube.com/embed/BAoyHUvSt4M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>