use role accountadmin; 

alter account set QUOTED_IDENTIFIERS_IGNORE_CASE = true;

create or replace database person; 
create or replace database sales; 
create or replace database production; 
create or replace database analytics; 
