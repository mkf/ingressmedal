ingressmedal
============

AP and medals counting for Ingress (game from Niantic Labs (a Google company))

Usage
---------

####The program is currently at an early stage of development, but it works well and already has many interesting features.

 * It can OCR the stats for you from the Ingress profile image
 * It can store data about many agents
 * It can print you the amount of AP you gained from different actions and their percentage of total AP.
 * It can save your entry to XML.
 * It can read your data from XML and tell you your average number of [attribute] per week between entries.
 * It can plot you a chart containing climbing to medals based on the XML database file, at the moment you can only view it from pyplot GUI, change the view (crop,resize), and save it from pyplot GUI.


 * ./ocrentryandcuranalyze.py — analyze single entry and/or append it to the database
 * ./entryandcuranalyze.py — the same, except it doesn't have OCR
 * ./pastgainpweekbetwentrs.py — calculates your average gain of parameters per week between entries
 * ./plotmedalclimbing.py — plot a chart containing climbing to medals based on the XML database file, at the moment you can only view it from pyplot GUI, change the view (crop,resize), and save
 

Program currently works only in text-only mode, except for sometimes pyplot GUI being opened.

###Search GMail for mails:
 * **edits**: *"Ingress Portal Data Edit Accepted:"*
 * **photos**: *"Ingress Portal Photo Accepted:"*
 
###What are the 'Uncomputables"?

The uncomputables are those values or parts of values, which can't be calculated. They are listed in the "AP-whereitcomesfrom-mindmap.mm" FreeMind mindmap in the info/ directory.

Why
---------

 * I'm learning Python
 * I love Ingress
 * I may accidentally create something... useful ;p