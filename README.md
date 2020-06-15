# freddygotfavoured.py
## Favouring tweets based on seed accounts
Enter a set of 'seed' acounts that you trust into this script and every 30 minutes it will randomly take something that one of these accounts has favourited and will favourite it for you.

![freddy](https://media3.giphy.com/media/10QmL848TB5AK4/giphy.gif?cid=ecf05e477df0abb3d40bf3572d539fa63a2efef884124706&rid=giphy.gif)


Install requirements:
```
pip install -r requirements.txt

```
To setup:
Add your Twitter app credentials (https://developer.twitter.com/en/apps) to:
```
consumer_key
consumer_secret
access_token
access_token_secret
```

Add the seed accounts you want to use  to:
```
users = ["thetafferboy", "googleanalytics"]
```


To run continually
```
freddy.sh
```
Is a shell file that will work on Raspberry Pi that will run the script once every 30 minutes.


To run once
```
python freddy.py
```

