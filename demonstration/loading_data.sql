create table tempTeam (
	teamName text, 
	league text
);

\copy tempTeam from team.csv delimiter ',' csv header;

insert into team 
select distinct teamName, league 
from tempTeam 
order by league;


create table tempPlayer (
	playerName text, 
	teamName text
);

\copy tempPlayer from player.csv delimiter ',' csv header;

insert into player 
select distinct playerName, teamName 
from tempPlayer 
order by teamName;


create table tempMatch (
	gameID text,
	length int not null,
	patch float not null,
	blue text not null,
	red text not null,
	result text not null
);

\copy tempMatch from match.csv delimiter ',' csv header;

insert into Match 
select distinct gameID, length, patch, blue, red, result
from tempMatch 
order by gameID;


create table tempTimeline (
	gameID text, 
	teamName text, 
	killsAt10 int,
	killsAt15 int,
	goldAt10 int,
	goldAt15 int,
	drakes int
);

\copy tempTimeline from timeline.csv delimiter ',' csv header;

insert into TeamScoreboard 
select gameID, teamName, killsAt10, killsAt15, goldAt10, goldAt15, drakes
from tempTimeline 
order by gameID;

create table tempPlayerScoreboard (
	gameID text, 
	playerName text, 
	position text, 
	kills int, 
	gold int, 
	visionScore float
);

\copy tempPlayerScoreboard from scoreboard.csv delimiter ',' csv header;

insert into PlayerScoreboard 
select gameID, playerName, position, kills, gold, visionscore
from tempPlayerScoreboard 
order by gameID;

drop table tempMatch, tempPlayer, tempPlayerScoreboard, tempTeam, tempTimeline;
