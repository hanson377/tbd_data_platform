
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}

with 

base as (
select 
 week,
 path,
 n_pageviews,
 row_number() over (partition by week order by n_pageviews desc) as desc_ranker
from (
select 
 date_trunc('week',timestamp) as week,
 properties___pathname as path,
 count(distinct id) as n_pageviews
 
from {{ source('posthog_source', 'events') }}

where event = '$pageview'
and path ilike '%/journal/%'
AND date_trunc('week', timestamp::date) = date_trunc('week', current_timestamp::date) - INTERVAL 1 WEEK
group by 1,2
)
)
select * from base
where desc_ranker <= 10
order by 3 desc
