# VT-Hacks-IX

By: James DeLoach, Grady Orr, Marcos Fassio Bazzi, and Patrick Dewey

## Inspiration
As students who are taking and have taken lots of CS classes, one thing we all noticed is the lack of good and consistent systems for managing TA office hours, and queue systems for meeting with them. We wanted to create a discord bot that makes it easy and viable to use discord as a universal platform to meet with TAs and get help with classes.
## What it does
This bot tracks users that register their "office hours" with the bot, and keeps an internal schedule of when office hours are taking place. During that time, people conducting office hours would open up a queue for students to request help through. As people are served, they are sent a notification to remind them to attend office hours.
## How we built it
We used Pycord, which adapts the javascript discord API into python-friendly 'async IO' calls. This library can be found at . We programmed a help function which uses discord embeds which makes text more user-friendly within a message from the program. The underlying structure of the queuing system is list-based within python such that a user is removed from the data structure when every entry placed in before them is served.
## Challenges we ran into
We attempted to synchronize office hours with an external source such as Google Calendar or a iCalendar file, but were unsuccessful in our implementation. 
## Accomplishments that we're proud of
A few members of our team had worked with other iterations and forks of the Discord API before, but something that we were proud of in this development was the "reload_cogs" command that we added in our initial fork. This allows the team to work asynchronously over github and still be able to work on their half-baked scripts without having to worry about "breaking the build" by running the script locally on their machine and testing it over Discord. This allowed for quick fixes to be made, and allowed the developer to quickly make any changes necessary for the proper functioning of the bot.
## What we learned
Our team is a little inexperienced with hackathons, with two of us participating in our first hackathon this weekend. We did not have a lot of ideas heading into the event, but that allowed us to use the first bit of time to brainstorm and come up with ideas for our project. With that, though, we were a little too ambitious with our ideas for the Office Hours Q-bot and took on a little too much to complete essentially within one day. Next time, I think we would have a better idea of what our expectations to handle within one hackathon are and hopefully have a well-thought-out idea heading into the event.
## What's next for Office Hours Q-Bot
I think we would like to add a few features in the future, such as voice channel integration, in which the bot checks to see if the next person up within the queue is in a lobby voice channel and moves them automatically into a voice channel with the TA that removed them from the queue to be helped. More features focused on user data would also be something that could be really interesting for such an application.