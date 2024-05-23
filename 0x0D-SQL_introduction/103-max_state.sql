-- Displays the max temperature of each state, ordered by state name.
SELECT `city`, MAX(`value`) AS `max_temp` FROM `temperature` GROUP BY `state` ORDER BY `state`;