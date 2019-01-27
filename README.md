# Twitter Terminal
#### This is a way to tweet from a GroupMe group chat.
## Why?
Suppose you have a shared Twitter account for an organization. As the leadership within the organization changes, you do not have to keep track of who has the password to the account and no longer have to worry about sharing credentials. Simply add the members that are allowed to tweet to a group chat. It can also be helpful for a group of organizers to tweet updates about an event and throughout an event.
## Commands:
"@bot#tweet: &lt;insert text here&gt;" This will tweet the text.  
"@bot#pic: &lt;word&gt; Will check if there is a r/<word> subreddit, pick a random picture from 150 of the hot posts and tweet the picture.   Example: "@bot#pic: cat" will tweet a picture of a cat pulled from reddit.com/r/cat 
## Set up:
  1. Ensure you have bot.key.txt , reddit.key.txt , twitter.key.txt in the config/ directory. Alternatively you can set environment variables for the follwing: GroupMe bot id, reddit client id, reddit client secret, twitter consumer key, twitter consumer secret, twitter access token, twitter access secret. 
### bot.key.txt:
  GroupMe bot ID 
 ### twitter.key.txt (each item on a new line):
  consumer key  
  consumer secret  
  access token  
  access secret  
 ### reddit.key.txt (each item on a new line):
  reddit client id  
  reddit client secret
 ### Note that there should be no information in the files other than the actual key values.
  2. Create a bot at https://dev.groupme.com/bots and set the callback url as the root url for your web server.
  3. Run the flask application on the server. I personally deploy it to Heroku. Be sure to use Python 3 or some dependencies will not work. 
