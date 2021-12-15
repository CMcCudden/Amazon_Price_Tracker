From the time that a user starts running this program, it will check every 30 seconds to see if there was a decrease to 
the desired price (in this case, 75% of the list price) or less. Once the price is low enough, you would be sent an email 
notifying you of the current discount as well as the link to the item you've been watching. 

Can easily be repurposed for any product or price point by changing the "URL" and "desired_price" variables. Additonally,
you would need to set your own HTTP headers specific to your region and system that you're using. You can locate that at:
http://myhttpheader.com/ . At the very least, you will need to establish the "Accept-Language" and "User-Agent" headers.