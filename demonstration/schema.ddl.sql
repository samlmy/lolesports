drop schema if exists LolEsport cascade;
create schema LolEsport;
set search_path to LolEsport;

create table Team ( 
	teamName text,
	league text not null,
	primary key (teamName)
);

create table Player (
	playerName text,
	teamName text not null,
	primary key (playerName, teamName),
	foreign key (teamName) references Team(teamName)
);

create table Match (
	gameID text,
	length int not null,
	patch text not null,
	blue text not null,
	red text not null,
	result text not null,
	primary key (gameID), 
	foreign key (blue) references Team(teamName),
	foreign key (red) references Team(teamName)
);

create table TeamScoreboard (
	gameID text, 
	teamName text,
	killsAt10 int,
	killsAt15 int,
	goldAt10 int,
	goldAt15 int,
	drakes int,
	primary key (gameID, teamName),
	foreign key (gameID) references Match(gameID),
	foreign key (teamName) references Team(teamName)
);

create table PlayerScoreboard (
	gameID text, 
	playerName text, 
	position text not null, 
	kills int, 
	gold int, 
	visionScore int,
	primary key (gameID, playerName), 
	foreign key (gameID) references Match(gameID)
);
