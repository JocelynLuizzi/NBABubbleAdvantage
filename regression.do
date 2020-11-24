clear all
set more off

// Change path and import file
cd "/Users/jocel/OneDrive/Documents/1433long/"
import delimited "2018_19_20_dataset.csv"

// create totals columns for relevant variables
gen fouls = hpf+apf
gen fouldiff = apf-hpf
gen turnovers = hturnover + aturnover


// Check averages for control and treatment
sum hpf if bubble==1
sum hpf if bubble==0
sum apf if bubble==1
sum apf if bubble==0
sum fouls if bubble==1
sum fouls if bubble==0
sum fouldiff if bubble==1
sum fouldiff if bubble==0


// check to see if more mistakes are made in the bubble generally
regress turnovers bubble
logit bubble turnovers

// Primary regression
regress fouldiff bubble outcome aturnover hturnover h3ptatt a3ptatt hfgatt afgatt hfgmade afgmade

// Alternative regression equations to get more nuance in effect
regress hpf bubble apf outcome aturnover hturnover hfgatt afgatt hfgmade afgmade h3ptatt a3ptatt 

regress apf bubble hpf outcome aturnover hturnover h3ptatt a3ptatt hfgatt afgatt hfgmade afgmade

regress fouls bubble outcome aturnover hturnover h3ptatt a3ptatt hfgatt afgatt hfgmade afgmade
